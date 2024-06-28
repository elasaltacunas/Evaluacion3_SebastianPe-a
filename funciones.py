import csv
def menu():
    print("Menu de opciones")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Vender producto")
    print("4. Salir")
    global opcion
    opcion = input("Elija una opcion: ")

def agregarproducto():
    print("Agregar producto")
    print("1. Agregar producto")
    print("2. Leer inventario")
    print("3. clasificar productos y exportar productos")   
    print("4. Salir")   
    opcion = input("Elija una opcion: ")
    

def agregar_inventario():
    print("\nAgregar producto")
    id = int(input("ID del producto: ")) 
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria del producto:\n 1. Electronica\n 2.Textil\n 3. Calzado")
    if categoria == "1":
        categoria = "Electronica"
    elif categoria == "2":
        categoria = "Textil"
    elif categoria == "3":
        categoria = "Calzado"
        precio = float(input("ingrese el Precio del producto: "))
        id = id + 1
        print(f"El producto {nombre}, Categoria {categoria} con precio {precio} se ha agregado correctamente")
        with open("inventario.csv", 'a', newline='') as inventario:
            escritor = csv.writer(inventario)
            escritor.writerow([id, nombre, categoria, precio])

def leer_inventario():
    print("\nLeer inventario de productos")
    with open("inventario.csv", 'r') as inventario:
        leer_archivo = csv.reader(inventario)
        print("ID Nombre Categoria Precio")
        for now in leer_archivo:
            print(now)

def clasificar_productos():
    print("\nClasificar productos")
    with open("inventario.csv", 'r') as inventario:
        leer_archivo = csv.reader(inventario)
        for now in leer_archivo:
            if now[2] == "Electronica":
                with open("Electronica.csv", 'a', newline='') as electronica:
                    escritor = csv.writer(electronica)
                    escritor.writerow(now)
            elif now[2] == "Textil":
                with open("Textil.csv", 'a', newline='') as textil:
                    escritor = csv.writer(textil)
                    escritor.writerow(now)
            elif now[2] == "Calzado":
                with open("Calzado.csv", 'a', newline='') as calzado:
                    escritor = csv.writer(calzado)
                    escritor.writerow(now)
    print("Los productos se han clasificado correctamente") 

while True:
    menu()
    if opcion == "1":
        agregarproducto()
    if opcion == "1":
            agregar_inventario()
    elif opcion == "2":
            leer_inventario()
    elif opcion == "3":
            clasificar_productos()
    elif opcion == "4":
            break
