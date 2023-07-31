import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json
from eth_abi import decode
import secrets
import psycopg2
import sqlite3


def extract_data_from_postgre(date, time, employee_id):
  # Connect to the remote PostgreSQL server
  conn = psycopg2.connect(
      host="192.168.1.238",
      port=5432,
      dbname="mydata",
      user="postgres",
      password="1126"
  )

  # Open a cursor to perform database operations
  cursor = conn.cursor()
  rows = cursor.execute("select research_data from recort where date = (%s) and time = (%s) and employee_id = (%s)", (date, time, employee_id,))
  rows = cursor.fetchall()
  
  if len(rows) > 1:
      print("Warning: Multiple rows returned for the given parameters. Selecting the first row only.")
  
  conn.commit()
  conn.close()
  
  if len(rows) > 0:
    return rows[0][0]
  else:
      return None


def encrypt(research_data):
  # Create a SHA256 hash of the research_data
  hash_object = hashlib.sha256()
  
  # Set encryption key and initialization vector
  encryption_key = 'mysecretpassword'
  iv = b'initialvector123'
  
  # Create the AES-GCM cipher
  cipher = AES.new(encryption_key.encode(), AES.MODE_GCM, iv)
  
  # Encrypt the hash with the cipher
  cipher_text, tag = cipher.encrypt_and_digest(research_data.encode())
  
  # Concatenate the iv, cipher text, and tag
  encrypted_data = iv + cipher_text + tag
  
  # Encode the encrypted data using base64
  base64_data = base64.b64encode(encrypted_data)
  
  return base64_data


def write_data_to_contract(date, time, employee_id, base64_data):

  # Connect to the web3 provider and middleware
  web3_http = Web3(HTTPProvider('http://127.0.0.1:5002'))
  web3_http.middleware_onion.inject(geth_poa_middleware, layer=0)

  private_key = secrets.token_bytes(32)

  # Set account address and contract address
  myAccount = '0x280bA7e0730F73Ae31604698211aA493CC485eE6'
  contractAddress = '0x7b2A0D4Ac83bb00b48f82ef25DE19f1edd33A7e2'

  # Load the contract ABI from myAbi.json
  with open('myAbi.json', 'r') as f:
      abi = json.load(f)

  # Load the contract using the ABI and the contract address
  contract = web3_http.eth.contract(address=web3_http.to_checksum_address(contractAddress), abi=abi)
  
  # Write the encrypted data to the contract
  tx_hash = contract.functions.write(base64_data.decode()).transact({'from': myAccount})

  # Wait for the transaction to be mined
  receipt = web3_http.eth.wait_for_transaction_receipt(tx_hash)
  
  # Connect to the database
  conn = sqlite3.connect('search.db')
  c = conn.cursor()
  c.execute("INSERT INTO search (date, time, employee_id, transactionHash_str) VALUES (?, ?, ?, ?)", (date, time, employee_id, tx_hash))
  conn.commit()
  conn.close()
  
  return tx_hash
  

def read_data_from_contract(tx_hash):
  # connect to a local Ethereum node
  web3 = Web3(HTTPProvider('http://127.0.0.1:5002'))
  
  # load the ABI file for the contract that generated the transaction
  with open('myAbi.json', 'r') as f:
      abi = json.load(f)

  # create a Contract object using the ABI and the contract address
  contract_address = web3.to_checksum_address('0x7b2A0D4Ac83bb00b48f82ef25DE19f1edd33A7e2')
  contract = web3.eth.contract(address=contract_address, abi=abi)

  # get the transaction object
  tx = web3.eth.get_transaction(tx_hash)
  # decode the input data of the transaction using the Contract object
  fn_name, args = contract.decode_function_input(tx.input)  
  
  return args['_str']
    

def decrypt(encrypted_data):
  encryption_key = 'mysecretpassword'
  
  # Decode the base64-encoded input string
  decoded_data = base64.b64decode(encrypted_data)
  
  # Extract the iv, cipher text, and tag from the decoded input data
  iv1 = decoded_data[:16]
  cipher_text1 = decoded_data[16:-16]
  tag1 = decoded_data[-16:]
  
  # Create the AES-GCM cipher using the encryption key and iv
  encode_enc_key=encryption_key.encode()
  cipher = AES.new(encode_enc_key, AES.MODE_GCM, iv1)
  
  # Try to decrypt the cipher text using the cipher and tag
  try:
      decrypted_data = cipher.decrypt_and_verify(cipher_text1, tag1).decode()

      return decrypted_data
  except ValueError:
      print("Decryption unsuccessful: Incorrect tag or padding")
