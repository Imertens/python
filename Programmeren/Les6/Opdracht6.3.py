def namen():
    namen = {}
    naam = '-'

    while naam != '':
        naam = input('Volgende naam: ')
        if naam != '':
            if naam in namen:
                namen[naam] += 1
            else:
                namen[naam] = 1

    for x in namen:
        if namen[x] == 1:
            print('Er is',namen[x], 'student met de naam ', x)
        else:
            print('Er zijn',namen[x], 'studenten met de naam ', x)

namen()