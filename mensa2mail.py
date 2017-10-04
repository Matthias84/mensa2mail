"""
Send mail listing meals from openmensa.org

Usage: mensa2mail.py MENSAID MENSAID2 FROM TO SERVER USER PASSWORD [--date=<date>]

"""

import os
import datetime
from docopt import docopt
from dateutil import parser
import requests
from jinja2 import Template, Environment, FileSystemLoader
import emoji
import smtplib
from email.message import EmailMessage

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

def sendReport(arguments, canteen, meals):
    date = dt.strftime('%d.%m.')
    env = Environment(loader=FileSystemLoader(mypath), trim_blocks=True)
    txt = env.get_template('template.txt').render(date=date, canteen=canteen, menues=meals)
    txt = emoji.emojize(txt, use_aliases=True)
    print(txt)
    subject = txt.split('\n', 1)[0]
    content = txt.split('\n', 1)[1]
    mailFrom = arguments["FROM"]
    mailTo = arguments["TO"]
    user = arguments["USER"]
    pw = arguments["PASSWORD"]
    server = arguments["SERVER"]
    sendEmail(content, subject, mailFrom, mailTo, server, user, pw)

def sendEmail(content, subject, emailFrom, emailTo, server, username, password):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = emailFrom
    msg["To"] = emailTo
    msg["X-Priority"] = '5'
    conn = smtplib.SMTP(server, 587)
    conn.ehlo()
    conn.starttls()
    conn.login(username, password)
    conn.sendmail(emailFrom, emailTo, msg.as_string())
    conn.close()

arguments = docopt(__doc__, version=vers)
mensaID = arguments["MENSAID"].split("=")[1]
if arguments["--date"]:
    dt = parser.parse(arguments["--date"])
else:
    dt = datetime.datetime.today()
date=dt.strftime('%Y-%m-%d')
#date="2017-07-04"
canteen, open, meals = getData(mensaID, date)
if open:
    sendReport(arguments, canteen, meals)
else:
    # fallback mensa2
    mensaID = arguments["MENSAID2"].split("=")[1]
    canteen, open, meals = getData(mensaID, date)
    if open:
        sendReport(arguments, canteen, meals)
    else:
        print("All mensas closed!")



#TODO: logging
#TODO: Fehlerfall API abfangen
