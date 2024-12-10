#https://www.meetup.com/api/schema/
import json
import sqlite3

# Connect to the database
conn = sqlite3.connect(r'C:\Users\arjam\OneDrive\Desktop\Apollo.sqlite')
# Create a cursor object
cur = conn.cursor()
# Execute a query
cur.execute('SELECT * FROM records WHERE key LIKE "%adsdata.grouptopics%"')
# Fetch the results
rows = cur.fetchall()
# Parse the results
for row in rows:
    print(row)
data = json.loads(json_data)

# Accessing the data
print(data["name"])  # Output: John Doe
print(data["age"])   # Output: 30
print(data["courses"])  # Output: ['Math', 'Science', 'History']
