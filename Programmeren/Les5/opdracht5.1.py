def seizoen(maand):
    lente = maand >= 3 and maand <=5
    herfst = maand >= 9 and maand <=11
    zomer = maand >=6 and maand <= 8
    winter = maand == 1 or maand == 2 or maand == 12

    if lente:
        print('Het is lente')
    if herfst:
        print('Het is herfst')
    if zomer:
        print('Het is zomer')
    if winter:
        print('Het is winter')

maandnummer = int(input('Welke maandnummer is het? :'))
seizoen(maandnummer)




