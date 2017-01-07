import datetime

def tijd():
    vandaag = datetime.datetime.today()
    return vandaag.strftime("%a %d %b %Y, %H:%M:%S")

x = 0
while x < 5:
    hardloper = input('Voer de naam van de loper in: ')
    record = str(tijd()) + ', ' + hardloper + "\n"
    with open("hardlopers.txt", "a") as myfile:
        myfile.write(record)
    x += 1
