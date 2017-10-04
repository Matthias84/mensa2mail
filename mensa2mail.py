"""
Send mail listing meals from openmensa.org

Usage: mensa2mail.py MENSAID [--date=<date>]

-h --help    show this

"""

import os
import datetime
from docopt import docopt
from dateutil import parser
import requests
from jinja2 import Template, Environment, FileSystemLoader
import emoji

vers = 'mensa2mail 0.1'
headers = {'User-Agent': vers,}
mypath = os.path.dirname(os.path.abspath(__file__))

def getData(mensaID, date):
    jsonCanteen = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/", headers=headers)
    jsonCanteenDay = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/days/"+date, headers=headers)
    jsonMeals = requests.get("https://openmensa.org/api/v2/canteens/"+mensaID+"/days/"+date+"/meals", headers=headers)
    canteen = jsonCanteen.json()
    canteenDay = jsonCanteenDay.json()
    meals = jsonMeals.json()
    return canteen, not canteenDay['closed'], meals

arguments = docopt(__doc__, version=vers)
mensaID = arguments["MENSAID"].split("=")[1]
if arguments["--date"]:
    dt = parser.parse(arguments["--date"])
else:
    dt = datetime.datetime.today()
date=dt.strftime('%Y-%m-%d')
#date="2017-07-04"
canteen, open, meals = getData(mensaID, date)
if open :
    date = dt.strftime('%d.%m.')
    env = Environment(loader=FileSystemLoader(mypath), trim_blocks=True)
    txt = env.get_template('template.txt').render(date=date, canteen=canteen, menues=meals)
    txt = emoji.emojize(txt, use_aliases=True)
    print(txt)

#TODO: sendmail
#TODO: Fehlerfall API abfangen
