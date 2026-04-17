import argparse

__version__ = "1.0.0"

def add_item(item, quantity):
    print(f"Added {quantity} x {item} to your grocery list 🛒")


def view_list():
    print("Your grocery list:")
    print("- Milk (2)")
    print("- Bread (1)")

def weather(city):
    # Simulated weather data
    print(f"Fetching weather for {city}...")
    print("Temperature: 25°C")
    print("Condition: Sunny ☀️")
    print("Humidity: 60%")


def main():
    parser = argparse.ArgumentParser(description="Grocery List CLI")
    # Version flag
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"FareEstimator CLI {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add item to list")
    add_parser.add_argument("--item", required=True)
    add_parser.add_argument("--quantity", type=int, default=1)

    # View command
    subparsers.add_parser("view", help="View grocery list")

    # Weather command
    weather_parser = subparsers.add_parser("weather", help="Get weather for a city")
    weather_parser.add_argument("--city", required=True)

    args = parser.parse_args()

    if args.command == "add":
        add_item(args.item, args.quantity)
    elif args.command == "view":
        view_list()
    elif args.command == "weather":
        weather(args.city)


if __name__ == "__main__":
    main()

# Example usage:
# python grocery.py add --item "Eggs" --quantity 12
# uv run grocery.py add --item "Eggs" --quantity 12
# Output:
# Added 12 x Eggs to your grocery list 🛒

# Example usage:
# python grocery.py view
# uv run grocery.py view
# Output:
# Your grocery list:
# - Milk (2)
# - Bread (1)
# Note: This is a simplified example. In a real application, you'd want to store the list persistently (e.g., in a file or database).