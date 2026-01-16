import math
def mean_a(a, b):
    return (a + b) / 2

def meen_g(a, b):
    return math.sqrt(a * b)

def math_function(func_type: str, x: list[float], y: list[float], xi: float, precision: int) -> float:
    #scegliamo il tipo di funzione
    match func_type:
        case "linear":
            mean1 = mean_a
            mean2 = mean_a
        case "exponential":
            mean1 = mean_a
            mean2 = meen_g
        case "logarithmic":
            mean1 = meen_g
            mean2 = mean_a
        case "power":
            mean1 = meen_g
            mean2 = meen_g

    #calcolo
    while (abs(y[0]- y[1]) > 10 ** (-precision)):
        tx = mean1(x[0], x[1])
        ty = mean2(y[0], y[1])
        if xi < tx:
            x[1] = tx
            y[1] = ty
        else:
            x[0] = tx
            y[0] = ty

    return round(mean2(y[0], y[1]), precision)


def input_data() ->  tuple[str, list[float], list[float], float, int]:
    x, y = [], []

    # tipo di funzione
    available_func_types = ("linear", "exponential", "logarithmic", "power")
    i = -1
    while i not in range(0, len(available_func_types)):
        i = int(input("Inserisci il tipo di funzione:\n 0 - linear, \n 1 - exponential,\n 2 - logarithmic,\n 3 - power:\n "))

    for j in range(2):
        print(f"Punto {j}")
        xj = float(input(f"Inserisci x[{j}]: "))
        yj = float(input(f"Inserisci y[{j}]: "))

        # controlli
        #da fare un giorno

        x.append(xj)
        y.append(yj)

    # x per cui vogiamo trovare il risultato
    SPECIAL_VALUES = {
        "e": math.e,
        "pi": math.pi,
        "sqrt2": math.sqrt(2)
    }
    print(f"Puoi inserire un valore speciale per x: {SPECIAL_VALUES.keys()}")

    xi = math.inf
    while xi < min(x) or xi > max(x):
        xi = input(f"Inserisci il valore di x per cui calcolare la funzione\n(deve essere compreso tra {min(x)} e {max(x)}):\n")
        if xi in SPECIAL_VALUES.keys():
            xi = SPECIAL_VALUES[xi]
        else:
            try:
                xi = float(xi)
            except:
                print("Valore non valido.")
        

    
    #precisione
    precision = 6
    while precision > 5:
        precision = int(input("Inserisci il numero di cifre decimali per la precisione.\nDeve essere compreso tra 0 e 5:\n "))

    return available_func_types[i], x, y, xi, precision

if __name__ == "__main__":
    #valori
    print("Esempio con valori preimpostati:")
    x = [1, 3]
    y = [4, 12]
    print(f"x: {x}")
    print(f"y: {y}")

    # x per cui vogiamo trovare il risultato
    xi = math.sqrt(2) 
    print(f"y: {xi}") 

    # tipo di funzione: linear, exponential, logarithmic, power
    # cambi valore di i:    0         1           2          3
    i = 0
    func_type = ("linear", "exponential", "logarithmic", "power")
    print(f"Funzione: {func_type[i]}")
    
    #precisione: a quante cifre dopo la virgola deve essere approsimato il risultato
    precision = 3
    print(f"Precisione: {precision} cifre dopo la virgola")
    result = math_function(func_type[i], x, y, xi, precision)
    print(f"Result: {result}")
    print("-"*15)

    #oppure input manuale
    result = math_function(*input_data())
    print("-"*15)
    print(f"Result: {result}")