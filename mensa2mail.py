import requests
headers = {'User-Agent': 'mensa2mail 0.1',}

jsonCanteen = requests.get("https://openmensa.org/api/v2/canteens/372/", headers=headers)
jsonMeals = requests.get("https://openmensa.org/api/v2/canteens/372/days/2017-07-04/meals", headers=headers)
canteen = jsonCanteen.json()
meals = jsonMeals.json()
print(meals)
print(canteen)
#TODO: Render template
# https://stackoverflow.com/questions/19627911/how-to-see-if-a-string-contains-another-string-in-django-template
#TODO: CLI
#TODO: trigger only if open -> fallbackCanteen
#TODO: sendmail