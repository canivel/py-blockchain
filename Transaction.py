import time
import uuid

class Transaction():
    def __init__(self, sender_pubkey, receiver_pubkey, amount, type):
        self.sender_pubkey = sender_pubkey
        self.receiver_pubkey = receiver_pubkey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ""
    
    def to_json(self):
        return self.__dict__