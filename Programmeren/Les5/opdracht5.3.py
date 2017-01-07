invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
nieuwinvoer = invoer.split("-")
nieuwinvoer = [int(i) for i in nieuwinvoer]
nieuwinvoer.sort()

totaal = 0
for num in nieuwinvoer:
    totaal = totaal + num

aantal = len(nieuwinvoer)
maximum = max(nieuwinvoer)
minimum = min(nieuwinvoer)
gemiddeld = totaal / aantal




print('Gesorteerde list van ints: ', nieuwinvoer)
print('Het grootste getal is:', maximum, ' en het kleinste getaal is:', minimum)

print('Aantal getallen is:', aantal,   'en de som van de getallen is:', totaal)
print('Gemiddelde is:', gemiddeld)

















