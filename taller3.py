opcion=100

print("Producto: ")
print("*****************\n")

print("1.RESGISTRAR")
print("2.Ver")
print("3.Ingresar")
print("4.Eliminar el ultimo producto de la lista")
print("0.SALIR\n")

productos=[]
while opcion != 0:
    opcion=int(input("DIGITA UNA OPCION: "))
    if opcion==1:
        producto=input("Digite el nombre del Producto a registrar: ")
        productos.append(producto)
    elif opcion==2:
        print(productos)
    elif opcion==3:
        producto=input("Digite el nombre del Producto a registrar: ")
        productos.append(producto)
    elif opcion==4:
        productos.pop()
        print(productos)
    else:
        print("Opcion no valida")   