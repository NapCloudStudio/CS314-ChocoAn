class Provider:
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"


class Member:
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"
    STATUS_SUSPENDED = "suspended"

# immutable address object returned from dao
class Address:
    def __init__(self, db_record: tuple):
        self._id = db_record[0]
        self._street = db_record[1]
        self._city = db_record[2]
        self._state = db_record[3]
        self._zip = db_record[4]

    def id(self) -> int:
        return self._id

    def street(self) -> str:
        return self._street

    def city(self) -> str:
        return self._city

    def state(self) -> str:
        return self._state

    def zipcode(self) -> str:
        return self._zip
