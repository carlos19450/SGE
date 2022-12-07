palabra = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    cont = 0
    for letra in palabra:
        if letra == vocal:
            cont += 1
    print("La vocal " + vocal + " aparece " + str(cont) + " veces")