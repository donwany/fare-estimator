import argparse


def calculate_fare(distance, rate):
    fare = distance * rate
    print(f"Total fare: ${fare:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Ride Fare Calculator")

    parser.add_argument("--distance", "-d", type=float, required=True, help="Distance in miles")
    parser.add_argument("--rate", "-r", type=float, default=2.0, help="Rate per mile")

    args = parser.parse_args()

    calculate_fare(args.distance, args.rate)


if __name__ == "__main__":
    main()
