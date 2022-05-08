import uuid

DB = {}  # this dict represents a test DB


class Carrier:
    """
    Class that describes a carrier.
    """

    def __init__(self, name: str, surname: str, latitude: float, longitude: float):
        self.carrier_id = str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.latitude = latitude
        self.longitude = longitude

    def save_to_db(self):
        DB[self.carrier_id] = self._to_db_dict()

    def delete(self):
        DB.pop(self.carrier_id)

    def _to_db_dict(self) -> dict:
        return {
            "carrier_id": self.carrier_id,
            "name": self.name,
            "surname": self.surname,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
