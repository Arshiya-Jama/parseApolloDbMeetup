#https://www.meetup.com/api/schema/
import json
import sqlite3
import re

def showAdData(cur):
    cur.execute('SELECT * FROM records WHERE key LIKE "%adsdata.grouptopics%"')
    # Fetch the results
    rows = cur.fetchall()
    # Parse the results
    print("Data that meetup uses to create personalised group recommendations:")
    for row in rows:
        data = json.loads(row[2])
        print("Type of " + data["__typename"] + ": " + data["name"])
    return

def notificationInfo(cur):
    cur.execute('SELECT * FROM records WHERE key LIKE "%notification%"')
    rows = cur.fetchall()
    print("Notification Data:")
    for row in rows:
        data = json.loads(row[2])
        printJsonData(data)
        print('\n')
    return

def printJsonData(obj, indent=0):
    for key, value in obj.items():
        print("  " * indent + f"{key}: ", end="")
        if isinstance(value, dict):  # Nested dictionary
            print()
            printJsonData(value, indent + 1)
        elif isinstance(value, list):  # List elements
            print()
            for item in value:
                print("  " * (indent + 1) + f"- {item}")
        else:  # Base case: direct key-value
            print(value)
    return

def userDetails(cur):
    cur.execute('SELECT * FROM records WHERE key="QUERY_ROOT.self"')
    rows = cur.fetchall()
    print("User Data:")
    for row in rows:
        data = json.loads(row[2])
        printJsonData(data)
        print("\n")
    return

def userInterets(cur):
    cur.execute('SELECT * FROM records WHERE key LIKE "%memberprofile%"')
    rows = cur.fetchall()
    print("User Interests are:")
    for row in rows:
        data = json.loads(row[2])
        if "id" in data:
            print(data["name"])
    return

def nextupcomingevent(cur):
    cur.execute('SELECT * FROM records WHERE key LIKE "%nextupcomingevent%"')
    rows = cur.fetchall()
    print("Next Event:")
    for row in rows:
        data = json.loads(row[2])
        printJsonData(data)
    return

def groupComments(cur):
    cur.execute('SELECT * FROM records WHERE key LIKE "QUERY_ROOT.event%"')
    rows = cur.fetchall()
    setOfID = set([])
    for row in rows:
        #Find all the event IDs and make a list
        pattern = r"id:(\d+)"
        match = re.search(pattern, row[1])
        if match:
            setOfID.add(match.group(1))
    for i in setOfID:
        #Parse through the event IDs and extract all details one by one
        print("Event details for event ID: " + i)
        for row in rows:
            data = json.loads(row[2])
            if (i in row[1] and data["__typename"] == "Event"):
                printJsonData(data)
                print('\n')

            elif (i in row[1] and data["__typename"] == "User"):
                print("User: " + data["name"] + '\n')

            elif i in row[1] and data["__typename"] == "EventComment":
                print(data['created'] + ": " + data["text"] + '\n')
    return


filePath = print("Enter the path - including the file name")
# Connect to the database
conn = sqlite3.connect(filePath)
# Create a cursor object
cur = conn.cursor()
while True:
    print("\nMain Menu")
    print("1. Show Data used by meetup to personalize adverts")
    print("2. Notification information")
    print("3. User Details")
    print("4. User Interests")
    print("5. Next Event")
    print("6. Event Details")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        showAdData(cur)
    elif choice == 2:
        notificationInfo(cur)
    elif choice == 3:
        userDetails(cur)
    elif choice == 4:
        userInterets(cur)
    elif choice == 5:
        nextupcomingevent(cur)
    elif choice == 6:
        groupComments(cur)
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
