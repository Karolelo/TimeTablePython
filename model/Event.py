import Exceptions
class event:
    def __init__(self,tag,dateOfEvent,descript):
        Exceptions.CustomExceptions.InvalidTagException(tag)
        Exceptions.CustomExceptions.InvalidDateException(dateOfEvent)
        Exceptions.CustomExceptions.InvalidDescriptionException(descript)
        self.tag = tag
        self.dateOfEvent = dateOfEvent
        self.descript = descript

    def __str__(self):
        return f"Event: {self.tag}, Date: {self.dateOfEvent}, Description: {self.descript}"