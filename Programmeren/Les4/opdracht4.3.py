bestand = 'kaartnummers.txt'

def klanten(bestand):
    infile = open(bestand, 'r')
    content = infile.readlines()
    infile.close()

    for aantal in content:
        aantal = len(content)
    print('Deze file heeft', aantal, 'regels.')


def grootstenummer(bestand):
    infile = open(bestand)
    file = infile.readlines()
    nummers = []
    for lines in file:
        lines = lines.strip()
        splitlst = lines.split(sep=',')
        nummers.append(splitlst[0])
    maxnummer = max(nummers)
    maxregelnummer = (nummers.index(maxnummer)+1)
    infile.close
    print('Het grootste nummer is:', maxnummer, 'en dat staat op regel', maxregelnummer)


klanten(bestand)
grootstenummer(bestand)
