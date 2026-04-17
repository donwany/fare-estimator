import argparse


def get_weather(city, units):
    # Simulated weather data
    print(f"Fetching weather for {city}...")
    print(f"Temperature: 25° ({units})")
    print("Condition: Sunny ☀️")


def main():
    parser = argparse.ArgumentParser(description="Weather App CLI")

    # Required argument
    parser.add_argument("--city", type=str, required=True, help="City name")

    # Optional argument
    parser.add_argument(
        "--units",
        type=str,
        choices=["metric", "imperial"],
        default="metric",
        help="Units for temperature"
    )

    args = parser.parse_args()

    get_weather(args.city, args.units)


if __name__ == "__main__":
    main()

# Example usage:
# python weather.py --city "Accra" --units imperial
# uv run weather.py --city "Accra" --units imperial

# Output:
# Fetching weather for Accra...
# Temperature: 25° (imperial)
# Condition: Sunny ☀️
