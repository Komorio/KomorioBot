from Database import *;
from datetime import datetime, timedelta

def AddTomorrowTodo(name:str, description:str):
    date = str(datetime.today() + timedelta(1))
    date = date.split(" ")[0]
    InsertData("TodayTodo",name, description, date)

def AddTodayTodo(name:str, description:str):
    date = str(datetime.today())
    date = date.split(" ")[0]

    InsertData("TodayTodo",name, description, date)

def GetTodayTodo():
    date = str(datetime.today())
    date = date.split(" ")[0]

    command = "SELECT * FROM TodayTodo WHERE footer = \"{0}\"".format(date)
    result = CustomExecute(command)
    
    return result
