
class Contact:
    def __init__(self, _id: int, name: str, email: str, phone_number: str):
        self.id = _id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"({self.name}, {self.email}, {self.phone_number})"

UNDEFINED_ID = -1
