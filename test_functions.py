from  functions import *
FUNC_TYPE = ("linear", "exponential", "logarithmic", "power")
precision = 3

print("Le funzioni fatte in classe")
print("-"*15)
x = [2, 4]
y = [7, 11]
xi = math.pi
print(f"Funzione: {FUNC_TYPE[0]}")
print(f"x: {x}")
print(f"y: {y}")
print(f"xi: {xi}")
result = math_function(FUNC_TYPE[0], x, y, xi, precision)
print("-"*15)
print(f"Result: {result}")

print("-"*15)
x = [2, 8]
y = [10, 42]
xi = math.pi
print(f"Funzione: {FUNC_TYPE[1]}")
print(f"x: {x}")
print(f"y: {y}")
print(f"xi: {xi}")
result = math_function(FUNC_TYPE[1], x, y, xi, precision)
print("-"*15)
print(f"Result: {result}")
print("E' diverso da quello che ci è venuto in classe (circa 12) probabilmente perché abbiamo sbagliato il calcolo :)")
print("-"*15)

print("Compito per casa 🏫")
x = [4, 9]
y = [8, 27]
xi = 5
print(f"Funzione: {FUNC_TYPE[3]}")
print(f"x: {x}")
print(f"y: {y}")
print(f"xi: {xi}")
result = math_function(FUNC_TYPE[3], x, y, xi, precision)
print("-"*15)
print(f"Result: {result}")

print("-"*15)
print("Input manuale dei dati:")
result = math_function(*input_data())
print("-"*15)
print(f"Result: {result}")