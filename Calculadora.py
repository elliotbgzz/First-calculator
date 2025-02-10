print("---- Bienvenido a mi calculadora ----")#Salutations
print("""1. Suma
2. Resta
3. Multiplicacion
4. Division""") #Displays available options
Seleccion = int(input("Selecciona que operacion quieres realizar: "))
if (Seleccion > 0) and (Seleccion < 5): #Checks if the Selections value is within range
    Num1 = int(input("Introduce el primer numero: ")) #First number input
    Num2 = int(input("Introduce el segundo numero: ")) #Second number input
    if Seleccion == 1:
        print(f'La suma de {Num1}+{Num2} es igual a {Num1 + Num2}') #Adds the two numbers
    if Seleccion == 2:
        print(f'La resta de {Num1}-{Num2} es igual a {Num1 - Num2}') #Substracts the two numbers
    if Seleccion == 3:
        print(f'La multiplicacion de {Num1}x{Num2} es igual a {Num1 * Num2}') #Multiplies the two numbers
    if Seleccion == 4:
        print(f'La division de {Num1}/{Num2} es igual a {Num1 / Num2}') #Divides the two numbers
else:
    print("""Opcion no disponible
-------- Saliendo --------""") #Comunicates to the user that the operation selected its not available
