palabra = input("Introduce una palabra: ")
palabraInvertida = palabra
palabra = list(palabra)
palabraInvertida = list(palabraInvertida)
palabraInvertida.reverse()
if palabra == palabraInvertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")