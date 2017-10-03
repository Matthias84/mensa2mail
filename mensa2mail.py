import os
import requests
from jinja2 import Template, Environment, FileSystemLoader
headers = {'User-Agent': 'mensa2mail 0.1',}
mypath = os.path.dirname(os.path.abspath(__file__))

date="2017-07-04"
jsonCanteen = requests.get("https://openmensa.org/api/v2/canteens/372/", headers=headers)
jsonMeals = requests.get("https://openmensa.org/api/v2/canteens/372/days/"+date+"/meals", headers=headers)
canteen = jsonCanteen.json()
meals = jsonMeals.json()
env = Environment(loader=FileSystemLoader(mypath), trim_blocks=True)
print(env.get_template('template.txt').render(date=date, canteen=canteen, menues=meals))
# https://stackoverflow.com/questions/19627911/how-to-see-if-a-string-contains-another-string-in-django-template
#TODO: CLI
#TODO: trigger only if open -> fallbackCanteen
#TODO: sendmail
#TODO: kürzeres Datum