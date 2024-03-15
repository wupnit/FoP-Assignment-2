import re

# Prompts user to select an event
def selectEvent(database):
    nam=input('What is the name of the event?')
    for sub_list in database:
        if nam in sub_list:
            y= database.index(sub_list)
            return y
    print("Event not found!!!")
    
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

    eventINDEX = selectEvent(database)
    loop = True
    while loop:
        print()
        print(f"Event Name       : {database[eventINDEX][0]}")
        print(f"Event Description: {database[eventINDEX][1]}")
        print(f"Event Location   : {database[eventINDEX][2]}")
        print(f"Event Date       : {database[eventINDEX][3]}")
        print(f"Event Time, START: {database[eventINDEX][4]}")
        print(f"             END : {database[eventINDEX][5]}")
        j = ", ".join(database[eventINDEX][6])
        print(f"Attendee(s)      : {j}")
        print()
        print("◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉")
        print("            Event Update")
        print("                Menu")
        print("    1. Event Name")
        print("    2. Event Description")
        print("    3. Event Location")
        print("    4. Event Date")
        print("    5. Event Time")
        print("    6. Event Attendee's Name")
        print("    7. Back to Main Menu")
        print("◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉")
        updateChoice = input("Enter choice: ")

        if updateChoice.isdigit():
            updateChoice = int(updateChoice)
            
            # 1. Event Name
            if updateChoice == 1:
                updateEventName = input("Enter a new event name: ")
                database[eventINDEX][0] = updateEventName
                print("Event Name updated!")

            # 2. Event Description    
            elif updateChoice == 2:
                updateEventDescription = input("Enter a new event description: ")
                database[eventINDEX][1] = updateEventDescription
                print("Event Description updated!")

            # 3. Event Location
            elif updateChoice == 3:
                updateEventLocation = input("Enter a new event location: ")
                database[eventINDEX][2] = updateEventLocation
                print("Event Location updated!")

            # 4. Event Date    
            elif updateChoice == 4:
                updateEventDate = input("Enter a new event date: ")
                database[eventINDEX][3] = updateEventDate
                print("Event Date updated!")

            # 5. Event Time
            elif updateChoice == 5:
                loop_Time = True
                while loop_Time:
                    print()
                    print("Which do you want to update?")
                    print(" 1. Start Time")
                    print(" 2. End Time")
                    print(" 3. Go back")
                    print()
                    timeChoice = input("Your choice: ")

                    if timeChoice.isdigit():
                        timeChoice = int(timeChoice)

                        # 1. Start Time
                        if timeChoice == 1:
                            updateEventStartTime = input("Enter a new event start time: ")
                            database[eventINDEX][4] = updateEventStartTime
                            print("Event Start Time updated!")
                            
                        # 2. End Time
                        elif timeChoice == 2:
                            updateEventEndTime = input("Enter a new event end time: ")
                            database[eventINDEX][5] = updateEventEndTime
                            print("Event End Time updated!")

                        # 3. Go back
                        elif timeChoice == 3:
                            loop_Time = False

                        else:
                            print("Please try again.")
                    
                    else:
                        print("Try again. Choose 1 or 2 only.")

            # 6. Event Attendee's Name
            elif updateChoice == 6:
                loop_AttendeeName = True
                while loop_AttendeeName:
                    number = 1
                    print()
                    print("Attendees List:")
                    for i in database[eventINDEX][6]:
                        print(f"    {number}. {i}")
                        number += 1
                    
                    print()
                    print("What do you want to do?")
                    print(" 1. Add Attendee")
                    print(" 2. Delete Attendee")
                    print(" 3. Change Attendee's Name")
                    print(" 4. Go back")
                    print()
                    updateEventAttendeeName =input("What to do?: ")

                    if updateEventAttendeeName.isdigit():
                        updateEventAttendeeName = int(updateEventAttendeeName)

                        # 1. Add Attendee
                        if updateEventAttendeeName == 1:
                            addName = input("Who to add? (ENTER NAME): ")
                            database[eventINDEX][6].append(addName)
                            print("Attendee Name added!")

                        # 2. Delete Attendee
                        elif updateEventAttendeeName == 2:
                            loop_deleteAttendee = True
                            while loop_deleteAttendee:
                                deleteName = input("Who do you wish to delete? (ENTER NUMBER): ")

                                if deleteName.isdigit():
                                    deleteName = int(deleteName)

                                    if deleteName <= 0:
                                        print("Try again.")

                                    elif deleteName <= len(database[eventINDEX][6]):

                                        # Confirmation
                                        loop_ConfirmProceed = True
                                        while loop_ConfirmProceed:
                                            print()
                                            confirmProceed = input("Are you sure? (Y or N) : ")
                                            confirmProceed = confirmProceed.upper()

                                            if confirmProceed == "Y":
                                                database[eventINDEX][6].pop(deleteName - 1)
                                                print("Attendee Name deleted!")
                                                loop_ConfirmProceed = False
                                            
                                            elif confirmProceed == "N":
                                                loop_ConfirmProceed = False

                                            else:
                                                print("Enter 'Y' or 'N' only. Try again.")

                                        loop_deleteAttendee = False

                                    else:
                                        print("Try again.")
                                    
                                else:
                                    print("Please try again.")

                        # 3. Change Attendee's Name
                        elif updateEventAttendeeName == 3:
                            changeName = input("Which Attendee do you wish to change? (ENTER NUMBER) : ")

                            if changeName.isdigit():
                                changeName = int(changeName)

                                if changeName <= 0:
                                    print("Try again.")
                                
                                elif changeName <= len(database[eventINDEX][6]):
                                    print()
                                    newlyChangedName = input(f"Change '{database[eventINDEX][6][changeName - 1]}' to? (ENTER NAME): ")
                                    database[eventINDEX][6][changeName - 1] = newlyChangedName
                                    print("Attendee Name changed!")

                                else:
                                    print("Try again.")
                        
                            else:
                                print("Numbers only. Try again.")

                            # 4. Go back
                        elif updateEventAttendeeName == 4:
                            loop_AttendeeName = False

                        else:
                            print("Invalid. Please try again.")

                    else:
                        print("Invalid options. Please try again.")

                print(database[eventINDEX])

            # 7. Back to Main Menu
            elif updateChoice == 7:
                print("Back to Main Menu......")
                loop = False
            
            else:
                print("Enter valid options only. Try again.")
        
        else:
            print("Please try again. Enter digits only.")

    return database

# Delete existing event
def deleteEvent(database):
    printSchedule(database)
    delegroup= selectEvent(database)
    del database[delegroup]
    print("Event succcessfully deleted :)")
    return database

# Manage attendees menu
def manageAttendees(database):
    pass

# Prints event schedule:
def printSchedule(database):
    event = database[selectEvent(database)]
    print('Name:',event[0])
    print('Description:',event[1])
    print('Location:',event [2])
    print('Date:',event[3])
    print('StartTime:',event[4])
    print('EndTime:',event[5])
    j = ", ".join(event[6])
    print('Attendee:',j)





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