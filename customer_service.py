from database import Database
from customer import Customer


class CustomerService:
    @staticmethod
    def create_customer() -> None:
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        customers = Database.get_all_customers()

        customer = Customer(
            customer_id=max((
                customer.customer_id for customer in customers), default=0) + 1,
            name=name,
            phone=phone
        )

        Database.insert_customer(customer)

    @staticmethod
    def get_customer_by_id() -> None:
        try:
            customer_id = int(input("Enter customer id: "))

        except ValueError:
            print("Please enter a valid number.")
            return

        customer = Database.get_customer_by_id(customer_id)

        if customer:
            CustomerService._display_customer(customer)
        else:
            print("Customer not found.")

    @staticmethod
    def get_all_customers() -> None:
        customers = Database.get_all_customers()

        if not customers:
            print("No customers found.")
            return

        for customer in customers:
            CustomerService._display_customer(customer)

    @staticmethod
    def _display_customer(customer: Customer) -> None:
        print("Customer Details: ")
        print(
            f"Id: {customer.customer_id}, "
            f"Name: {customer.name}, "
            f"Phone: {customer.phone}"
        )
