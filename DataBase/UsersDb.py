import sqlite3


def CreateTable():
    sqliteConnection = sqlite3.connect('mobiledb.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("CREATE TABLE  IF NOT EXISTS UserTable(username, password, contactnumber,emailid,address,location)")
    cursor.execute("""
        insert into UserTable values
                   ('thinesh','123','1234567890','thinesh@gmail.com','add1','172.19.0'),
                   ('seeni','123','1234567890','seeni@gmail.com','add1','172.19.0')
    """)
    sqliteConnection.commit()

    cursor.execute("select * from UserTable")
    userdt = cursor.fetchall()
    print(userdt)

    cursor.close()
    sqliteConnection.close()
    return True
    

    



def ValidateDBLogin(username, password):
    CreateTable()
    sqliteConnection = sqlite3.connect('mobiledb.db')
    cursor = sqliteConnection.cursor()   
    cursor.execute("SELECT COUNT(1) FROM UserTable WHERE username = ? AND password = ?", (username, password))
    userdt = cursor.fetchone()[0]
    print(userdt)
    cursor.close()
    sqliteConnection.close()
    if(userdt > 0):
         return 1
    else:
         return 0



