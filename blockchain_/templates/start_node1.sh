#!/bin/bash
nohup geth --datadir node1 --networkid 12345 --nat extip:"192.72.28.44" --port "30306" --syncmode "full" --cache 4096 --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0xE94454891A9357c7F25b90825f344Fb050889f88 --password node1/password.txt --verbosity 3 > node1/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://f3aa1224e5c50ae9841bed638c943b0b7f438734cfe627a22671338768f648699e0436f2f3f31354737f460f2fa32932717763f378d88ac6eec2e18149d0eaed@192.72.28.45:30307?discport=0')" attach node1/geth.ipc
geth --exec "admin.addPeer('enode://7e9bdc91076b12ebd83c7befeba4a187a11a762bbe92372c44fb3ff4c38623bf3af48b4a339d69c76db588b2b77e806ed926eee3dfb59da9637d6dc76c01bf2c@192.72.28.46:30308?discport=0')" attach node1/geth.ipc

geth --exec "miner.setEtherbase('0xE94454891A9357c7F25b90825f344Fb050889f88')" attach node1/geth.ipc

geth --exec "clique.propose('0xE94454891A9357c7F25b90825f344Fb050889f88', true)" attach node1/geth.ipc
geth --exec "clique.propose('0xaC78b1aC91277da0533e22CA9fb8BC2eA31A5007', true)" attach node1/geth.ipc
geth --exec "clique.propose('0x50e92d58994Fe3235D4BA34D64C7BfeCa6aB0Dca', true)" attach node1/geth.ipc

sleep 30

geth --exec "miner.start()" attach node1/geth.ipc
