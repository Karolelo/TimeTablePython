from datetime import datetime

class InvalidTagException(Exception):
    pass

    def validate_tag(self, tag):
        if not isinstance(tag, str) or not tag.strip():
            raise InvalidTagException("Tag must be a non-empty string.")
        return tag
class InvalidDateException(Exception):
    pass

    def validate_date(self, dateOfEvent):
        if not isinstance(dateOfEvent, datetime):
            raise InvalidDateException("dateOfEvent must be a datetime object.")
        return dateOfEvent
class InvalidDescriptionException(Exception):
    pass

    def validate_description(self, descript):
        if not isinstance(descript, str) or not descript.strip():
            raise InvalidDescriptionException("Description must be a non-empty string.")
        return descript

class noSuchTagException(Exception):
    def __init__(self, value):
        self.value = value
        message = "No such tag {}".format(value)
        super().__init__(message)
