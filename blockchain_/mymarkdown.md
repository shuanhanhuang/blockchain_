# 壹. 安裝 Ubuntu
請參考 .\BlockChain-main\Installation\Installation\Ubuntu_Installation.txt 檔案

# 貳. 安裝私有乙太坊

   本計畫之私有以太坊將由三個以太坊節點，各自跑在一台獨立的計算空間(例如，獨立的電腦或VM)。參各節點將命名為 node1、node2、和 node3，並且以 node1 為主要節點。因此 node1 除了扮演一個乙太坊節點的角色外，也將負責運行本計畫所有和乙太坊互動的所有軟體。
- ## 在每台電腦的 Ubuntu 作業系統中安裝乙太坊的節點軟體 (Geth) 下載最新版geth方法
1. 到 Ubuntu 命令視窗中輸入下列指令來將將以太坊存儲庫添加到您的 Ubuntu 系統 
  ```
  sudo add-apt-repository -y ppa:ethereum/ethereum
  ```
2. 在 Ubuntu 命令視窗中輸入下列指令來更新 Ubuntu 作業系統
  ```
  sudo apt-get update
  ```
3. 在 Ubuntu 命令視窗中輸入下列指令來在這台電腦的 Ubuntu 中開始安裝乙太坊節點
  ```
  sudo apt-get install ethereum
  ```
4. 在 Ubuntu 命令視窗中輸入下列指令來更新乙太坊節點軟體
  ```
  sudo apt-get upgrade geth
  ```

※ 刪除geth 
   ```
   sudo apt-get remove geth
   ```

- ## 在每台電腦的 Ubuntu 作業系統中安裝乙太坊的節點軟體 (Geth) 下載geth 1.11.06

1. 到 https://geth.ethereum.org/downloads  安裝 1.11.06版本 壓縮檔
   或是
   ```
   wget https://gethstore.blob.core.windows.net/builds/geth-linux-arm6-1.11.6-ea9e62ca.tar.gz
   ```
2. 解壓縮檔案
   ```
   tar -xzvf geth-linux-amd64-1.11.06-ea9e62ca
   ```
3. 將資料夾中(geth-linux-amd64-1.11.06-ea9e62ca)的 geth 檔案 移到 /usr/loacl/bin/
   ```
   sudo mv geth-linux-amd64-1.11.06-ea9e62ca/geth /usr/local/bin/
   ```
4. 啟動
   ```
   sudo chmod +x /usr/local/bin/geth
   ```
5. 檢查是否安裝成功
   ```
   geth version
   ```
請在另外兩台電腦的 Ubuntu 作業系統上以同樣的步驟，各自安裝一個以太坊節點軟體。
  
6. 接下來，在在三台電腦的 Ubuntu 作業系統上，各自建立一個以太坊節點，並請將這三台電腦的以太坊節點分別命名為 node1，node2、和 node3，步驟如下：

&ensp;&ensp;(1). 請再開啟一個 Ubuntu 命令視窗

&ensp;&ensp;(2). 在 home 下建立一個新的目錄 user，home/user 下建立一個新的目錄 mypbc

  ```
        mkdir user
        mkdir mypbc
  ```
&ensp;&ensp;(3). 輸入以下指令來建立一個節點的目錄 (另外兩台電腦，請將以下指令中的 node1 分別換成 node2 和 node3)
   
  ```
        mkdir node1 node2 node3
  ```
&ensp;&ensp;(4). 輸入以下指令來為這個節點建立以太坊帳戶 (另外兩台電腦，請將以下指令中的 node1 分別換成 node2 和 node3)
  ```
        geth --datadir node1 account new
  ```
&ensp;&ensp;(5). 您將會在 Ubuntu 命令視窗上看到以下英文訊息，此時請在 [Password:] 和 [Repeat password:]  為這個帳戶輸入兩次相同的密碼。

   ```
   Your new account is locked with a password. Please give a password. Do not foget this password.
   
   Password:
   
   Repeat password:

   Your new key was generated

   Public address of the key: 0xC1B2c0dFD381e6aC08f34816172d6343Decbb12b
   
   Path of the secret key file: node1/keystore/UTC--2022-05-13T14-25-49.229126160Z--c1b2c0dfd381e6ac08f34816172d6343decbb12b

   - You can share your public address with anyone. Others need it to interact with you.
   - You must NEVER share the secret key with anyone! The key controls access to your funds!
   - You must BACKUP your key file! Without the key, it's impossible to access account funds!
   - You must remember your password! Without the password, it's impossible to decrypt the key!
   ```
   
   此時請務必記下上面英文訊息中的"密碼(key)和密鑰的公共地址(Public address of the key)”，因為在後續的以太坊指令中都會需要用到這兩個資訊。
   例如，node1 的“密鑰的公共地址”將用在以太坊的創生檔案( genesis.json ) 中的兩個地方，而 node2 和 node3 的 “密鑰的公共地址”也將用在以太坊的創生檔案( genesis.json )中的一個地方。
   也因此，我們必須等待到 三個以太坊節點的 “密鑰的公共地址” 都得到了，才能有完整的以太坊的創生檔案( genesis.json )。 
  
7. 請找到 .\BlockChain-main\ 目錄中的以太坊的創生檔案( genesis.json )，並進行以下修改：  
   (1). 請將其第 24 行和第 26 行各自的八組 NODE1 (各自共 40 個字元) 改成上面得到的 node1 的"密鑰的公共地址(Public address of the key)”。  
   (2). 請將其第 27 行的八組 NODE2 (共 40 個字元) 改成上面得到的 node2 的"密鑰的公共地址(Public address of the key)”。  
   (3). 請將其第 28 行的八組 NODE3 (共 40 個字元) 改成上面得到的 node3 的"密鑰的公共地址(Public address of the key)”。  
   (4). 最後請記得要儲存這個修改後的以太坊的創生檔案( genesis.json )在原來的目錄內。  

8. 接下來，在三台電腦的在 Ubuntu 命令視窗中，各自輸入以下指令來的到每一個以太坊節點的以太坊區塊練的初始化創世區塊

   ※如果三個 node 都在同一台電腦 genesis.json 放在 mypbc 資料夾下

   ※如果三個 node 在不同台電腦 genesis.json 放在home下即可，不用放在node1, node2, node3下
  ```
  geth --datadir node1 init genesis.json
  ```
  
9. 請在三台電腦的在 Ubuntu 命令視窗中，各自輸入以下指令來為每個節點添加一個密碼檔案  
   (1). 開啟一個新的 Ubuntu 命令視窗  
   (2). 在 Ubuntu 的命令視窗中，我們可以使用 Ubuntu 的編輯軟件 (例如 vi, vim) 來在各自節點的密碼檔案中寫入密碼，例如在 node1 節點的密碼檔案中寫入密碼的指令如下  
  ```
  vi node1/password.txt
  ```

# 參. 啟動以太坊節點

   在三台電腦的 Ubuntu 命令視窗中，各自輸入以下指令來啟動每台電腦的以太坊節點
 
- ### 請用以下指令來啟動每台電腦的以太坊節點
1. 請在 node1 的電腦開啟一個 Ubuntu 命令視窗，並輸入以下指令來啟動 node1 的以太坊節點
  ```
   geth --datadir node1 --networkid 12345  --nat extip:"10.0.129.2" --port "5021"  --syncmode "full" --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0xBd367d52531889EbCBA1F53B47FB75ED334262b0 console
  ```

  以下命令啟動 node1 的以太坊，讓 Remix 可以透過 http://127.0.0.1:5002 連結
  ```
   geth --datadir node1 --networkid 12345 --port 30306 --syncmode "full" --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "https://remix.ethereum.org" --vmdebug --http.api "personal,db,eth,net,web3,txpool,miner, debug" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0xBd367d52531889EbCBA1F53B47FB75ED334262b0 console
  ```

  請注意，這個指令中的 "NODE1NODE1NODE1NODE1NODE1NODE1NODE1NODE1" 應該被替換為創建 node1 帳戶時得到的“密鑰的公共地址”。
  
