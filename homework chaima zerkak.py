# CLASS CLIENT (represents a bank client)
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin           
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []       

    # Getters
    def get_CIN(self):
        return self.__CIN
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_tel(self):
        return self.__tel

    # Setter
    def set_tel(self, tel):
        self.__tel = tel

    # Add account
    def add_account(self, account):
        self.__accounts.append(account)

    # List all accounts
    def listAccounts(self):
        print("Accounts of", self.firstName, self.lastName)
        if len(self.__accounts) == 0:
            print("This client has no accounts.")
        else:
            for acc in self.__accounts:
                print(" Account code:", acc.get_code(), ", Balance:", acc.get_balance(), "DA")

    # Show client info
    def display(self):
        print(f"CIN: {self.CIN} , Name: {self.firstName}, {self.lastName}, Tel: {self.tel}") 


# CLASS ACCOUNT (represents bank account)
class Account:
    nbAccounts = 0   # counts total accounts

    def init(self, owner):
        Account.nbAccounts += 1
        self.__code = Account.nbAccounts
        self.__balance = 0
        self.__owner = owner
        self.__transactions = []
        owner.add_account(self)

    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner

    # Add a transaction
    def add_transaction(self, text):
        self.__transactions.append(text)

    # Show transactions
    def displayTransactions(self):
        print("Transaction history for account", self.__code)
        if len(self.__transactions) == 0:
            print("No transactions yet.")
        else:
            for t in self.__transactions:
                print(" ", t)

    # Credit money
    def credit(self, amount, from_account=None):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.__balance += amount
        if from_account:
            self.add_transaction(f"Received {amount} DA from account {from_account.get_code()}") 
        else:
            self.add_transaction(f"Credited +{amount} DA")

    # Debit money
    def debit(self, amount, to_account=None):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance!")
            return
        self.__balance -= amount
        if to_account:
            self.add_transaction(f"Sent {amount} DA to account {to_account.get_code()}")
        else:
            self.add_transaction(f"Debited -{amount} DA")

    # Transfer money
    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance for transfer!")
            return
        self.debit(amount, target_account)
        target_account.credit(amount, self)

    # Show account info
    def display(self):
        print("Account Code:", self.__code)
        owner = self.__owner
        print("Owner:", owner.get_firstName(), owner.get_lastName())
        print("Balance:", self.__balance, "DA")

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)