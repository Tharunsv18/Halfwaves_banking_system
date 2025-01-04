import hashlib
import os
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class BankingSystem:
    ACCOUNTS_FILE = 'accounts.txt'
    TRANSACTIONS_FILE = 'transactions.txt'

    def __init__(self):
        self.current_user = None

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self):
        name = input(Fore.CYAN + "Enter your name: ")
        initial_deposit = float(input(Fore.CYAN + "Enter your initial deposit: "))
        password = input(Fore.CYAN + "Enter a password: ")
        account_number = self.generate_account_number()
        hashed_password = self.hash_password(password)

        with open(self.ACCOUNTS_FILE, 'a') as f:
            f.write(f"{account_number},{name},{hashed_password},{initial_deposit}\n")

        print(Fore.GREEN + f"Account created successfully! Your account number is {account_number}. Save this for login.")

    def generate_account_number(self):
        return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

    def login(self):
        account_number = input(Fore.CYAN + "Enter your account number: ")
        password = input(Fore.CYAN + "Enter your password: ")
        hashed_password = self.hash_password(password)

        with open(self.ACCOUNTS_FILE, 'r') as f:
            for line in f:
                acc_no, name, stored_password, balance = line.strip().split(',')
                if acc_no == account_number and stored_password == hashed_password:
                    self.current_user = {
                        'account_number': acc_no,
                        'name': name,
                        'balance': float(balance)
                    }
                    print(Fore.GREEN + "Login successful!")
                    return

        print(Fore.RED + "Invalid account number or password.")

    def perform_transaction(self, transaction_type):
        if not self.current_user:
            print(Fore.RED + "You must be logged in to perform transactions.")
            return

        amount = float(input(Fore.CYAN + f"Enter amount to {transaction_type.lower()}: "))
        if transaction_type == 'Deposit':
            self.current_user['balance'] += amount
        elif transaction_type == 'Withdrawal':
            if self.current_user['balance'] < amount:
                print(Fore.RED + "Insufficient balance.")
                return
            self.current_user['balance'] -= amount

        self.update_account_balance()
        self.log_transaction(transaction_type, amount)
        print(Fore.GREEN + f"{transaction_type} successful! Current balance: {self.current_user['balance']}")

    def update_account_balance(self):
        lines = []
        with open(self.ACCOUNTS_FILE, 'r') as f:
            lines = f.readlines()

        with open(self.ACCOUNTS_FILE, 'w') as f:
            for line in lines:
                acc_no, name, password, balance = line.strip().split(',')
                if acc_no == self.current_user['account_number']:
                    f.write(f"{acc_no},{name},{password},{self.current_user['balance']}\n")
                else:
                    f.write(line)

    def log_transaction(self, transaction_type, amount):
        with open(self.TRANSACTIONS_FILE, 'a') as f:
            f.write(f"{self.current_user['account_number']},{transaction_type},{amount},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    def main_menu(self):
        while True:
            print(Fore.YELLOW + "\nWelcome to the Banking System!")
            print(Fore.YELLOW + "1. Create Account")
            print(Fore.YELLOW + "2. Login")
            print(Fore.YELLOW + "3. Deposit")
            print(Fore.YELLOW + "4. Withdraw")
            print(Fore.YELLOW + "5. Exit")
            choice = input(Fore.CYAN + "Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.perform_transaction('Deposit')
            elif choice == '4':
                self.perform_transaction('Withdrawal')
            elif choice == '5':
                print(Fore.MAGENTA + "Thank you for using the Banking System. Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == '__main__':
    BankingSystem().main_menu()
