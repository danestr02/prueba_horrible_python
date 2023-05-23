print("*"*30)
print("¡Bienvenido a El Diente de Oro!")
print("*"*30)

print("Ingrese una opción: ")
print("1.- Cotización.")
print("2.- Renunciar.")
print("3.- SALIR.")
opcion=int(input(": "))

while True:
    if opcion==1:
        carillas=0
        implantes=0
        ortodoncia=0
        print("Los tratamientos disponibles son: ")
        print("1.- Carillas Porcelana. $250000.-")
        print("2.- Implantes Dentales. $475000.-")
        print("3.- Ortodoncia Braquets. $800000.-")
        tratamiento=int(input(": "))
        if tratamiento==1:
            carillas+=1
        if tratamiento==2:
            implantes+=1
        if tratamiento==3:
            ortodoncia+=1
        print("¿Desea Agregar otro tratamiento?")
        print("1.- SI")
        print("2.- NO")
        opc=int(input(": "))
        if opc==2:
            break
        print("Ingrese el tipo de cargo que posee: ")
        print("1.- Trabajador Auxiliar.")
        print("2.- Trabajador Administrativo.")
        print("3.- Trabajador Docente.")
        cargo=int(input(": "))
        if cargo==1:
            desc=0.15
            print("Tiene un 15% de descuento en el total de su pago.")
        if cargo==2:
            desc=0.10
            print("Tiene un 10% de descuento en el total de su pago.")
        if cargo==3:
            desc=0.05
            print("Tiene un 5% de descuento en el total de su pago.")
total1=(carillas*250000) 
total2=(implantes*475000)
total3=(ortodoncia*800000)
print("-"*50)
print("\tCotización")
print("-"*50)
print("Total:")
print(f"Carillas porcelana: {total1}")
print(f"Implantes dentals: {total2}")
print(f"Ortodoncia braquets: {total3}")