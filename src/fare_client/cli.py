import argparse
from estimator import FareEstimator
from fare_errors import FareEstimatorError, InvalidRateError, InvalidDistanceError
from utils import parsers, book_ride, estimate_ride, ask_doctor_question


def main():
    args = parsers()

    # d = args.distance
    # r = args.rate
    # c = args.currency
    #
    # estimator = FareEstimator()
    # calculated_fare = estimator.estimate(distance=d, rate=r)
    # print(f"The calculated fare for the ride is: {calculated_fare:.2f} {c}")

    try:
        # command usage
        if args.command == "book":
            print(book_ride(args))
        elif args.command == "estimate":
            estimate_ride(args)
        elif args.command == "doctor":
            ask_doctor_question(args)
        else:
            print("Nothing to do")

    except InvalidRateError as ex:
        print(f"Rate error: {ex}")
    except InvalidDistanceError as ex:
        print(f"Distance error: {ex}")
    except FareEstimatorError as ex:
        print(f"General fare error: {ex}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    main()
