from menu import show_menu
from customer_service import CustomerService
from account_service import AccountService
from database import Database


def main():
    Database.create_tables()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if (choice == "1"):
            CustomerService.create_customer()

        elif (choice == "2"):
            CustomerService.get_customer_by_id()

        elif (choice == "3"):
            CustomerService.get_all_customers()

        elif (choice == "4"):
            AccountService.create_account()

        elif (choice == "5"):
            AccountService.deposit()

        elif (choice == "6"):
            AccountService.withdraw()

        elif (choice == "8"):
            print("Thank you")
            break
        else:
            print(f"You have selected option {choice}")


if __name__ == "__main__":
    main()
