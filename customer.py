from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: int
    name: str
    phone: str