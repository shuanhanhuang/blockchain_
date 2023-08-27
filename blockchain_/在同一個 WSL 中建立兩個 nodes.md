// 在 home/user 下建立一個新的目錄 mypbc
> cd mypbc

// 在 home/user/mypbc 下再建立兩個新的目錄別是 node1 和 node2
> mkdir node1 node2

// 在 home/user/mypbc 下的 node1 中建立第一個新的 以太坊帳戶
> geth --datadir node1 account new
  % 以下是 Console 訊息
	Your new account is locked with a password. Please give a password. Do not foget this password.
	Password:
	Repeat password:

	Your new key was generated

	Public address of the key:   0x7043130cD282a13cB9D7d11B951BF81C0EbFeEA9
	Path of the secret key file: node1/keystore/UTC--2022-12-31T02-18-15.200527400Z--7043130cd282a13cb9d7d11b951bf81c0ebfeea9

// 在 home/user/mypbc 下的 node2 中再建立一個新的 以太坊帳戶
> geth --datadir node2 account new
  % 以下是 Console 訊息
	Your new account is locked with a password. Please give a password. Do not foget this password.
	Password:
	Repeat password:

	Your new key was generated

	Public address of the key:   0x10d6cE216ce0d76F86625Fb49EF24d45Ea86A73D
	Path of the secret key file: node2/keystore/UTC--2022-12-31T02-19-28.461470700Z--10d6ce216ce0d76f86625fb49ef24d45ea86a73d
	
// 編輯一個 genesis.json，供 node1 及 node2 下一個步驟初始化以太坊節點使用，將其存放在 home/user/mypbc。
> vi genesis.json
{
  "config": {
    "chainId": 12345,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "muirGlacierBlock": 0,
    "berlinBlock": 0,
    "londonBlock": 0,
    "arrowGlacierBlock": 0,
    "grayGlacierBlock": 0,
    "clique": {
      "period": 5,
      "epoch": 30000
    }
  },
  "difficulty": "1",
  "gasLimit": "1000000",
  "extradata": "0x00000000000000000000000000000000000000000000000000000000000000007043130cD282a13cB9D7d11B951BF81C0EbFeEA90000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "alloc": {
    "7043130cD282a13cB9D7d11B951BF81C0EbFeEA9": { "balance": "1000000000000000000000000000" },
    "10d6cE216ce0d76F86625Fb49EF24d45Ea86A73D": { "balance": "1000000000000000000000000000" }
  }
}

// 初始化在 node1 和 node2 的以太坊
> geth --datadir node1 init genesis.json
> geth --datadir node2 init genesis.json

// 開啟另一個 WSL 終端，先建立 node1 的以太坊帳戶密碼檔案
> cd mypbc

// 在編輯軟體中寫入密碼
> vi node1/password.txt

// 以下命令啟動 node1 的以太坊，{可能無法}讓 Remix 連結
> geth --datadir node1 --networkid 12345 --port 30306 --syncmode "full" --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,db,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0x7043130cD282a13cB9D7d11B951BF81C0EbFeEA9 --password node1/password.txt console

// 以下命令啟動 node1 的以太坊，讓 Remix 可以透過 http://127.0.0.1:5002 連結
> geth --datadir node1 --networkid 12345 --port 30306 --syncmode "full" --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "https://remix.ethereum.org" --vmdebug --http.api "personal,db,eth,net,web3,txpool,miner, debug" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0x7043130cD282a13cB9D7d11B951BF81C0EbFeEA9 --password node1/password.txt --dev console

// 再開啟另一個 WSL 終端，先建立 node2 的以太坊帳戶密碼檔案
> cd mypbc

// 在編輯軟體中寫入密碼
> vi node2/password.txt

// 以下命令啟動 node2 的以太坊，{可能無法}讓 Remix 連結
> geth --datadir node2 --networkid 12345 --port 30307 --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "*"  --http.api "personal,db,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x10d6cE216ce0d76F86625Fb49EF24d45Ea86A73D --password node2/password.txt console

// 以下命令啟動 node1 的以太坊，讓 Remix 可以透過 http://127.0.0.1:5003 連結
>>>>> if Connect to Remix <<<<< !!!!! 還沒試出來能在有 node2 的情況下，讓 Remis 連的到 !!!!!
> geth --datadir node2 --networkid 12345 --port 30307 --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "https://remix.ethereum.org" --vmdebug  --http.api "personal,db,eth,net,web3,txpool,miner,debug" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x10d6cE216ce0d76F86625Fb49EF24d45Ea86A73D --password node1/password.txt --dev console

// 進入 node2 Geth 的環境，用以下命令建立 node2 成為 node1 的 peer，可讓 node1 與 node2成為一個私有以太坊。 
> admin.addPeer("enode://0cb1759d35bcfe42b6b098251519129a57e8191647346913510ebee7dabcc6223b0afed4d3ac3cb631c81dd6715ee85cf902d89eae2cc4e3b75195f0d0c0c534@127.0.0.1:30306?discport=0")

// 再開啟一個新的 WSL 終端，進入 node1 的 Geth，可以使用 Geth 命令來和 node1 的 Geth 環境互動，以了解 node1 Geth 的狀態
> geth attach node1/geth.ipc

// 驗證 node1 和 node2 以太坊是否有連結
> admin.peers

// 查詢 node1 的以太坊帳戶有多少錢 {單位: Wei}
> eth.getBalance(eth.accounts[0])

// 再開啟一個新的 WSL 終端，進入 node2 的 Geth，可以使用 Geth 命令來和 node2 的 Geth 環境互動，以了解 node2 Geth 的狀態
> geth attach node1/geth.ipc