student = {}
materii = []
nr_materii = 4
note = []
nume = input("Numele, Prenumele elevului: ")
student.update({"Nume" : nume})
for i in range(0, nr_materii):
    materii.append(input("Materia: "))
    note.append(int(input("Nota: ")))
for a in range(0,nr_materii):
    student.update({materii[a] : note[a]})
media = (sum(note)/len(note))
print("Studentul " + student.get("Nume") + "are media " + str(media ))

for j in range(0, nr_materii):
    print(materii[j] + " : " + str(note[j] ))

