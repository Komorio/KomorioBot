import sqlite3 as sql


dbName = "komoriobot.db"

def AddTable(tableName:str):
    db = sql.connect(dbName)
    cursor = db.cursor()

    command = "CREATE TABLE {0} (title text, description text, footer text)".format(tableName)
    cursor.execute(command)
    
    db.close()

def DropTable(tableName:str):
    db = sql.connect(dbName)
    cursor = db.cursor()

    command = "DROP TABLE {0}".format(tableName)
    cursor.execute(command)

    db.close()


def InsertData(tableName:str, title:str = "", description:str ="", footer:str =""):
    db = sql.connect(dbName)
    cursor = db.cursor()
        
    command = "INSERT INTO {0} VALUES('{1}', '{2}', '{3}')".format(tableName, title, description, footer)
    cursor.execute(command)
    db.commit()

    db.close()


def DeleteData(tableName:str, title:str =""):
    db = sql.connect(dbName)
    cursor = db.cursor()

    command = "DELETE FROM {0} WHERE title = '{1}'".format(tableName, title)
    cursor.execute(command)
    db.commit()
    
    db.close()


def GetAllData(tableName:str):
    db = sql.connect(dbName)
    cursor = db.cursor()

    command = "SELECT * FROM {0}".format(tableName)
    cursor.execute(command)
    result = cursor.fetchall()
    db.close()
    
    return result

def CustomExecute(command:str):
    db = sql.connect(dbName)
    cursor = db.cursor()

    cursor.execute(command)
    result = cursor.fetchall()
    db.commit()
    db.close()

    return result