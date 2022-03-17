from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.pin = custPin
        self.balance = custBalance
    
    def checkId(self):
        return self.id
    
    def checkPin(self):
        return self.custPin
    
    def checkBalance(self):
        return self.custBalance
    
    def withdrawlBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal