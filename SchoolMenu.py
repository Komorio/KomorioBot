import requests
import json
from datetime import datetime

def GetLunchMenu():
    apiUrl = "https://schoolmenukr.ml/api/high/B100000662?year={0}&month={1}&date={2}".format(datetime.today().year,datetime.today().month,datetime.today().day)
    response = requests.get(apiUrl)

    menuJson = json.loads(response.text)
    menuJson = json.dumps(menuJson['menu'])
    menuJson = json.loads(menuJson)

    lunchMenu = menuJson[0]['lunch']
    return lunchMenu