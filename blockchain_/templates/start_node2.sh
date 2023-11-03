#!/bin/bash
nohup geth --datadir node2 --networkid 12345 --nat extip:"192.72.28.45" --port "30307" --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0xaC78b1aC91277da0533e22CA9fb8BC2eA31A5007 --password node2/password.txt --verbosity 3 > node2/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://db25d9b2d94531e9fba8ab6865bbf390f5360a36a2f82634375969dd420174d0b308b9070b6feb39a4ffd94cbcab32faa1d5532095a2d855004e6e82d1b86705@192.72.28.44:30306?discport=0')" attach node2/geth.ipc
geth --exec "admin.addPeer('enode://7e9bdc91076b12ebd83c7befeba4a187a11a762bbe92372c44fb3ff4c38623bf3af48b4a339d69c76db588b2b77e806ed926eee3dfb59da9637d6dc76c01bf2c@192.72.28.46:30308?discport=0')" attach node2/geth.ipc

geth --exec "miner.setEtherbase('0xaC78b1aC91277da0533e22CA9fb8BC2eA31A5007')" attach node2/geth.ipc

geth --exec "clique.propose('0xE94454891A9357c7F25b90825f344Fb050889f88', true)" attach node2/geth.ipc
geth --exec "clique.propose('0xaC78b1aC91277da0533e22CA9fb8BC2eA31A5007', true)" attach node2/geth.ipc
geth --exec "clique.propose('0x50e92d58994Fe3235D4BA34D64C7BfeCa6aB0Dca', true)" attach node2/geth.ipc

sleep 30

geth --exec "miner.start()" attach node2/geth.ipc