stations = ['schagen', 'heerhugowaard', 'alkmaar', 'castricum', 'amsterdam sloterdijk', 'amsterdam centraal', 'amsterdam amstel', 'utrecht centraal', 's-hertogenbosch', 'eindhoven', 'weert', 'roermond', 'sittard', 'maastricht']
beginstation = input('Wat is je beginstation? :')

if beginstation not in stations:
    print('Je station', beginstation, 'staat niet op de route, je beginstation is: schagen')
    beginstation = 'schagen'

eindstation = input('Wat is je eindstation? :')

if eindstation not in stations or stations.index(eindstation) <= stations.index(beginstation) :
    print('Je eindstation', eindstation, 'staat niet op de route, je eindstation is: maastricht')
    eindstation = 'maastricht'

beginnummer = stations.index(beginstation) +1
eindnummer = stations.index(eindstation) +1
afstand = eindnummer-beginnummer
prijs = afstand*5

print('\nHet beginstation', beginstation, 'is station nummer', beginnummer, 'op de route.')
print('Het eindstation', eindstation, 'is het station nummer', eindnummer, 'op de route.')
print('De reis duurt', afstand, 'stations.')
print('De prijs is', prijs, 'euro.')
print('U stapt in in:', beginstation)
print('\nDe tussen stations zijn:')
for i in range(beginnummer, eindnummer-1):
    print('-', stations[i])
print('\nU stapt uit in:', eindstation)
