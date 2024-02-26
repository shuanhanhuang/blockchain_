#!/bin/bash
nohup geth --datadir node2 --networkid 12345 --nat extip:"10.0.129.3" --port 5022 --syncmode "full" --nodiscover --http --http.port "5003" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6003" --allow-insecure-unlock --unlock 0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27 --password node2/password.txt --verbosity 3 > node2/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://de558f69abdd15b8c082e77af7bb6a7de9109c017ea5a653f2fca8d223659f15fa56f45b86d7acafd6739ac2a516da5533fc864bdb9449cc2cd67dce7d0d7d1c@10.0.129.2:5021?discport=0')" attach node2/geth.ipc
geth --exec "admin.addPeer('enode://d00c9735a256dd651f9a56d9a2dea4ee5f13301487d1a77801677bbd8ff50fdc029a60d5068f5df99f8ae4ee50ef74c6c1ed5d349b460c7e0f01d537458b5213@10.0.129.4:5023?discport=0')" attach node2/geth.ipc

geth --exec "miner.setEtherbase('0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27')" attach node2/geth.ipc

geth --exec "clique.propose('0xBd367d52531889EbCBA1F53B47FB75ED334262b0', true)" attach node2/geth.ipc
geth --exec "clique.propose('0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27', true)" attach node2/geth.ipc
geth --exec "clique.propose('0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C', true)" attach node2/geth.ipc

sleep 30

geth --exec "miner.start()" attach node2/geth.ipc