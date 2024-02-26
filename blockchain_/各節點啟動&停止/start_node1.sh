#!/bin/bash
nohup geth --datadir node1 --networkid 12345 --nat extip:"10.0.129.2" --port "5021" --syncmode "full" --cache 4096 --nodiscover --http --http.port "5002" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6002" --allow-insecure-unlock --unlock 0xBd367d52531889EbCBA1F53B47FB75ED334262b0 --password node1/password.txt --verbosity 3 > node1/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://d5a4a280cd254f16bcbc61d0556d103d76ed2a33dde4fd20d6fcb496c554970fa53e560564b435e71fc9260cb912bd78f36c56a0651e5533b06785ba41686c53@10.0.129.3:5022?discport=0')" attach node1/geth.ipc
geth --exec "admin.addPeer('enode://d00c9735a256dd651f9a56d9a2dea4ee5f13301487d1a77801677bbd8ff50fdc029a60d5068f5df99f8ae4ee50ef74c6c1ed5d349b460c7e0f01d537458b5213@10.0.129.4:5023?discport=0')" attach node1/geth.ipc

geth --exec "miner.setEtherbase('0xBd367d52531889EbCBA1F53B47FB75ED334262b0')" attach node1/geth.ipc

geth --exec "clique.propose('0xBd367d52531889EbCBA1F53B47FB75ED334262b0', true)" attach node1/geth.ipc
geth --exec "clique.propose('0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27', true)" attacSh node1/geth.ipc
geth --exec "clique.propose('0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C', true)" attach node1/geth.ipc

sleep 30

geth --exec "miner.start()" attach node1/geth.ipc
