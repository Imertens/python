getallen = [1,18,63,-73,-4]

def kwadraten_som():

    return sum(i*i for i in getallen if i > 0)

print(kwadraten_som())