2. 請在 node2 的電腦開啟一個 Ubuntu 命令視窗，並輸入以下指令來啟動 node2 的以太坊節點
  ```
   geth --datadir node2 --networkid 12345 --nat extip:"10.0.129.3" --port 5022  --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27 console
  ```
  
  以下命令啟動 node2 的以太坊，讓 Remix 可以透過 http://127.0.0.1:5003 連結
  ```
   geth --datadir node2 --networkid 12345 --port 30307 --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "https://remix.ethereum.org" --vmdebug --http.api "personal,db,eth,net,web3,txpool,miner,debug" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27 console
  ```

  請注意，這個指令中的 "0xNODE2NODE2NODE2NODE2NODE2NODE2NODE2NODE2" 應該被替換為創建 node2 帳戶時得到的“密鑰的公共地址”。
  
3. 請在 node3 的電腦開啟一個 Ubuntu 命令視窗，並輸入以下指令來啟動 node3 的以太坊節點
  ```
   geth --datadir node3 --networkid 12345 --nat extip:"10.0.129.4" --port 5023 --syncmode "full" --nodiscover --http --http.port "5004" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6004" --allow-insecure-unlock --unlock 0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C console
  ```

  以下命令啟動 node3 的以太坊，讓 Remix 可以透過 http://127.0.0.1:5004 連結
  ```
   geth --datadir node3 --networkid 12345 --port 30308 --syncmode "full" --nodiscover --http --http.port "5004" --http.addr "0.0.0.0" --http.corsdomain "https://remix.ethereum.org" --vmdebug --http.api "personal,db,eth,net,web3,txpool,miner,debug" --authrpc.addr "0.0.0.0" --authrpc.port "6004" --allow-insecure-unlock --unlock 0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C console
  ```
  
  請注意，這個指令中的 "0xNODE3NODE3NODE3NODE3NODE3NODE3NODE3NODE3" 應該被替換為創建 node3 帳戶時得到的“密鑰的公共地址”。
  

### 將每個節點在以太坊的 Geth 環境中與其他兩個節點配對（對每個節點，請重複以下命令，例如將節點 1 替換為節點 2 等）

1. 取得每個節點的 enode 位置，請在上述步驟，進入 Geth 環境內，輸入以下 Geth 指令來得到這個節點的 enode 位址
```
   admin.nodeInfo.enode
```
   Geth 將會回覆這個節點的 enode 位址，格式如下；
```
   "enode://73b5bc4c927713a2bdd5d5fdecad346da0f28acf67e9ef92d3720907f62fbef023b52a5a8c53bb8f03b50abd264eb57b7adc3a32598e55db66995b7616f6d29a@192.168.1.101:30307?discport=0"
```   

2. 在取得三個節點各自的 enode 位址後，我們將利用以下指令，設定 node2 和 node3 成為 node1 的夥伴。請進入 Geth 環境內，輸入以下 Geth 指令
```
admin.addPeer(此處請填 node2 的 enode 位址)
admin.addPeer(此處請填 node3 的 enode 位址)
```

   請注意，上述動作需要在 node2 和 node3 中各運作一次，來設定 node1 和 node3 成為 node2 的夥伴，以及設定 node1 和 node3 成為 node2 的夥伴。成功後，node1、node2、和 node3 就形成一個以 node1 為主點的私有以太坊。

   node1:
   ```
      admin.addPeer("enode://d5a4a280cd254f16bcbc61d0556d103d76ed2a33dde4fd20d6fcb496c554970fa53e560564b435e71fc9260cb912bd78f36c56a0651e5533b06785ba41686c53@10.0.129.3:5022?discport=0")
      admin.addPeer("enode://d00c9735a256dd651f9a56d9a2dea4ee5f13301487d1a77801677bbd8ff50fdc029a60d5068f5df99f8ae4ee50ef74c6c1ed5d349b460c7e0f01d537458b5213@10.0.129.4:5023?discport=0") 
   ``` 
   node2:
   ```
      admin.addPeer("enode://de558f69abdd15b8c082e77af7bb6a7de9109c017ea5a653f2fca8d223659f15fa56f45b86d7acafd6739ac2a516da5533fc864bdb9449cc2cd67dce7d0d7d1c@10.0.129.2:5021?discport=0")
      admin.addPeer("enode://d00c9735a256dd651f9a56d9a2dea4ee5f13301487d1a77801677bbd8ff50fdc029a60d5068f5df99f8ae4ee50ef74c6c1ed5d349b460c7e0f01d537458b5213@10.0.129.4:5023?discport=0")
   ``` 
   node3:
   ```
      admin.addPeer("enode://de558f69abdd15b8c082e77af7bb6a7de9109c017ea5a653f2fca8d223659f15fa56f45b86d7acafd6739ac2a516da5533fc864bdb9449cc2cd67dce7d0d7d1c@10.0.129.2:5021?discport=0")
      admin.addPeer("enode://d5a4a280cd254f16bcbc61d0556d103d76ed2a33dde4fd20d6fcb496c554970fa53e560564b435e71fc9260cb912bd78f36c56a0651e5533b06785ba41686c53@10.0.129.3:5022?discport=0") 
   ``` 

