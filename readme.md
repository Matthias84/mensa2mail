A simple Python script to mail daily canteen menu by www.openmensa.org
Can fallback to another canteen / mensa if first one is closed.
Sends mails like this example:
> subject: 🍴 Menüs am 04.10. (Mensa Kleine Ulme)
> * 🥕 Broccoli und Champignons in Mandelsauce (vegan) 1.45€ / 2.4€
> * 🍳 Blumenkohl-Käsemedaillon (vegetarisch) 0.8€ / 2.75€
> * 🍳 Spätzle-Pilzpfanne (vegetarisch) 1.5€ / 2.6€
> * 🍖 Kabeljaufilet, natur (aus nachhaltiger Fischerei) 1.75€ / 3.75€
> * 🍖 Steak mit Würzfleisch überbacken 2.0€ / 4.5€
> * 🍖 Hähnchenbrustfilet in Mandelpanade 1.2€ / 3.15€
> * 🍖 Käsesauce mit Schinken und Erbsen 1.35€ / 3.2€
>
> 🍳 Guten Appetit! 👨🍳
>
> Ulmenstraße 45, 18057 Rostock, Germany (https://www.openstreetmap.org/?mlat=54.08786795&mlon=12.1079285474557)

Uses the json APIv2 of OpenMensa and is build upon Python3 and requests, jinja2 libs.

# Usage

* You might want to setup an Python3 virtual environment
* Install dependencies: `pip install -r requirements.txt`
* Find your Mensas [OpenMensa IDs](https://openmensa.org) (click at map, copy id from URL)
* Invoke via `python --mensaid=372 --mensaid2=373 --emailfrom=bot@mydomain.de --emailto=receiver@mydomain.de --smtpserver=mydomain.de --smtpuser=bot@mydomain.de --smtppass=secret`
  * you might wan to add `--date=2017-10-1`if you prefer not todays meals
* Customize `template.txt` for your needs, you can use all OpenMensa [API properties](openmensa.org/api/v2/canteens/)
* Add a cronjob e.g. for every weekday 8am : `0 08 * * 1-5 python ...`

# Mensa missing?

If your mensa / canteen is still missed, you might want to [contribute](https://openmensa.org/contribute) to the project. Help by extending their [python scrapers](https://github.com/mswart/openmensa-parsers)!
