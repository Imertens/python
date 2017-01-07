import csv

lijst = []
with open('gamers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for rij in reader:
       lijst += rij

for element in lijst:
    parts = element.split(',')

hoogste = max(parts)
naam, datum, score = hoogste.split(";")
print('De hoogste score is:',score,'op',datum,'gehaald door',naam)
