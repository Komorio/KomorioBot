import sqlite3 as sql




def AddTodo(todo:str, limit:str):
    db = sql.connect('./manager.db')
    dbCursor = db.cursor()

    dbCursor.execute("INSERT INTO TODO Values(?, ?)",(todo, limit))
    db.commit()

    dbCursor.close()
    db.close()

def GetAllData():
    db = sql.connect('./manager.db')
    dbCursor = db.cursor()

    # dbCursor.execute("SELECT * FROM {0}".format(table))
    dbCursor.execute("SELECT * FROM TODO")
    return dbCursor.fetchall()

def DeleteTodo(deleteTodo:str):
    db = sql.connect('./manager.db')
    dbCursor = db.cursor()

    dbCursor.excute('DELETE FROM TODO WHERE Todo = {}'.format(deleteTodo))
    db.commit()

    dbCursor.close()
    db.close()