3. 接下來，在各節點進行挖礦前，我們必須告訴各節點，這個私有以太坊的挖礦動作是由三個節點合作輪流挖礦。請進入各節點的 Geth 環境內，輸入以下 Geth 指令。例如，進入 node1 的 Geth 環境後，輸入以下 Geth 指令。

  ```
  clique.propose(此處請填 node2 密鑰的公共地址, true) 
  clique.propose(此處請填 node3 密鑰的公共地址, true) 
  ```
 
   請注意在 node1 密鑰的公共地址前後要加上雙引號，並且上述動作需要在 node2 和 node3 中各運作一次，來設定 讓 node1、node2、和 node3 合作輪流挖礦。 

   node1:
   ```
      clique.propose("0xBd367d52531889EbCBA1F53B47FB75ED334262b0", true)
      clique.propose("0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27", true)
      clique.propose("0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C", true)
   ``` 
   node2:
   ```
      clique.propose("0xBd367d52531889EbCBA1F53B47FB75ED334262b0", true)
      clique.propose("0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27", true)
      clique.propose("0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C", true)
   ``` 
   node3:
   ```
      clique.propose("0xBd367d52531889EbCBA1F53B47FB75ED334262b0", true)
      clique.propose("0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27", true)
      clique.propose("0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C", true)
   ``` 
   
4. 接下來，我們就可以啟動個節點的挖礦動作，請進入各節點的 Geth 環境內，輸入以下 Geth 指令。例如，進入 node1 的 Geth 環境後，輸入以下 Geth 指令。
  ```
   miner.setEtherbase(此處請填 node1 密鑰的公共地址) 
   miner.start()
  ```
  請注意在 node1 密鑰的公共地址前後要加上雙引號，並且上述動作需要在 node2 和 node3 中各運作一次
  
  node1:
   ```
      miner.setEtherbase("0xBd367d52531889EbCBA1F53B47FB75ED334262b0")
      miner.start()
   ``` 
   node2:
   ```
      miner.setEtherbase("0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27")
      miner.start()
   ``` 
   node3:
   ```
      miner.setEtherbase("0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C")
      miner.start()
   ```

# 肆. 上傳智能合約到私有以太坊的主要節點 node1

- ### 設定 Remix 網頁的 ENVIRONMENT 為本計畫的私有以太坊

