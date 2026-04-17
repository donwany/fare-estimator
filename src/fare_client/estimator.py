from fare_errors import InvalidRateError, InvalidDistanceError


class FareEstimator:
    def __init__(self):
        ...

    def estimate(self, distance, rate):
        """"""
        if distance <= 0:
            raise InvalidDistanceError("Distance must be greater than 0")

        if rate <= 0:
            raise InvalidRateError("Rate must be greater than 0")

        fare = distance * rate
        return fare
