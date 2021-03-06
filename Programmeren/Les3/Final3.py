def standaardprijs(afstandKM):
    grensafstand = 50
    ritlangkostenkm = 0.6
    ritkortkosten = 0.8
    ritlangkosten = 15
    if afstandKM >= grensafstand:
        prijs=(float(afstandKM * ritlangkostenkm + ritlangkosten))
    elif afstandKM <=0:
        print('De ingevoerde waarde is niet correct')
        quit()
    else:
        prijs = (float(afstandKM * ritkortkosten))
    return prijs

def ritprijs(leeftijd, heeftWeekendKorting, afstandKM):
    allesbonus = 0.65
    weekendbonus = 0.6
    leeftijdbonus = 0.7

    heeftLeeftijdsKorting = leeftijd >= 65 or leeftijd <= 12

    totaalprijs = float(standaardprijs(afstandKM))
    if heeftWeekendKorting:
        if heeftLeeftijdsKorting:
            totaalprijs = float(standaardprijs(afstandKM) * allesbonus)
        else:
            totaalprijs = float(standaardprijs(afstandKM) * weekendbonus)
    else:
        if heeftLeeftijdsKorting:
            totaalprijs = float(standaardprijs(afstandKM) * leeftijdbonus)

    return totaalprijs



afstandKM = float(input('Wat is de afstand van de rit in KM? :'))
standaardprijs(afstandKM)
leeftijd = int(input('Voer je leeftijd in :'))
heeftWeekendKorting = input('Is de rit in het weekend? :')=='ja'

print('Deze rit kost', ritprijs(leeftijd,heeftWeekendKorting,afstandKM),'euro.')




