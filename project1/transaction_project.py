#!/usr/bin/env python

# William Jessop
# 9-10-2021

# Assignment Description

# Write a python bitcoin script that interacts with 
# bitcoin on the testnet using bitcoind and python-bitcoinlib.  

# Include screen shots of it working and an explanation of what it does.  

# It should interact in some way with transaction of your own.


import bitcoin
import bitcoin.rpc
import bitcoin.wallet
from bitcoin.wallet import CBitcoinAddress
from bitcoin.core import COIN, b2lx

bitcoin.SelectParams("testnet")

conf_path = "/home/wjessop/.bitcoin/bitcoin.conf"
proxy = bitcoin.rpc.Proxy(btc_conf_file=conf_path)

command = ""
while True:
    print("\nWhat would you like to do?\n")
    print("[send] a transaction")
    print("[check] balance")
    print("[quit]\n")

    command = input()

    if(command == "send"):
        print("\nPlease enter the address you would like to send to: ")
        stringAddr = input()

        print("\nPlease enter the ammount in BTC you would like to send: ")
        ammount = input()

        print("\nPlease verify the transaction details:")
        print("Address to send to: ", stringAddr)
        print("Ammout to send: ", str(ammount))
        print("\nType [confirm] to send the transaction\n")

        command = input()
        if(command == "confirm"):
            print("\nSending transaction...")
            addr = CBitcoinAddress(stringAddr)
            txid = proxy.sendtoaddress(addr, float(ammount) * COIN)
            print("Transaction sent")
            print("\nTransaction ID: ", b2lx(txid))

        else:
            print("Returning to main menu")
    
    elif(command == "check"):
        print("\nYour wallet currently has a balance of: ", proxy.getbalance(), " SAT")
    
    elif(command == "quit"):
        break

    else:
        print("Please check your command and try again")


print("\nGoodbye")
