getal= -1
aantal= -1
totaal= 0
while getal != 0:
    getal = int(input('Geef een getal: '))
    aantal += 1
    totaal += getal
print('Er zijn', aantal, 'getallen ingevoerd, de som is:', totaal)