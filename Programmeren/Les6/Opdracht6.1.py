cijfers = {'Hans':7,'Piet':10,'Henk':9,'jan':9.5,'Henkje':7.9,'Bart':8.9,'David':9.1}
cijfers = {(key):float(value) for key,value in cijfers.items()}
for (key,value) in cijfers.items():
    if value >= 9:
        print(key,value)