import random
def monopolyworp():
    gooi1 = random.randrange(1,7)
    gooi2 = random.randrange(1,7)
    totaal1 = gooi1 + gooi2
    print(gooi1, '+', gooi2, '=' , totaal1)
    if gooi1 == gooi2:
        gooi3 = random.randrange(1, 7)
        gooi4 = random.randrange(1, 7)
        totaal2 = gooi3 + gooi4
        print(gooi3, '+', gooi4, '=' , totaal2, '(dubbel)')
        if gooi3 == gooi4:
            gooi5 = random.randrange(1, 7)
            gooi6 = random.randrange(1, 7)
            totaal3 = gooi5 + gooi6
            if gooi5 == gooi6:
                print(gooi5, '+', gooi6, '=', totaal3, 'Gelijk naar de gevangenis!')
            else:
                print(gooi5, '+', gooi6, '=', totaal3, '(dubbel)')

monopolyworp()