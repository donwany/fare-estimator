import argparse

__version__ = "1.0.0"

def calculate_fare(distance, rate, passengers, currency, discounts):
    base_fare = distance * rate
    total_discount = sum(discounts) if discounts else 0
    final_fare = base_fare - total_discount

    print("\n--- Fare Summary ---")
    print(f"Distance: {distance} miles")
    print(f"Rate: {rate} per mile")
    print(f"Passengers: {passengers}")
    print(f"Currency: {currency}")
    print(f"Base Fare: {base_fare:.2f}")
    print(f"Discounts Applied: {total_discount:.2f}")
    print(f"Final Fare: {final_fare:.2f} {currency}")
    print("---------------------\n")


def main():
    parser = argparse.ArgumentParser(
        prog="fare-calculator",  # program name shown in help
        usage="%(prog)s --distance DIST [options]",  # custom usage message
        description="🚗 Ride Fare Calculator CLI - Estimate trip costs easily",
        epilog="Example: python fare_v2.py --distance 10 --rate 2.5 --currency USD",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # auto shows defaults
        prefix_chars="-",  # allows - or -- (default)
        add_help=True,  # automatically adds -h/--help
        allow_abbrev=True  # allows shortened flags like --dis for --distance
    )

    # Version flag
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"FareEstimator CLI {__version__}"
    )

    # Required argument
    parser.add_argument(
        "--distance",
        type=float,
        required=True,
        help="Distance of the trip in miles"
    )

    # Optional with default
    parser.add_argument(
        "--rate",
        type=float,
        default=2.0,
        help="Rate per mile (default: 2.0)"
    )

    # Optional with choices
    parser.add_argument(
        "--currency",
        choices=["USD", "GHS", "EUR"],
        default="USD",
        type=str,
        help="Currency type"
    )

    # Optional with default
    parser.add_argument(
        "--passengers",
        type=int,
        default=1,
        help="Number of passengers (default: 1)"
    )

    # Multiple values using nargs
    parser.add_argument(
        "--discounts",
        type=float,
        nargs="*",
        help="List of discount amounts (e.g. --discounts 2 1.5 0.5)"
    )

    args = parser.parse_args()

    calculate_fare(
        args.distance,
        args.rate,
        args.passengers,
        args.currency,
        args.discounts
    )


if __name__ == "__main__":
    main()
