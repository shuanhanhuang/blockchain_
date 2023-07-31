# A. Install Ubuntu
Check [Ubuntu_Installation.txt](https://github.com/Jenniferwyqq/BlockChain/blob/main/Installation/Ubuntu_Installation.txt)

# B. Install a Private Ethereum Network

## Install Geth on each computer
1. Add the Ethereum repository to your system'
  ```
  sudo add-apt-repository -y ppa:ethereum/ethereum
  ```
If ERROR is encountered: `‘~ethereum‘ user or team does not exist`, can refer to [this article](https://blog.csdn.net/taozi550185271/article/details/115175708?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-115175708-blog-104215270.pc_relevant_recovery_v2&spm=1001.2101.3001.4242.1&utm_relevant_index=3).

2. Update system
  ```
  sudo apt-get update
  ```
3. Install Ethereum
  ```
  sudo apt-get install ethereum
  ```
4. Upgrade geth
  ```
  sudo apt-get upgrade geth
  ```
  
## Create nodes on each computer (for each node, repeat the command, replacing node1 to node2, node3 etc)
1. Open a new terminal window
2. Create a directory for node
  ```
  mkdir node1
  ```
3. Create a new account for the node
  ```
  geth --datadir node1 account new
  ```
   Your new account is locked with a password. Please give a password. Do not foget this password.
   
   ```
   Password:
   
   Repeat password:

   Your new key was generated

   Public address of the key: 0xC1B2c0dFD381e6aC08f34816172d6343Decbb12b
   
   Path of the secret key file: node1/keystore/UTC--2022-05-13T14-25-49.229126160Z--c1b2c0dfd381e6ac08f34816172d6343decbb12b
   ```

   - You can share your public address with anyone. Others need it to interact with you.
   - You must NEVER share the secret key with anyone! The key controls access to your funds!
   - You must BACKUP your key file! Without the key, it's impossible to access account funds!
   - You must remember your password! Without the password, it's impossible to decrypt the key!

   Both password and "Public address of the key" must be remembered,
   "Public address of the key" will be used in the parameters of many geth commands, and it must be changed to genesis.json,
   The "Public address of the key" of node1 will be used in two places in genesis.json
   The "Public address of the key" of node2 and node3 will be used in one place in genesis.json

So you have to wait for ndeo1,2,3 "Public address of the key" to have a complete grnrsis.json
  
4. Save the [genesis.json 文件](https://github.com/Jenniferwyqq/BlockChain/blob/main/genesis.json), and replace the node account address
5. Initialize the Genesis block
  ```
  geth --datadir node1 init genesis.json
  ```
  
## add password for each node (for each node, repeat the command, replacing node1 to node2 etc)
1. Open a new terminal window
2. Write password in editing software
  ```
  vi node1/password.txt
  ```

# C. Start the Ethereum

## Run below code to start the Ethereum
1. node1 
  ```
  geth --datadir node1 --networkid 12345 --port 30306 --syncmode "full" --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "*"  --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0x251faDa5F25C6Ef2A949FA74CE28265F3090F7C6 --password password.txt console
  ```
  
  Note: "0x251faDa5F25C6Ef2A949FA74CE28265F3090F7C6" should be replaced with the "Public address of the key" obtained by the node when creating the account.
  
2. node2
  ```
  geth --datadir node2 --networkid 12345 --port 30307 --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "*"  --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x68e0f231dbf61485A023C1564e5592aA8276EA4C --password password.txt console
  ```
  
  Note: "0x68e0f231dbf61485A023C1564e5592aA8276EA4C" should be replaced with the "Public address of the key" obtained by the node when creating the account.

3. node3
  ```
  geth --datadir node3 --networkid 12345 --port 30308 --syncmode "full" --nodiscover --http --http.port "5004" --http.addr "0.0.0.0" --http.corsdomain "*"  --http.api "personal,db,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6004" --allow-insecure-unlock --unlock 0xf47e13ABf553FeE98a686f12C7Dd120A7be39c68 --password password.txt console
  ```
  
  Note: "0xf47e13ABf553FeE98a686f12C7Dd120A7be39c68" should be replaced with the "Public address of the key" obtained by the node when creating the account.

## Each node will partner the other two in the Geth environment (for each node, repeat the command, replacing node1 to node2 etc)
```
admin.addPeer("enode://73b5bc4c927713a2bdd5d5fdecad346da0f28acf67e9ef92d3720907f62fbef023b52a5a8c53bb8f03b50abd264eb57b7adc3a32598e55db66995b7616f6d29a@192.168.1.101:30307?discport=0")
 ```

 Note: "73b5bc4c927713a2bdd5d5fdecad346da0f28acf67e9ef92d3720907f62fbef023b52a5a8c53bb8f03b50abd264eb57b7adc3a32598e55db66995b7616f6d29a@192.168.1.101:30307?discport=0" should be replaced with the other two get the enode position when executing the "admin.nodeInfo.enode" command.

## Each node should be in the Geth environment to allow the other two to mine together. (repeat the code on different node)
  ```
  clique.propose("0x68e0f231dbf61485A023C1564e5592aA8276EA4C", true) 
  ```
  
  Note: "0x68e0f231dbf61485A023C1564e5592aA8276EA4C" should be replaced with the "Public address of the key" obtained by the node when creating the account.

## Each node should start mining in the Geth environment (repeat the code on different node)
  ```
  miner.start()
  ```
  
  After executing miner.start(), if you see the message [`WARN [05-17|17:26:19.061] Block sealing failed err="signed recently, must wait for others`](Installation/bchain_success.jpg) continuously in the mining information screen in the terminal, it indicates successful connection of mining actions among the three nodes.
  
 Note: If miner.start() appears that Etherbase is not specified, type the following command (repeat the code on different node)
 ```
 miner.setEtherbase("0xf47e13ABf553FeE98a686f12C7Dd120A7be39c68")  
 ```
 
 Note: "0x68e0f231dbf61485A023C1564e5592aA8276EA4C" should be replaced with the "Public address of the key" obtained by the node when creating the account.

## Open another Geth terminal
You can open another terminal for each node and use the geth command to monitor the running status of the node in the geth environment or execute other geth commands.

# D. Install Libraries on Node1
## Download libraries
1. install pip
```
sudo apt update
sudo apt install python3-pip
```

2. install sqlite3
```
sudo apt install sqlite3
pip3 install pysqlite3
```

3. install psycopg
```
sudo apt-get install python3-psycopg2
```

4. install requirements.txt
```
pip3 install -r requirements.txt
```

## Build sqlite database
1. create search database
```
sqlite3 search.db
```
2. create search table
```
python3 sqlite_database.py
```
      
## Change variable in python_function.py
1. In extract_data_from_postgre() function, this is my postgresql info, we should replace with owner's postgresql database
```
conn = psycopg2.connect(
      host="192.168.1.238",
      port=5432,
      dbname="mydata",
      user="postgres",
      password="1126"
)
```

2. In encrypt() function, we should replace encryption_key and iv. The encryption_key and iv have a length of 16 bytes, which is 128 bits.

   encryption_key = 'mysecretpassword'

   iv = b'initialvector123'

3. In write_data_to_contract(), we should replace myAccount and contractAddress (blockchain)

   myAccount = '0x280bA7e0730F73Ae31604698211aA493CC485eE6'

   contractAddress = '0x7b2A0D4Ac83bb00b48f82ef25DE19f1edd33A7e2'

4. read_data_from_contract read_data_from_contract , we should replace contractAddress (blockchain)

   contractAddress = '0x7b2A0D4Ac83bb00b48f82ef25DE19f1edd33A7e2'

5. In decrypt() function, we should replace encryption_key, it should be same as the encryption_key in encrypt() function. 

   encryption_key = 'mysecretpassword'
      
6. Execute flask app
```
export FLASK_APP=app.py
```


## Run flask application

1. Open a WSL terminal, navigate to the directory where the program is located, and enter the following code:
```
flask run
```
2. Open a Chrome browser

Enter the following URL in the address bar for the data upload page: `http://localhost:5000/upload`

Enter the following URL in the address bar for the data transaction page: `http://localhost:5000/transactions`

# E. Exit the Application
##  Stop flask application
Typing ```ctrl``` + ```C``` in the WSL terminal where you ran the Flask application.

##  Enter the following two lines in the WSL terminal for node1 to stop the mining process:
```miner.stop()```

```ctrl``` + ```D```
##  Enter the following two lines in the WSL terminal for node2 to stop the mining process:
```miner.stop()```

```ctrl``` + ```D```
