def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
