v1 = (1, 2, 3)
v2 = (-1, 0, 2)
product = 0
for i in range(len(v1)):
    product += v1[i] * v2[i]
print("El producto de los vectores" + str(v1) + " y " + str(v2) + " es " + str(product))