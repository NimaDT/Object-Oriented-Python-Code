# Bank that manages a dictionary of Account objects

from Account import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accounts_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input('What is your account number? ')
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if account_number not in self.accounts_dict:
            raise AbortTransaction('There is no account ' + str(account_number))
        return account_number
    
    def ask_for_valid_destination_account(self):
        account_number = input('What is the number of the account? ')
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if account_number not in self.accounts_dict:
            raise AbortTransaction('There is no account ' + str(account_number))
        return account_number

    def get_users_account(self):
        account_number = self.ask_for_valid_account_number()
        o_account = self.accounts_dict[account_number]
        self.ask_for_valid_password(o_account)
        return o_account

    def ask_for_valid_password(self, o_account):
        password = input('Please enter your password: ')
        o_account.check_password_match(password)

    def create_account(self, the_name, the_starting_amount, the_password):
        o_account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = o_account
        # Increment to prepare for the next account to be created
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print('*** Open Account ***')
        user_name = input('What is the name for the new user account? ')
        user_starting_amount = input('What is the starting balance for this account? ')
        user_password = input('What is the password you want to use for this account? ')
        user_account_number = self.create_account(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number)

    def close_account(self):
        print('*** Close Account ***')
        user_account_number = self.ask_for_valid_account_number()
        o_account = self.accounts_dict[user_account_number]
        self.ask_for_valid_password(o_account)
        the_balance = o_account.get_balance()
        print('You had', the_balance, 'in your account, which is being returned to you.')
        del self.accounts_dict[user_account_number]
        print('Your account is now closed')

    def balance(self):
        print('*** Get Balance ***')
        o_account = self.get_users_account()
        the_balance = o_account.get_balance()
        print(f'Your balance is: {the_balance: ,}')

    def deposit(self):
        print('*** Deposit ***')
        o_account = self.get_users_account()
        deposit_amount = input('Please enter amount to deposit: ')
        the_balance = o_account.deposit(deposit_amount)
        print('Deposited:', deposit_amount)
        print('Your new balance is:', the_balance)

    def withdraw(self):
        print('*** Withdraw ***')
        o_account = self.get_users_account()
        user_amount = input('Please enter the amount to withdraw: ')
        the_balance = o_account.withdraw(user_amount)
        print('Withdrew:', user_amount)
        print('Your new balance is:', the_balance)

    def get_info(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accounts_dict), 'account(s) open.')
    
    def get_total_assets(self):
        print('*** Total Assets of Bank ***')
        total_assets = 0
        total_assets = int(total_assets)
        for account in self.accounts_dict:
            o_account = self.accounts_dict[account]
            #print(o_account)
            account_balance = o_account.get_balance()
            total_assets += account_balance
        print(f'     Total assets: {total_assets: ,} ')
        print('     Number of accounts:', len(self.accounts_dict))
    
    def transfer(self):
        print('*** Transfer ***')
        from_account = self.get_users_account()
        to_account =  self.accounts_dict[self.ask_for_valid_destination_account()]
        user_amount = input('Please enter amount to transfer: ')
        from_balance = from_account.withdraw(user_amount)
        to_balance = to_account.deposit(user_amount)
        print(f'Transfered {user_amount}')
        print(f'Your new balance is: {from_balance: ,} ')

    # Special method for Bank administrator only
    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for user_account_number in self.accounts_dict:
            o_account = self.accounts_dict[user_account_number]
            print('Account:', user_account_number)
            o_account.show()
            print()
