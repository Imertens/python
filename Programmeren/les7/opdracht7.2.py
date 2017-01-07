import datetime
import csv

def krijgTijd():
    tijd = datetime.datetime.today()
    return tijd.strftime("%a %d %b %Y at %H:%M")

with open('gebruikers.csv', 'w', newline='') as csvfile:
    fieldnames = ['tijd', 'naam', 'voorl', 'gbdatum', 'email',]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow({'tijd': krijgTijd(), 'naam': naam, 'voorl': voorl, 'gbdatum': gbdatum, 'email': email})