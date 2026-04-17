import argparse

__version__ = "0.1.0"


def calculate_fare(distance, rate):
    fare = distance * rate
    return fare


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ride Fare Calculator")
    parser.add_argument("--distance", "-d", type=float, default=1.0, help="Distance of the ride in miles")
    parser.add_argument("--rate", "-r", type=float, default=2.5, help="Fare rate per mile")
    parser.add_argument("--currency", "-c", type=str, default="USD", choices=["USD", "EUR", "GHS"],
                        help="Currency for the fare (e.g., USD, EUR)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--version", "-v", action="version", version=f"fare-estimator CLI: {__version__}")

    args = parser.parse_args()

    d = args.distance
    r = args.rate
    c = args.currency

    calculated_fare = calculate_fare(d, r)
    print(f"The calculated fare for the ride is: {calculated_fare:.2f} {c}")

