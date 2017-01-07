woord=''
while len(woord) != 4:
    woord = input('Geef een string van vier letters: ')
    if len(woord) != 4:
        if len(woord) == 0:
            print(woord, 'heeft', str(len(woord)), 'letter.')
        else:
            print(woord, 'heeft', str(len(woord)), 'letters.')

print('Inlezen van de correcte string:' ,woord ,'is geslaagd')