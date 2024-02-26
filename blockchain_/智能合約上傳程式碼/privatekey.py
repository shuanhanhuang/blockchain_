from web3 import Web3
from eth_account import Account

# Replace with the path to your keystore file and password
keystore_path = '/home/node1/user/mypbc/node1/keystore/UTC--2023-11-11T15-42-54.407964899Z--d47d2cf2efc5fc095da3734e5ea4e6ade063956a'
password = 'node1'

# Load keystore file
with open(keystore_path) as f:
    keystore_json = f.read()

# Decrypt private key
private_key = Account.decrypt(keystore_json, password)

# Create an account object from the private key
#account = Account.privateKeyToAccount(private_key)

# Print the address and private key
#print("Address:", account.address)
print("Private Key:", private_key.hex())
