edad = int(input("Introduce tu edad: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else :
    precio = 10
print("El precio a pagar es: ", precio)