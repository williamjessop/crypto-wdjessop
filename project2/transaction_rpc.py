import requests
from dotenv import load_dotenv
import os
import json

# Example transaction address to find:
# 2200d4d74606eca205797ea8ee4414af54ee45d5d04b63d29cd5fab8ec133b7c

# Testnet Faucet Address:
# tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt

# Setting up variables needed for any request & secret variables
env_path = './.env'
load_dotenv(dotenv_path=env_path)

RPC_USER = os.getenv("RPC_USER")
RPC_PASS = os.getenv("PASSWORD")
auth = (RPC_USER, RPC_PASS)

url = "http://127.0.0.1:18332"

def get_transaction(addr):
    body = {
        "method": "gettransaction",
        "params": [addr]
    }

    headers = {
        "content-type": "application/json"
    }

    res = requests.post(url=url, json=body, auth=auth, headers=headers)

    print("The following is the transaction you requested: ")
    print(json.loads(res.content))

def send_transaction(addr, ammt):
    body = {
        "method": "sendtoaddress",
        "params": [addr, float(ammt)]
    }

    headers = {
        "content-type": "application/json"
    }

    res = requests.post(url=url, json=body, auth=auth, headers=headers)

    print("The following is the result of your transaction: ")
    print(json.loads(res.content))

def check_balance():
    body = {
        "method": "getbalance"
    }

    headers = {
        "content-type": "application/json"
    }

    res = requests.post(url=url, json=body, auth=auth, headers=headers)

    print("The following is your wallet balance: ")
    print(json.loads(res.content))
    
command = ""
while True:
    print("\nWhat would you like to do?\n")
    print("[send] a transaction")
    print("[get] a transaction")
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
            try:
                send_transaction(stringAddr, ammount)
                print("Transaction sent")
            except:
                print("There was a problem sending your transaction")

        else:
            print("Returning to main menu")
    
    elif(command == "check"):
        try:
            check_balance()
        except:
            print("There was a problem checking your balance")

    elif(command == "get"):
        print("\nPlease enter the address of the transaction you want to get: ")
        stringAddr = input()

        try:
            get_transaction(stringAddr)
        except:
            print("There was a problem getting the transaction")
    
    elif(command == "quit"):
        break

    else:
        print("Please check your command and try again")

print("\nGoodbye")