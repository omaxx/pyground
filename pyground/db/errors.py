class DBError(Exception):
    pass


class DoesNotExist(DBError):
    pass


class AlreadyExist(DBError):
    pass
