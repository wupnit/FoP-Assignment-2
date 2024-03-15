import re

# Prompts user to select an event
def selectEvent(database):
    pass

# Register a new event
def registerEvent(database):
    events = []

    def eventinput():
        name = input("Enter event name: ")
        loop_date = True
        while loop_date:
            date = input("Enter a date (DD/MM/YY): ")
            match = re.match(r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([0-9][0-9])$", date)
            if match:
                date = match.group(0)
                print("Event Date added!")
                loop_date = False
            else:
                print("Invalid Date. Please use the format DD/MM/YY")
        loop_startTime = True
        while loop_startTime:
            start_time = input("Enter a start time in 24h format (HH:MM): ")
            match = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", start_time)
            if match:
                start_time = match.group(0)
                print("Event Start Time added!")
                loop_startTime = False
            else:
                print("Invalid Time format. Please use the format HH:MM")
        loop_endTime = True
        while loop_endTime:
            end_time = input("Enter a start time in 24h format (HH:MM): ")
            match = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", end_time)
            if match:
                start_time = match.group(0)
                print("Event End Time added!")
                loop_endTime = False
            else:
                print("Invalid Time format. Please use the format HH:MM")
        location = input("Enter event location: ")
        description = input("Enter event description: ")
        event = [name,description,location,date,start_time,end_time,[]]
        events.append(event)
        print("\nEvent:")
        print(f"\nName: {name}\nDate: {date}\nStart Time: {start_time}\nEnd Time: {end_time}\nLocation: {location}\nDescription: {name}\n")
        new = input("Add another event? Type 'y' for yes, 'n' for no.: ")
        while new == "y":
            name = input("Enter event name: ")
            date = input("Enter the date:")
            start_time = input("Enter event start time in 24 hour format (HH:MM):")
            end_time = input("Enter event end time in 24 hour format(HH:MM): ")
            location = input("Enter event location: ")
            description = input("Enter event description: ")
            events.append(event)
            print("\nEvent:")
            print(f"\nName: {name}\nDate: {date}\nStart Time: {start_time}\nEnd Time: {end_time}\nLocation: {location}\nDescription: {name}\n")
            new = input("Add another event? Type 'y' for yes, 'n' for no.: ")
        print("bye")

    eventinput()

    # eventINDEX = selectEvent(database)
    # location = database[eventINDEX][2]
    # date = database[eventINDEX][3]

    # for event in database:
    #     if location == database[eventINDEX][2]:
    #         if date == database[eventINDEX][2]:
    #     else:
    #         print("Clashing events")
    # return database

# Update existing event
def updateEvent(database):
    pass

# Delete existing event
def deleteEvent(database):
    pass

# Manage attendees menu
def manageAttendees(database):
    pass

# Prints event schedule:
def printSchedule(database):
    pass

while True:
    # Read data from database
    database = []
    with open('database.txt', 'r') as file:
        content = file.readlines()
    for event in content:
        event = event.strip('\n')
        event = event.split(', ')
        event = event[:6] + [event[6:]]
        database.append(event)
    
    print('''
        Event Management System
                Menu
    1. Register new event
    2. Update an existing event
    3. Delete an existing event
    4. Manage attendees for an existing event
    5. Print event schedule
    6. Exit''')
    choice = input('Enter choice: ')
    if choice == '1':
        database = registerEvent(database)
    elif choice == '2':
        database = updateEvent(database)
    elif choice == '3':
        database = deleteEvent(database)
    elif choice == '4':
        database = manageAttendees(database)
    elif choice == '5':
        printSchedule(database)
    elif choice =='6':
        break
    else:
        print('Error: Invalid choice')

    # Testing the database
    # database = [database[0]]

    # Converts to format of database
    databaseString = ''
    for event in database:
        eventString = ''
        for item in event[:-1]:
            eventString += item + ', '
        attendees = event[-1]
        for person in attendees:
            eventString += person + ', '
        eventString = eventString.strip(', ') + '\n'

        databaseString += eventString

    # Writes to database
    with open('database.txt','w') as file:
        file.write(databaseString)