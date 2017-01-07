eindbestemmingFile = open('eindbestemming.txt')
oudeindFile = eindbestemmingFile.readlines()
eindbestemmingFile.close()

geanuleerdeFile = open('geanuleerde.txt')
oudgeanuleerde = geanuleerdeFile.readlines()
geanuleerdeFile.close()

geanuleerdeList = []
eind = []

for geanuleerde in oudgeanuleerde:
    geanuleerdeList.append(geanuleerde.rstrip().split(': ')[1])

for bestemming in oudeindFile:
    nieuwbestemming = bestemming.rstrip().split(' - ')[1]
    if(geanuleerdeList.count(nieuwbestemming) == 0):
        eind.append(bestemming)

nieuweindFile = open('nieuweeindbestemming.txt', 'w')
nieuweindFile.writelines(eind)
nieuweindFile.close()