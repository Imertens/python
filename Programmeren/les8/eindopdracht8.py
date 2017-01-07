import xmltodict

with open('les8.xml') as xmlBestand:
    stationLijst = xmltodict.parse(xmlBestand.read(),dict_constructor=dict)

eind = '{}'

print('Dit zijn de codes en types van de 4 stations:')
for stations in stationLijst['Stations']['Station']:
    code = stations['Code']
    type = stations['Type']
    print(eind.format(code),' -', type)


print('\nDit zijn alle stations met één of meer synoniemen:')
for stations in stationLijst['Stations']['Station']:
    if stations['Synoniemen'] !=  None:
        synoniemCode = stations['Code']
        synoniemen = stations['Synoniemen']
print(eind.format(synoniemCode),' -', (str(synoniemen)))


print('\nDit is de lange naam voor elk station:')
for stations in stationLijst['Stations']['Station']:
    naamCode = stations['Code']
    naamLang = stations['Namen']['Lang']
    print(eind.format(naamCode),' -', naamLang)