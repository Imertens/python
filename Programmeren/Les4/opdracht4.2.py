def klanten(file):
    infile=open(file)
    lines = infile.readlines()

    for line in lines:
        line=line.strip()
        klantnmr=line.split(', ')
        print(klantnmr[1],'heeft het kaart nummer:',klantnmr[0])
    infile.close()

klanten('kaartnummers.txt')