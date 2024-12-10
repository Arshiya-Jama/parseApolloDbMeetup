# parseApolloDbMeetup
iOS phones store an SQLite database called Apollo that holds most of the meetup user information in the following location: 
```tsql
\filesystem1\private\var\mobile\Containers\Data\Application\<App_ID>\Library\Application Support\Apollo 
```
This database includes a lot of information in the form of json dumps. I have identified some information that would be relevant in a forensic setting. The script is written in python and can be used to connect to the database and extract this information for further analysis. 

Run the script by the command: python3 parseApolloDB.py. It will then ask the user to input the path of the file is stored and provide a menu for the specific data to be searched. It will then output the information found.
