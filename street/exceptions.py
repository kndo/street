class StreetError(Exception):
    pass


class BadCookieWarning(StreetError):
    pass


class EarningsTableNotFound(StreetError):
    pass


class RequestBlocked(StreetError):
    pass