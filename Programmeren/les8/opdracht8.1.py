import xmltodict

with open('producten.xml') as xmlBestand:
    xml = xmltodict.parse(xmlBestand.read(),dict_constructor=dict)

for producten in xml['artikelen']['artikel']:
    print(producten['naam'])