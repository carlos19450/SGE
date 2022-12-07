print("Bienvenido a la pizzeria Bella Napoli.")
tipo = input("Introduce el tipo de pizza \n1.Vegetariana\n2.No vegetariana\nIntroducir: ")
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n1.Pimiento\n2.Tofu\n")
    ingrediente = input("Introduce un ingrediente: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n 1.Pimiento\n2.Tofu\n")
    ingrediente = input("Introduce un ingrediente: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")