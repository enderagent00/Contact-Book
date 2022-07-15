
import re

class InputValidator:
    def validate_email(email: str):
        regex = r"[^@]+@[^@]+\.[^@]+"
        return re.match(regex, email)

    def validate_phone_number(phone_number: str):
        regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        return re.match(regex, phone_number)

