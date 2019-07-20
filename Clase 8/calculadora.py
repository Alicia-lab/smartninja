

print("Bienvenido a mi primera calculadora de Python.")
print("Ahora introduce los datos")
print()

op = input("Que quieres hacer (+-*/): ")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
resultado = None

# Aqui procesamos los datos

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    resultado = num1 / num2
else:
    print("No has metido una operación correcta")
    exit()

print ("El resultado de la operación es:")
print (str(num1) + "" + op + "" + str(num2) + " = " + str(resultado))