1. 在 node1 的 Desktop 上開啟網頁瀏覽器(例如，Chrome)，並且前往外部的 Remix 網站 (https://remix.ethereum.org/)。

2. 點選 Remix 網頁上最右側工具列上最下方的 "Deploy & run transactions" 圖示，最右側工具列的左側的內容會從 "FILE EXPLORER" 頁次切換到 "DEPLOY & RUN TRANSACRIONS" 頁次。

3. 點選 "DEPLOY & RUN TRANSACRIONS" 頁次最上方的 "ENVIRONMENT" 下拉式選單，並在其中點選 "Custom - External Http Provider" 選項，隨即會彈出一個 "External Http Provide" 小視窗。

4. 在彈出的 "External Http Provide" 小視窗的最下方 "External HTTP Provider Endpoint" 輸入欄位中，將預設的 "http://127.0.0.1:8545" 改成 "http://127.0.0.1:5002"，也就是本計畫私有以太坊的主要節點的 http 通訊埠號 (Port)。

5. 此時 Remix 網頁上的 "Deploy & run transactions" 頁次上的 ENVIRONMENT 下拉式選單的下一個 ACCOUNT 下拉式選單將會出現 node1 的 “密鑰的公共地址”。亦即我們可以開始透過 Remix 網頁與我們的私有以太坊互動。

- ### 上傳智能合約到私有乙太坊

1. 點選 Remix 網頁上最右側工具列上最上方的 "File explorer" 圖示，最右側工具列的左側的內容會從 "DEPLOY & RUN TRANSACRIONS" 頁次切換回到 "FILE EXPLORER" 頁次

2. 以滑鼠右鍵點選 "FILE EXPLORER" 頁次上的 "contracts" ，會彈出一個快捷選單，此時再點選快捷選單上的第一個選項 "New File"，此時 "contracts" 選單隨即會展開，其中已經列有三個預設的智能合約範例，從上到下分別是 _Storage.sol、_Owner.sol、_Ballot.sol。此時緊鄰 _Ballot.sol 下方會出現一個空白的可輸入欄位，讓我們輸入要新的智能合約，此時請輸入 update.sol，並且按下鍵盤上的 "Enter" 鍵。此時在 "FILE EXPLORER" 頁次的右方區域將會出現空白的編輯區，提供我們將智能合約的內容編輯於其中。

3. 在編輯區域內輸入以下智能合約內容：  

   ```	
	// SPDX-License-Identifier: GPL-3.0

	pragma solidity >=0.4.0;

	contract upload {
		string str;

		function write (string memory _str) public {
			str = _str;
		}

		function read () public view returns (string memory) {
			return str;
		}
	}
   ```
   
4. 點選 Remix 網頁上最右側工具列上最上方的 "DEPLOY & RUN TRANSACRIONS" 圖示，最右側工具列的左側的內容會從 "FILE EXPLORER" 頁次切換回到 "DEPLOY & RUN TRANSACRIONS" 頁次。

5. 在 "DEPLOY & RUN TRANSACRIONS" 頁次上尋找並點擊 "Deploy" 按鈕，稍待片刻，即會將智能合約上傳至本計畫私有以太坊上。

6. 智能合約上傳至私有以太坊的結果可以從 Remix 網頁右側邊及區域下方的 "listen on all transactions" 頁次看到，其內容如下：  

   ```
	creation of upload pending...  
	[block:2351433 txIndex:0]from: 0x251...0F7C6to: upload.(constructor)value: 0 weidata: 0x608...20033logs: 0hash: 0xb71...dbed8  
	status			true Transaction mined and execution succeed  
	transaction 		0xd11a1226b6e0ebce9fd0f5362a324e9353136c4d3fc0e7e11f41057c0c16ce56  
	block hash		0xb718695233197766cd2746d973b3322b0e41d962cb4e55e42ae7c8f65b8dbed8  
	block number		2351433  
	contract address	0x8291f17363b14634401f4F72DA981f6e7BC0aF9a  
	from			0x251faDa5F25C6Ef2A949FA74CE28265F3090F7C6  
	to			upload.(constructor)  
	gas			410868 gas  
	transaction cost	410868 gas   
	input			0x608...20033  
	decoded input		{}  
	decoded output		-   
	logs			[]  
	val			0 wei  
   ```
   
7. 檢視上一步 "listen on all transactions" 頁次的內容，可以看到一個 "contract address" 的內容是 "0x8291f17363b14634401f4F72DA981f6e7BC0aF9a"，這個即為我們上述操作上傳到私有以太坊的智能合約的位址。

8. 記下上一步驟智能合約的位址，這個位址在後續上傳和下載資料到以太坊的程式中會需要使用。

  
# 伍. 安裝本計畫程式所需要的環境套件

接下來我們在個電腦的 Ubuntu 作業系統中，安裝為了本計畫程式所需要的環境套件。因為我們以 node1 為這個私有乙太坊的主要節點，因此以下環境套件安裝只需要在 node1 的 Ubuntu 環境中執行。

- ### 下載函數庫

請在 node1 電腦中打開一個 Ubuntu 命令視窗

1. 請在 Ubuntu 命令視窗中輸入以下 Ubuntu 指令來安裝 pip 軟體
	```
	sudo apt update
	sudo apt install python3-pip
	```

2. 請在 Ubuntu 命令視窗中輸入以下 Ubuntu 指令來安裝 sqlite3 軟體
	```
	sudo apt install sqlite3
	pip install pysqlite3-binary
	```

3. 請在 Ubuntu 命令視窗中輸入以下 Ubuntu 指令來安裝 psycopg 軟體 
	```
   第一種方法
   sudo apt-get install sqlite3 libsqlite3-dev
	sudo apt-get install python3-psycopg2 
   第二種方法
   pip install psycopg2-binary
	```

4. 請在 Ubuntu 命令視窗中輸入以下 Ubuntu 指令來安裝 requirements.txt 中所列的函式庫  
	```
	pip3 install -r requirements.txt (python_version 不用安裝)
   顧問電腦安裝版本 (python version 3.10.12) 
	```

- ### 建立 sqlite 資料庫管理系統
1. 創建一個資料庫，命名為 search，指令如下：
	```
	sqlite3 search.db
	```
2. 安裝 visual code 

   (1)下載 https://code.visualstudio.com/Download

   (2)安裝
      ```
      sudo dpkg -i 下載的安裝檔名稱
      範例:
      sudo dpkg -i code_1.50.0-1602051089_amd64.deb
      ```
   (3)開啟 VS Code
      ```
      code
      ```
   (4)執行程式碼
      ```
      python3 fileName.py
      ```

3. 在 Ubuntu 命令視窗中，透過以下指令來在 search 資料庫中建立本計畫程式所需要的基本數據，指令如下：
	```
	python3 sqlite_database.py
	```   

- ### 修改參數以連結船舶中心資料庫管理系統
因為要上傳到以太坊的資料要從船舶中心的資料庫讀取，因此要修改主目錄下的 python_function.py 檔案中的參數，以配合船舶中心的資料庫讀取。  

1. 在檔案內尋找到 extract_data_from_postgre() 函式，修改子函數的第一行程式碼，如下：
```
conn = psycopg2.connect(
      host="此處要填船舶中心的電子研究紀錄簿資料庫管理系統的 IP 位址",
      port=此處要填船舶中心的電子研究紀錄簿資料庫管理系統的埠號碼(例如，對 PostgreSQL 而言，預設是 5432),
      dbname="此處要填船舶中心的電子研究紀錄簿資料庫管理系統的資料庫名稱",
      user="此處要填可以連線進入船舶中心的資料庫管理系統讀資料的一個使用者名稱",
      password="此處要填上述使用者名稱(user)的密碼"
)
```
2. 在檔案內尋找到 write_data_to_contract() 函式，並修改其中的兩個參數

   ```
   myAccount = '此處要填 node1 的密鑰的公共地址'
   contractAddress = '此處要填智能合約的地址'
   ```
3. 在檔案內尋找到 read_data_from_contract() 函式，並修改其中的兩個參數

   ```
   contract_address = web3.to_checksum_address('此處要填智能合約的地址')
   ```

4. 修改完成上述內容後，請在 Ubuntu 命令視窗中，將目錄改變到 app.py 所在的目錄，輸入以下指令執行 flask app：
   ```
   export FLASK_APP=app.py
   ```


- ## 啟動 flask 應用軟體

1. 在 Ubuntu 命令視窗中，將目錄改變到 app.py 所在的目錄，並輸入以下指令；

   ```
   python3 app.py
   ```
2. 開啟網頁瀏覽器 (例如，Chrome)，分別開啟以下兩個網址：
   ```
   上傳電子研究記錄資料到以太坊的網頁位於：http://localhost:5000/upload
   
   從以太坊下載電子研究記錄資料的網頁位於：http://localhost:5000/transactions
   ```
# 陸. 結束應用軟體的運行

1. 停止 flask 應用軟體的運行

   在運行中的flask 應用軟體的指令列中，同時按下鍵盤的 ```ctrl``` 鍵和 ```c``` 鍵
   
2. 停止各個以太坊節點的挖礦動作:

   在三個以太坊節點還在挖礦的 Ubuntu 命令視窗上， 輸入以下指令：
   ```miner.stop()```

3. 停止 以太坊節點 的運行

   在三個運行中的以太坊節點的 Geth 指令列中，同時按下鍵盤的 ```ctrl``` 鍵和 ```d``` 鍵