leeftijd = int(input('Geef je leeftijd:'))
paspoort = input('Heb je een Nederlands paspoort:')
if leeftijd > 17 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag nog niet stemmen')

