asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?: ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i] + " donde " + asignaturas[i] + " es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.")