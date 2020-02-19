import sqlite3 as sql

db = sql.connect('./manager.db')

dbCursor = db.cursor()


def AddTodo(todo:str, limit:str):
    dbCursor.execute("INSERT INTO TODO Values(?, ?)",(todo, limit))
    db.commit()

def GetAllData():
    # dbCursor.execute("SELECT * FROM {0}".format(table))
    dbCursor.execute("SELECT * FROM TODO")
    return dbCursor.fetchall()

def DeleteTodo(deleteTodo:str):
    dbCursor.excute("DELETE FROM Todo WHERE Todo = {0}".format(deleteTodo))
    db.commit()
