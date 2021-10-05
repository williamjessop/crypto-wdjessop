#!/usr/bin/env python

# Write a python bitcoin script that interacts with 
# bitcoin on the testnet using bitcoind and python-bitcoinlib.  
# Upload a link to your repository named 
# crypto-<cmu-user-name> (for example, crypto-wmacevoy for me). 
# Or upload the files directly here.  
# Include screen shots of it working 
# and an explanation of what it does.  
# It should interact in some way with transaction of your own.

# My example repo is

# https://github.com/wmacevoy/crypto-wmacevoy


import bitcoin
bitcoin.SelectParams("testnet")

import bitcoin.rpc

conf_path = "/home/wjessop/.bitcoin/bitcoin.conf"

proxy = bitcoin.rpc.RawProxy(btc_conf_file=conf_path)

info = proxy.getwalletinfo()

print("Wallet has a balance of: ", info['balance'])
