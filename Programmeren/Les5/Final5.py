stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']


def inlezen_beginpunt():
    while True:
        startStation = str(input('Wat is je beginstation: '))
        if(stations.count(startStation) > 0):
            return startStation
        else:
            print('Fout: Dit station bestaat niet.')


def inlezen_eindpunt(startStation):
    while True:
        try:
            eindStation = str(input('Wat is je endstation: '))
            if((stations.count(eindStation) > 0) & (stations.index(startStation) < stations.index(eindStation))):
                return eindStation
            else:
                print('Fout: Dit station bestaat niet of heeft een lagere index.')
        except:
            print('Fout: Dit station bestaat niet of heeft een lagere index.')


def omroepen_reis(startStation='Schagen', eindstation='Maastricht'):
    startStationIndex = stations.index(startStation)
    eindStationIndex = stations.index(eindstation)
    print('\nHet beginstation',startStation,'is het',str(startStationIndex + 1) + 'e station in het traject.')
    print('Het eindstation',eindstation,'is het',str(eindStationIndex + 1) + 'e station in het traject.')
    print('De afstand bedraagt',str(eindStationIndex - startStationIndex),'station(s).')
    print('De prijs van het kaartje is',str((eindStationIndex - startStationIndex) * 5),'euro.\n')

    print('Jij stapt in in:',startStation)
    i = startStationIndex + 1
    while(i < eindStationIndex):
        print(' -' ,stations[i])
        i = i + 1
    print('Jij stapt uit in:',eindstation)

print('De volgende stations zijn beschikbaar: ', ', '.join(stations),'\n')

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)