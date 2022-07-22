from Transaction import Transaction 

if __name__ == "__main__":
    transaction = Transaction(sender_pubkey="sender", 
                              receiver_pubkey="receiver", 
                              amount="1", 
                              type="TRANSFER")
    print(transaction.to_json())