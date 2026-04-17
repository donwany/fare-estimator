import argparse
from enum import Enum


# ✅ Step 1: Define Enum (safe status values)
class PaymentStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMPLETED = "completed"


# ✅ Step 2: Payment class
class Payment:
    def __init__(self, amount: float, status: PaymentStatus):
        self.amount = amount
        self.status = status

    def __str__(self):
        return f"Payment(amount=${self.amount}, status={self.status.value})"


# ✅ Step 3: CLI logic
def main():
    parser = argparse.ArgumentParser(prog="payment")

    subparsers = parser.add_subparsers(dest="command")

    # 👉 create command
    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--amount", type=float, required=True)
    create_parser.add_argument("--status", type=str, required=True)

    args = parser.parse_args()

    if args.command == "create":
        try:
            # Convert string → Enum
            status = PaymentStatus(args.status.lower())

            payment = Payment(args.amount, status)
            print("✅ Payment created successfully!")
            print(payment)

        except ValueError:
            print("❌ Invalid status!")
            print("Valid options:", [s.value for s in PaymentStatus])


if __name__ == "__main__":
    main()

# Example usage:
# python payment.py create --amount 100 --status pending
# uv run payment.py create --amount 100 --status pending

# Output:
# ✅ Payment created successfully!
# Payment(amount=$100.0, status=pending)