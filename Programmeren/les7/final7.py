import random,csv

def menu():
    while True:
        print('1: Ik wil een nieuwe kluis')
        print('2: Ik wil mijn kluis openen')
        print('3: Ik geef mijn kluis terug')
        print('4: Ik wil weten hoeveel kluizen nog vrij zijn')
        print('5: Ik wil stoppen\n')
        try:
            keuze = int(input('Kies uw optie: '))
            if keuze == 1:
                kluisGeven()
            elif keuze == 2:
                kluisOpenen()
            elif keuze == 3:
                print('Deze keuze is nog niet beschrikbaar\n')
            elif keuze == 4:
                aantalKluizenVrij()
            elif keuze == 5:
                break
            else:
                print('Uw invoer is ongeldig\n')
        except:
            print('Uw invoer is ongeldig\n')

def kluisGeven():
    if kluisAantalCheck() == True:
        kluisOpslaan()

def kluisOpslaan():
    kluisnummer = kluisKrijgen()
    wachtwoord = maakWachtWoord()

    with open('kluizen.csv', 'a', newline='') as csvBestand:
        fieldnames = ['kluisnummer', 'wachtwoord']
        writer = csv.DictWriter(csvBestand, fieldnames=fieldnames)
        writer.writerow({'kluisnummer': kluisnummer, 'wachtwoord': wachtwoord})
    print('Uw kluisnummer is: ', kluisnummer, ' en uw wachtwoord is: ', wachtwoord,'\n')

def kluisKrijgen():
    kluisNummer = str(random.randrange(1, 13))
    while kluisNummer in openenKluizenBestand():
        kluisNummer = str(random.randrange(1, 13))
    return kluisNummer

def maakWachtWoord():
    wachtwoord = random.randint(1111, 9999)
    return wachtwoord

def kluisAantalCheck():
    with open('kluizen.csv') as csvfile:
        kluizen = [line.strip() for line in csvfile]

        if len(kluizen) >= 12:
            print('Er zijn geen kluizen vrij\n')
        else:
            return True

def kluisNummerCheck():
    with open('kluizen.csv') as csvfile:
        kluisnummers = [[line.split(None, 1)[0] for line in csvfile]]
        return(kluisnummers)

def openenKluizenBestand():
    with open('kluizen.csv','r') as csvfile:
        return dict(filter(None, csv.reader(csvfile)))

def kluisOpenen():
    invoer = input('Voer uw wachtwoord in: ')
    wachtwoorden = dict.values(openenKluizenBestand())
    if invoer in wachtwoorden:
        kluisNummer = (list(openenKluizenBestand().keys())[list(openenKluizenBestand().values()).index(invoer)])
        print('Uw kluis nummer',kluisNummer,'is geopend.\n')
    else:
        print('Het wachtwoord is incorrect\n')

def aantalKluizenVrij():
    with open('kluizen.csv') as csvfile:
        kluizen = [line.strip() for line in csvfile]
        aantal = 12 - len(kluizen)
        print('Er zijn nog',aantal,'kluizen vrij.\n')

menu()
