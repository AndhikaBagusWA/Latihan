class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def CekPinAwal(self):
        return self.defaultPin
    
    def CekSaldoAwal(self):
        return self.defaultBalance