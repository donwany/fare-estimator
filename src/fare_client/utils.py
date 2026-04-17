import argparse
from estimator import FareEstimator
from datetime import datetime

__version__ = "0.1.0"

estimator = FareEstimator()


def parsers():
    parser = argparse.ArgumentParser(
        prog="FareClient",  # program name shown in help
        usage="%(prog)s --distance DIST [options]",  # custom usage message
        description="🚗 Ride Fare Calculator CLI - Estimate trip costs easily",
        epilog="Example: fare-client --distance 10 --rate 2.5 ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # auto shows defaults
        prefix_chars="-",  # allows - or -- (default)
        add_help=True,  # automatically adds -h/--help
        allow_abbrev=True  # allows shortened flags like --dist for --distance
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    # estimate command
    estimate_parser = subparsers.add_parser("estimate", help="Estimate the ride fare")
    estimate_parser.add_argument("--distance", "-d", type=float, default=1.0, help="Distance of the ride in miles")
    estimate_parser.add_argument("--rate", "-r", type=float, default=2.5, help="Fare rate per mile")
    # book command
    book_parser = subparsers.add_parser("book", help="Book a ride")
    book_parser.add_argument("--distance", type=float, help="Distance of the ride in miles")
    book_parser.add_argument("--pickup", type=str, required=True, help="Pickup location")
    book_parser.add_argument("--dropoff", type=str, required=True, help="Dropoff location")
    book_parser.add_argument("--rate", type=float, default=2.5, help="Fare rate per mile")
    # login command
    login_parser = subparsers.add_parser("login", help="login to application")
    login_parser.add_argument("--username", "-u", type=str, required=True, help="Enter your username")
    login_parser.add_argument("--password", "-p", type=str, required=True, help="Enter your password")

    doctor_parser = subparsers.add_parser("doctor", help="ask a doctor a question")
    doctor_parser.add_argument("--question", type=str, required=True, help="ask a question")

    # parser.add_argument("--distance", "-d", type=float, default=1.0, help="Distance of the ride in miles")
    # parser.add_argument("--rate", "-r", type=float, default=2.5, help="Fare rate per mile")
    parser.add_argument("--currency", "-c", type=str, default="USD", choices=["USD", "EUR", "GHS"],
                        help="Currency for the fare (e.g., USD, EUR)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--version", "-v", action="version", version=f"fare client CLI: {__version__}")

    args = parser.parse_args()

    return args


def book_ride(args):
    print("Booking a ride ...")
    ride = {
        "id": f"RIDE-{datetime.now().timestamp()}",
        "distance": args.distance,
        "rate": args.rate,
        "pickup": args.pickup,
        "dropoff": args.dropoff,
        "status": "confirmed",
        "timestamp": datetime.now().isoformat(),
    }
    return ride


def estimate_ride(args):
    print(f"estimating ride fare ...")
    calculated_fare = estimator.estimate(distance=args.distance, rate=args.rate)
    print(f"The calculated fare for the ride is: ${calculated_fare:.2f}")


def ask_doctor_question(args):
    print(f"asking doctor question: {args.question}")
