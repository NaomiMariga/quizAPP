from conn import dbconn

myCursor = dbconn.cursor()

#creating Database 
def createDatabase():
    #checking if database already exist
    myCursor.execute("SHOW DATABASES")

    databases = []
    for database in myCursor:
        databases.append(database) #getting all the existing databases. The result of each database is a one item tuple eg. ("test",)

    db = "test2"
    if ("{}".format(db),) not in databases:
        #creating database if it does not exist
        myCursor.execute("CREATE DATABASE {}".format(db)) 
        message = "database {} createed successfully".format(db)
        print (message)
        #creating tables
        
        try:
            myCursor.execute("USE {}".format(db))
            myCursor.execute("CREATE TABLE quiz (id INT AUTO_INCREMENT PRIMARY KEY, question TEXT NOT NULL, answer TEXT NOT NULL, option1 TEXT NOT NULL, option2 TEXT NOT NULL, option3 TEXT NOT NULL)")
            message = "Table quiz created successfully"
            print(message)
        except Exception as error:
            message = str(error)
            print(message)
        
    else:
        message = "database {} already exists".format(db)
        print(message)
    
#createDatabase()

def addQuizes(db,question, answer, option1, option2, option3):
    if question and answer and option1 and option2 and option3:
        myCursor.execute("USE {}".format(db))
        sql = "INSERT INTO quiz (question, answer, option1, option2, option3) VALUES (%S, %S, %S, %S)"
        values = (question, answer, option1, option2, option3)
        try: 
            myCursor.execute(sql, values)
            dbconn.commit() #required to make the changes, otherwise no changes are made to the table.
            message = "Quiz sussecfully added"
            print(message)
        except Exception as error:
            message = str(error)
            print(message)
    else:
        message = "All field are required"
        print (message)


def deleteDatabase(db):
    myCursor.execute("USE {}".format(db))
    myCursor.execute("SHOW TABLES")
    tables = []
    for table in myCursor:
        tables.append(table)
    
    print (tables)
    if tables != []:
        sql = "DROP TABLE quiz"
        myCursor.execute(sql)
        sql = "DROP DATABASE {}".format(db)
        myCursor.execute(sql)
        dbconn.commit()
        message = "Database {} deleted".format(db)
        print(message)
    else:
        sql = "DROP DATABASE {}".format(db)
        myCursor.execute(sql)
        dbconn.commit()
        message = "Database {} deleted".format(db)
        print(message)




