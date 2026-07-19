from account import Account
from database import Database


class AccountService:

    @staticmethod
    def create_account() -> None:
        try:
            customer_id = int(input("Enter customer id: "))
        except ValueError:
            print("Please enter a valid customer id.")
            return

        customer = Database.get_customer_by_id(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        accounts = Database.get_all_accounts()

        next_account_id = max(
            (account.account_id for account in accounts),
            default=0
        ) + 1

        next_account_number = str(1000000000 + next_account_id)

        account = Account(
            account_id=next_account_id,
            account_number=next_account_number,
            customer_id=customer_id,
            balance=0.0
        )

        Database.insert_account(account)

        print(f"Account created successfully.")
        print(f"Account Number: {account.account_number}")

    @staticmethod
    def deposit() -> None:
        try:
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter valid input.")
            return

        account = Database.get_account_by_number(account_number)

        if account is None:
            print("Account not found.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        account.balance += amount

        Database.update_balance(
            account.account_number,
            account.balance
        )

        print(f"Deposit successful.")
        print(f"Current Balance: ₹{account.balance:.2f}")

    @staticmethod
    def withdraw() -> None:
        try:
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter valid input.")
            return

        account = Database.get_account_by_number(account_number)

        if account is None:
            print("Account not found.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > account.balance:
            print("Insufficient balance.")
            return

        account.balance -= amount

        Database.update_balance(
            account.account_number,
            account.balance
        )

        print(f"Withdrawal successful.")
        print(f"Current Balance: ₹{account.balance:.2f}")
