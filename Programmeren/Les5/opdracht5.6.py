studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]



def gemiddelde_per_student(studentencijfers):
    for num in range(0,len(studentencijfers)):
        gemiddeldPerStudent = float(sum(studentencijfers[num]) / 3 / 10)
        print(gemiddeldPerStudent,end='        ')
    return

def gemiddelde_van_alle_studenten(studentencijfers):
    totaal = 0
    for num in range(0, len(studentencijfers)):
        totaal += sum(studentencijfers[num])
    GemiddeldTotaal = float(totaal / 12 / 10)

    return GemiddeldTotaal


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
