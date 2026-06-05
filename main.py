class BankAccount:
    
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.current_balance = initial_balance
    
    def display(self):
        print(self.name)
        print(self.account_number)
        print(self.current_balance)

acc = []

while True:
    user = input("User: ")
    
    if user == "Create Account":
        accown_name = input("Name: ")
        acc_num = int(input("Account Number: "))
        acc_ini_bal = int(input("Initial Balance: "))
        account = BankAccount(accown_name, acc_num, acc_ini_bal)
        acc.append(account)

    if user == "View Accounts":
        for account in acc:
            account.display()

    if user == "Deposit Money":
        acco_num = int(input("Account Number: "))
        amount = int(input("Amount: "))
        found = False
        for account in acc:
            if acco_num == account.account_number:
                account.current_balance += amount
                account.display()
                found = True
        if not found:
            print("Account not found")

    if user == "Withdraw Money":
        acco_num = int(input("Account Number: "))
        amount = int(input("Amount: "))
        found = False
        for account in acc:
            if acco_num == account.account_number:
                if account.current_balance >= amount:
                    account.current_balance -= amount
                    found = True
                else:
                    print("Insufficient Balance")
            
        if not found:
            print("Account not found")

    if user == "Check Balance":
        acco_num = int(input("Account Number: "))
        found = False
        for account in acc:
            if acco_num == account.account_number:
                print(account.current_balance)
                found = True
        if not found:
            print("Account not found")
        
    if user == "Find Richest Account":
        if acc:
            richest = acc[0]
            for current_acc in acc:
                if current_acc.current_balance >= richest.current_balance:
                    richest = current_acc
            richest.display() 
        else:
            print("No Account Found")


    if user == "Exit":
        break
