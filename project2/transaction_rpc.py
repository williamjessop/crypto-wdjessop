import requests

def send_transaction(addr, ammount):
    pass

def check_balance():
    # balance = somerequest
    # get the address you want to check
    print("\nYour wallet currently has a balance of: ", balance, " SAT")
    pass

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
            send_transaction(stringAddr, ammount)
            print("Transaction sent")
            # print("\nTransaction ID: ", b2lx(txid))

        else:
            print("Returning to main menu")
    
    elif(command == "check"):
        check_balance()
    
    elif(command == "quit"):
        break

    else:
        print("Please check your command and try again")


print("\nGoodbye")