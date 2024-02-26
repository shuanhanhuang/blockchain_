#!/bin/bash
nohup geth --datadir node3 --networkid 12345 --nat extip:"10.0.129.4" --port 5023 --syncmode "full" --nodiscover --http --http.port "5004" --http.addr "0.0.0.0" --http.corsdomain "*" --http.api "personal,eth,net,web3,txpool,miner" --authrpc.addr "0.0.0.0" --authrpc.port "6004" --allow-insecure-unlock --unlock 0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C --password node3/password.txt --verbosity 3 > node3/geth.log 2>&1 &

sleep 60

geth --exec "admin.addPeer('enode://de558f69abdd15b8c082e77af7bb6a7de9109c017ea5a653f2fca8d223659f15fa56f45b86d7acafd6739ac2a516da5533fc864bdb9449cc2cd67dce7d0d7d1c@10.0.129.2:5021?discport=0')" attach node3/geth.ipc
geth --exec "admin.addPeer('enode://d5a4a280cd254f16bcbc61d0556d103d76ed2a33dde4fd20d6fcb496c554970fa53e560564b435e71fc9260cb912bd78f36c56a0651e5533b06785ba41686c53@10.0.129.3:5022?discport=0')" attach node3/geth.ipc

geth --exec "miner.setEtherbase('0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C')" attach node3/geth.ipc

geth --exec "clique.propose('0xBd367d52531889EbCBA1F53B47FB75ED334262b0', true)" attach node3/geth.ipc
geth --exec "clique.propose('0x0C6c3863aF1DA72eD715ca9f0832D936D8A3Fc27', true)" attach node3/geth.ipc
geth --exec "clique.propose('0x3c5C5b13f82e04Bf952E399b196a6AAE08b2f07C', true)" attach node3/geth.ipc

sleep 30

geth --exec "miner.start()" attach node3/geth.ipc