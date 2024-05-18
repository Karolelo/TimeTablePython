import sys
from datetime import datetime
from TimeTable import TimeTable
from PasswordLock import PassManager

def print_menu():
    print("1. Create event")
    print("2. Delete event")
    print("3. Show all events")
    print("4. Show events on today")
    print("5. Show events on a certain date")
    print("6. Show events from date to date")
    print("7. Change event date")
    print("8. Modify description")
    print("9. Show sorted events by date")
    print("10. Show events with tag")
    print("11. Create new tag")
    print("0. Exit")

password_manager = PassManager.PasswordManager()
logged_in = False
number_to_int = ()

def print_login_menu():
    print("1. Create user account")
    print("2. Log in")
    print("0. Exit")

while not logged_in:
    print_login_menu()
    choice = input("Enter your choice:")

    if choice == '1':
        login = input("Enter your login:")
        password = input("Enter your password:")
        password_manager.create_account(login, password)
    elif choice == '2':
        login = input("Enter your login:")
        password = input("Enter your password:")
        logged_in, user_number = password_manager.log_in(login, password)
        number_to_int = (logged_in, user_number)
    elif choice == '0':
        sys.exit()

timetable = TimeTable.TimeTable(number_to_int[1])

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        tag = input("Enter tag: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        date_of_event = datetime.strptime(date_str, "%Y-%m-%d").date()
        timetable.create_event(tag, date_of_event, description)
    elif choice == '2':
        timetable.show_all_events()
        id = int(input("Enter event ID to delete: "))
        timetable.delete_event(id)
    elif choice == '3':
        timetable.show_all_events()
    elif choice == '4':
        timetable.show_events_on_today()
    elif choice == '5':
        date_str = input("Enter date (YYYY-MM-DD): ")
        date_of_event = datetime.strptime(date_str, "%Y-%m-%d").date()
        timetable.show_event_on_certain_date(date_of_event)
    elif choice == '6':
        date_from_str = input("Enter start date (YYYY-MM-DD): ")
        date_to_str = input("Enter end date (YYYY-MM-DD): ")
        date_from = datetime.strptime(date_from_str, "%Y-%m-%d").date()
        date_to = datetime.strptime(date_to_str, "%Y-%m-%d").date()
        timetable.show_events_from_to(date_from, date_to)
    elif choice == '7':
        timetable.show_all_events()
        number = int(input("Enter number: "))
        new_date_str = input("Enter new date (YYYY-MM-DD): ")
        new_date_of_event = datetime.strptime(new_date_str, "%Y-%m-%d").date()
        timetable.change_event_date(number, new_date_of_event)
    elif choice == '8':
        timetable.show_all_events()
        number = int(input("Enter number: "))
        descrip = input("Enter description text: ")
        timetable.change_description_of_event(number, descrip)
    elif choice == '9':
        revers = input("Sort descending? (yes/no): ").lower() == 'yes'
        timetable.show_sorted_events_date_descending(revers)
    elif choice == '10':
        tag = input("Enter tag: ")
        timetable.show_events_with_tag(tag)
    elif choice == '11':
        tag = input("Enter new tag: ")
        timetable.create_new_tag(tag)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")