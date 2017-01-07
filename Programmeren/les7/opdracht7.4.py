import csv

artikelnummer = []
artikelcode = []
naam = []
voorraad = []
prijs = []
with open('artikel.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artikelnummer.append(row['Artikelnummer'])
        artikelcode.append(row['Artikelcode'])
        naam.append(row['Naam'])
        voorraad.append(int(row['Voorraad']))
        prijs.append(float(row['Prijs']))


totaalProducten = sum(voorraad)

hoogstePrijs = (max(prijs))
hoogsteNaamIndex = prijs.index(hoogstePrijs)
hoogsteNaam = naam[hoogsteNaamIndex]

laagsteVoorraad = (min(voorraad))
laagsteVoorraadNaamIndex = voorraad.index(laagsteVoorraad)
laagsteVoorraadNaam = artikelnummer[laagsteVoorraadNaamIndex]

print('Het duurste artikel is',hoogsteNaam,'met een prijs van',hoogstePrijs,'euro')
print('Er zijn slechts',laagsteVoorraad,'exemplaren in voorraad van het product met nummer',laagsteVoorraadNaam)
print('In totaal hebben we',totaalProducten,'producten in ons exemplaar liggen')



