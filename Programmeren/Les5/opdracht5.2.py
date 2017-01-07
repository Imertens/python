lijst = eval(input("Geef lijst met minimaal 10 strings: "))
lijst2 = []

for string in lijst:
    if len(string) == 4:
        lijst2.append(string)


print(lijst2)