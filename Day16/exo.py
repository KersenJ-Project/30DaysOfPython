from datetime import datetime, date

now = datetime.now()
jour = now.day
mois = now.month
annee = now.year
heure = now.hour
minute = now.minute
timestamp = now.timestamp()
print(jour, mois, annee, heure, minute)
print('timestamp', timestamp)

format_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("format date :", format_date)


date_string = "5 December, 2019"
print("chaîne_date =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("objet_date =", date_object)

new_year = date(year=2027, month=1, day=1)

print("Time till new year 2027:", new_year - now.date())

old_new_year = date(year=1970, month=1, day=1)

print("Time since new year 1970:", now.date() - old_new_year)