#!/bin/bash
nohup geth --datadir node3 --networkid 12345 --nat extip:"192.72.28.46" --port "30308" --syncmode "full" --nodiscover --http --http.port "5004" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6004" --allow-insecure-unlock --unlock 0x50e92d58994Fe3235D4BA34D64C7BfeCa6aB0Dca --password node3/password.txt --verbosity 3 > node3/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://db25d9b2d94531e9fba8ab6865bbf390f5360a36a2f82634375969dd420174d0b308b9070b6feb39a4ffd94cbcab32faa1d5532095a2d855004e6e82d1b86705@192.72.28.44:30306?discport=0')" attach node3/geth.ipc
geth --exec "admin.addPeer('enode://f3aa1224e5c50ae9841bed638c943b0b7f438734cfe627a22671338768f648699e0436f2f3f31354737f460f2fa32932717763f378d88ac6eec2e18149d0eaed@192.72.28.45:30307?discport=0')" attach node3/geth.ipc

geth --exec "miner.setEtherbase('0x50e92d58994Fe3235D4BA34D64C7BfeCa6aB0Dca')" attach node3/geth.ipc

geth --exec "clique.propose('0xE94454891A9357c7F25b90825f344Fb050889f88', true)" attach node3/geth.ipc
geth --exec "clique.propose('0xaC78b1aC91277da0533e22CA9fb8BC2eA31A5007', true)" attach node3/geth.ipc
geth --exec "clique.propose('0x50e92d58994Fe3235D4BA34D64C7BfeCa6aB0Dca', true)" attach node3/geth.ipc

sleep 30

geth --exec "miner.start()" attach node3/geth.ipc