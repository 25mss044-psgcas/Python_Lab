class InsufficientBalanceError(Exception):
    def __init__(self, message="Withdrawal amount exceeds available balance."):
        self.message = message
        super().__init__(self.message)


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            f"Requested ₹{amount}, but available balance is only ₹{balance}."
        )
    return balance - amount


current_balance = 5000

try:
    amt = float(input(f"Current Balance: ₹{current_balance}. Enter amount to withdraw: "))
    current_balance = withdraw(current_balance, amt)
    print(f"Withdrawal successful! Remaining Balance: ₹{current_balance}")

except InsufficientBalanceError as e:
    print(f"Transaction Failed: {e}")