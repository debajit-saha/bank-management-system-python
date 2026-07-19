from dataclasses import dataclass


@dataclass
class Account:
    account_id: int
    account_number: str
    customer_id: int
    balance: float