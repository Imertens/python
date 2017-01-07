def ticker():
    tickers = {}
    with open('tickersymbool.txt') as f:
        for line in f:
            (key, val) = line.rstrip("\n").split(sep=':')
            tickers[key] = val
    return tickers

def bedrijf():
    bedrijf = {}
    with open('tickersymbool.txt') as f:
        for line in f:
            (key, val) = line.rstrip("\n").split(sep=':')
            bedrijf[val] = key
    return bedrijf

def krijgTicker():
    bedrijfsNaam = input('Enter Company Name: ')
    print('Ticker Symbol: ', ticker()[bedrijfsNaam], '\n')

def krijgBedrijf():
    ticker = input('Enter Ticker Symbol: ')
    print('Company name: ', bedrijf()[ticker], '\n')

def menu():
    krijgTicker()
    krijgBedrijf()

menu()

