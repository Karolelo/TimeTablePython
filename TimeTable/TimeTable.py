import os.path
from datetime import datetime
import Reader
import Writer
import joblib
import model
import Exceptions

class TimeTable:
    def __init__(self,numOfTable):
        self.filename = f"TimeTable.dat{numOfTable}"
        if(os.path.exists(self.filename)):
            self.table = Reader.Reader.reader.read_object(self.filename)
        else:
            self.table = []

        self.availableTags=set()
        for tag in self.table:
            self.availableTags.add(tag)
    def create_event(self, tag, dateOfEvent, description):
        event = model.Event.event(tag, dateOfEvent, description)
        self.table.append(event)
        Writer.Writer.writer.save_object( self.table,self.filename)
    def delete_event(self, id):
        if 0 <= id < len(self.table):
            to_delete = self.table[id]
            self.table.remove(to_delete)
            Writer.Writer.writer.save_object(self.table,self.filename)
        else:
            print(f"No event with id: {id}")

    def show_all_events(self):
        counter=0
        for event in self.table:
            print(f"{counter}.{event}\n")
            counter+=1
    def show_events_on_today(self):
        today = datetime.today().date()
        for event in self.table:
            if event.dateOfEvent == today:
                print(f"{event}\n")

    def show_event_on_certain_date(self, dateOfEvent):
        for event in self.table:
            if event.dateOfEvent == dateOfEvent:
                print(f"{event}\n")

    def show_events_from_to(self, dateFrom, dateTo):
        for event in self.table:
            if dateFrom <= event.dateOfEvent <= dateTo:
                print(f"{event}\n")

    def change_event_date(self,id,new_date):
        self.table[id].dateOfEvent=new_date
        Writer.Writer.writer.save_object(self.table,self.filename)


    def show_sorted_events_date_descending(self,revers):
        sorted_events = sorted(self.table, key=lambda event: event.dateOfEvent, reverse=revers)
        for event in sorted_events:
            print(f"{event}\n")

    def show_events_with_tag(self,tag):
        if tag in self.availableTags:
            for event in self.table:
                if event.tag == tag:
                    print(f"{event}\n")
        else:
            raise Exceptions.CustomExceptions.noSuchTagException
    def create_new_tag(self,tag):
        if tag not in self.availableTags:
            Exceptions.CustomExceptions.InvalidTagException(tag)
            self.availableTags.add(tag)
    def change_description_of_event(self,id,new_description):
        self.table[id].descript=new_description
