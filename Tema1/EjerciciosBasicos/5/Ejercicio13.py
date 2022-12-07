numeros = input("Introduce una muestra de números separados por comas: ")
numeros = numeros.split(',')
n = len(numeros)
for i in range(n):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)
sum = 0
sumsq = 0
for i in numeros:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('Media', mean, '\nDesviación típica', stdev)