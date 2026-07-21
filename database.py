import sqlite3
from customer import Customer
from account import Account
from decorators import log_query

DB_NAME = "bank.db"


class Database:

    @staticmethod
    def get_connection():
        connection = sqlite3.connect(DB_NAME)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    @staticmethod
    @log_query()
    def create_tables():
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS customers(
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL
                    )
                """)

                cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS accounts(
                        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account_number TEXT UNIQUE NOT NULL,
                        customer_id INTEGER NOT NULL,
                        balance REAL NOT NULL,
                        FOREIGN KEY(customer_id)
                            REFERENCES customers(customer_id)
                    )
                """)

                connection.commit()
                print("Database tables created successfully.")

        except sqlite3.Error as ex:
            print(f"Database Error: {ex}")

    @staticmethod
    @log_query()
    def insert_customer(customer: Customer):
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO customers(customer_id, name, phone)
                    VALUES (?, ?, ?)
                """, (customer.customer_id, customer.name, customer.phone))

                connection.commit()
                print("Customer inserted successfully.")

        except sqlite3.Error as ex:
            print(f"Database Error: {ex}")

    @staticmethod
    @log_query(log_args=True, log_result=True)
    def get_all_customers():
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM customers")

                rows = cursor.fetchall()

                customers = [
                    Customer(
                        customer_id=row[0],
                        name=row[1],
                        phone=row[2]
                    )
                    for row in rows
                ]

            return customers

        except sqlite3.Error as ex:
            print(f"Database Error: {ex}")
            return []

    @staticmethod
    @log_query()
    def get_customer_by_id(customer_id):
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    SELECT *
                    FROM customers
                    WHERE customer_id = ?
                """, (customer_id,))

                row = cursor.fetchone()

                if row is None:
                    return None

                customer = Customer(
                    customer_id=row[0],
                    name=row[1],
                    phone=row[2]
                )

                return customer

        except sqlite3.Error as ex:
            print(f"Database Error: {ex}")

    @staticmethod
    @log_query()
    def insert_account(account: Account) -> None:
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO accounts
                    (account_id, account_number, customer_id, balance)
                    VALUES (?, ?, ?, ?)
                """, (
                    account.account_id,
                    account.account_number,
                    account.customer_id,
                    account.balance
                ))

                connection.commit()

        except sqlite3.Error as ex:
            print(ex)

    @staticmethod
    @log_query()
    def get_account_by_number(account_number: str) -> Account | None:
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    SELECT *
                    FROM accounts
                    WHERE account_number = ?
                """, (account_number,))

                row = cursor.fetchone()

                if row is None:
                    return None

                return Account(
                    account_id=row[0],
                    account_number=row[1],
                    customer_id=row[2],
                    balance=row[3]
                )

        except sqlite3.Error as ex:
            print(ex)
            return None

    @staticmethod
    @log_query()
    def get_all_accounts() -> list[Account]:
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM accounts")

                rows = cursor.fetchall()

                return [
                    Account(
                        account_id=row[0],
                        account_number=row[1],
                        customer_id=row[2],
                        balance=row[3]
                    )
                    for row in rows
                ]

        except sqlite3.Error as ex:
            print(ex)
            return []

    @staticmethod
    @log_query()
    def update_balance(account_number: str, balance: float) -> None:
        try:
            with Database.get_connection() as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    UPDATE accounts
                    SET balance = ?
                    WHERE account_number = ?
                """, (
                    balance,
                    account_number
                ))

                connection.commit()

        except sqlite3.Error as ex:
            print(ex)
