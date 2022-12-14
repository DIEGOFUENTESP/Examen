multi3=0
for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        multi3=multi3+1
print("Cantidad de valores ingresados múltiplos de 3 :" , multi3)