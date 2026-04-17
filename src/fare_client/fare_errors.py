class FareEstimatorError(Exception):
    """Base class for fare estimator errors."""

    pass


class InvalidDistanceError(FareEstimatorError):
    """Raised when distance is invalid."""

    pass


class InvalidRateError(FareEstimatorError):
    """Raised when duration is invalid."""

    pass
