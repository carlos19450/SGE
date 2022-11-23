nombreProducto = input("Introduce el nombre del producto: ")
precioProducto = float(input("Introduce el precio del producto: "))
unidadesProducto = int(input("Introduce el numero de unidades: "))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = nombreProducto, unidades = unidadesProducto, precio = precioProducto, total = unidadesProducto * precioProducto))