class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):#function for deposition
        if amount > 0: #amount is more than 0 
            self.balance += amount#add the amount to the balance 
            print(f"Amount ${amount} deposited successfully.")#successfull statement
        else:
            print("Deposit amount should be positive.")#not successfull statement

    def withdraw(self, amount):#function for withdraw
        if amount > self.balance:#if  withdrawing amount is more than the balance then
            print("Insufficient balance.")#print this statement
        elif amount <= 0:#if withdrawing amount is less than 0 then  
            print("Withdrawal amount should be positive.")#print this statement
        else:
            self.balance -= amount#if thw withdrawing amount is sufficient then the amount will be withdrawn from the balance
            print(f"Amount ${amount} withdrawn successfully.")#print this statement

    def check_balance(self):#checking balance 
        print(f"Account Balance: ${self.balance}")#printing the balance amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):#funtion for creating a account
        if account_number in self.accounts:#if the account is in self accounts
            print("Account already exists.")#print this statement
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)#account is not present
            print(f"Account created for {account_holder} with Account Number: {account_number}")#print this statement

    def get_account(self, account_number):#function  for getting the account 
        if account_number in self.accounts:#
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None


# Main Program
bank = Bank()

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))#choice option

    if choice == 1:#if entering choice is 1
        acc_num = input("Enter Account Number: ")#entering the account number
        acc_holder = input("Enter Account Holder Name: ")#entering the account holder name
        bank.create_account(acc_num, acc_holder)#printing the account number and name

    elif choice == 2:#if enetring option is 2
        acc_num = input("Enter Account Number: ")#entering account number
        account = bank.get_account(acc_num)#if a
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

    elif choice == 3:
        acc_num = input("Enter Account Number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

    elif choice == 4:
        acc_num = input("Enter Account Number: ")
        account = bank.get_account(acc_num)
        if account:
            account.check_balance()

    elif choice == 5:
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")