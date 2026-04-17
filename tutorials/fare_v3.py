import argparse
import json
import os
import sys
from datetime import datetime
import getpass

__version__ = "1.0.0"

class FareCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="fare",
            usage="fare <command> [options]",
            description="🚗 Fare CLI - Ride estimation and booking tool",
            epilog="Example: fare estimate --distance 10 --rate 2.5",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )

        # Global options
        self.parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
        self.parser.add_argument("--json", action="store_true", help="Output results in JSON format")
        # Version flag
        self.parser.add_argument(
            "--version",
            "-v",
            action="version",
            version=f"FareEstimator CLI {__version__}"
        )

        subparsers = self.parser.add_subparsers(dest="command", required=True)

        # ---- estimate command ----
        estimate_parser = subparsers.add_parser("estimate", help="Estimate ride fare")

        required = estimate_parser.add_argument_group("Required Arguments")
        required.add_argument("--distance", type=float, required=True)

        optional = estimate_parser.add_argument_group("Optional Arguments")
        optional.add_argument("--rate", type=float, default=self.get_env("RATE", 2.0))
        optional.add_argument("--currency", choices=["USD", "EUR", "GHS"], default="USD")
        optional.add_argument("--passengers", type=int, default=1)
        optional.add_argument("--discounts", type=float, nargs="*")

        # ---- book command ----
        book_parser = subparsers.add_parser("book", help="Book a ride")
        book_parser.add_argument("--distance", type=float, required=True)
        book_parser.add_argument("--pickup", required=True)
        book_parser.add_argument("--dropoff", required=True)

        # ---- history command ----
        subparsers.add_parser("history", help="View ride history")

        # --- login command ---
        login_parser = subparsers.add_parser("login", help="Log in to your account")
        login_parser.add_argument("--username", type=str, required=True, help="Your username")
        login_parser.add_argument("--password", type=str, help="Your password (optional, will prompt if not provided)")

        self.token = None  # store authentication token

    # ---- login method ----
    def login(self, args):
        password = args.password
        if not password:
            password = getpass.getpass("Password: ")

        # Mock authentication logic
        if args.username == "testuser" and password == "secret123":
            self.token = "mock_token_abc123"
            result = {"status": "success", "message": f"Logged in as {args.username}", "token": self.token}
        else:
            result = {"status": "failed", "message": "Invalid username or password"}

        self.output(result, args)

    def get_env(self, key, default):
        return type(default)(os.getenv(key, default))

    def log(self, message, verbose):
        if verbose:
            print(f"[DEBUG] {message}")

    def estimate(self, args):
        self.log("Calculating fare...", args.verbose)

        rate = args.rate
        distance = args.distance
        discounts = sum(args.discounts) if args.discounts else 0

        base = distance * rate
        final = base - discounts

        result = {
            "distance": distance,
            "rate": rate,
            "base_fare": round(base, 2),
            "discounts": discounts,
            "final_fare": round(final, 2),
            "currency": args.currency,
        }

        self.output(result, args)

    def book(self, args):
        self.log("Booking ride...", args.verbose)

        ride = {
            "id": f"RIDE-{datetime.now().timestamp()}",
            "distance": args.distance,
            "pickup": args.pickup,
            "dropoff": args.dropoff,
            "status": "confirmed",
            "timestamp": datetime.now().isoformat(),
        }

        self.output(ride, args)

    def history(self, args):
        self.log("Fetching history...", args.verbose)

        # Mock data
        rides = [
            {"id": "RIDE-1", "distance": 5, "status": "completed"},
            {"id": "RIDE-2", "distance": 12, "status": "completed"},
        ]

        self.output(rides, args)

    def output(self, data, args):
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            print("\n=== RESULT ===")
            print(data)
            print("==============\n")

    def run(self):
        args = self.parser.parse_args()
        if args.command == "login":
            self.login(args)
        elif args.command == "estimate":
            self.estimate(args)
        elif args.command == "book":
            self.book(args)
        elif args.command == "history":
            self.history(args)
        else:
            self.parser.print_help()
            sys.exit(1)


if __name__ == "__main__":
    FareCLI().run()
