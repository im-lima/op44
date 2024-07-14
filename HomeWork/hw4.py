class Asset:
    pass

class InsurableItem:
    pass

class InterestBearingItem:
    pass

class RealEstate(Asset, InsurableItem):
    pass

class Security(Asset, InterestBearingItem):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass

class BankAccount(Asset, InsurableItem, InterestBearingItem):
    pass

class SavingsAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass