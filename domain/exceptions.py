class ServiceDeskError(Exception):
    """Base exception for expected service desk errors."""


class RequestNotFoundError(ServiceDeskError):
    pass


class DuplicateRequestError(ServiceDeskError):
    pass


class InvalidPriorityError(ServiceDeskError):
    pass


class AlreadyResolvedError(ServiceDeskError):
    pass


class DataFileError(ServiceDeskError):
    pass
