import mysql.connector
from creds import creds

# conneting to the database 
dbconn = mysql.connector.connect(
host = creds["host"],
user = creds["user"],
password = creds["code"]
)
