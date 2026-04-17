import argparse

__version__ = "1.0.0"

class FareEstimatorError(Exception):
    """Base exception for fare estimator."""
    pass


class InvalidDistanceError(FareEstimatorError):
    pass


class InvalidRateError(FareEstimatorError):
    pass


class FareEstimator:
    def __init__(self, base_fare=2.5):
        self.base_fare = base_fare

    def estimate(self, distance, rate):
        if distance <= 0:
            raise InvalidDistanceError("Distance must be greater than 0.")

        if rate <= 0:
            raise InvalidRateError("Rate must be greater than 0.")

        return self.base_fare + (distance * rate)


def main():
    parser = argparse.ArgumentParser(
        description="Estimate ride fare from distance and rate."
    )

    # Version flag
    parser.add_argument(
        "--version",
        action="version",
        version=f"FareEstimator CLI {__version__}"
    )

    parser.add_argument("--distance", type=float, required=True)
    parser.add_argument("--rate", type=float, required=True)
    parser.add_argument("--base", type=float, default=2.5)

    args = parser.parse_args()

    estimator = FareEstimator(base_fare=args.base)

    try:
        fare = estimator.estimate(args.distance, args.rate)
        print(f"Estimated Fare: ${fare:.2f}")

    except FareEstimatorError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()