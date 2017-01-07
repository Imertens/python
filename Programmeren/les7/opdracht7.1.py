def aantal():
    aantal = abs(int(input("Hoeveel personen gaan er mee op reis? ")))
    return aantal


def kosten():
    kosten = 4356 / aantal()
    return kosten

try:
    print('Dit kost', kosten(), 'euro per persoon.')
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except:
    print("Onjuiste invoer")