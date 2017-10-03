import os
import datetime
import requests
from jinja2 import Template, Environment, FileSystemLoader

mensaID = "372"

headers = {'User-Agent': 'mensa2mail 0.1',}
mypath = os.path.dirname(os.path.abspath(__file__))

def getData(mensaID, date):
    jsonCanteen = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/", headers=headers)
    jsonCanteenDay = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/days/"+date, headers=headers)
    jsonMeals = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/days/"+date+"/meals", headers=headers)
    canteen = jsonCanteen.json()
    canteenDay = jsonCanteenDay.json()
    meals = jsonMeals.json()
    return canteen, canteenDay['closed'], meals

d = datetime.datetime.today()
date=d.strftime('%Y-%m-%d')
#date="2017-07-04"
canteen, open, meals = getData(mensaID, date)
if open :
    date = d.strftime('%d.%m.')
    env = Environment(loader=FileSystemLoader(mypath), trim_blocks=True)
    print(env.get_template('template.txt').render(date=date, canteen=canteen, menues=meals))
#TODO: CLI
#TODO: sendmail