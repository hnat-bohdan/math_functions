import math
def mean_a(a, b):
    return (a + b) / 2

def mean_g(a, b):
    if a > 0 and b > 0:
        return math.sqrt(a * b)
    # per le progressioni geometriche con valori negativi
    if a < 0 and b < 0:
        return -math.sqrt(a * b)
    raise ValueError("I valori per la media geometrica devono essere entrambi positivi o entrambi negativi.")
def next_value_a(a, b):

    """
    Calcola il prossimo valore nella sequenza aritmetica del tipo: ..., a, b, valore desiderato.
    Se vuoi trovare il prossimo valore da parte sinistra cambia a e b di posto.
    
    """
    return 2*b - a

def next_value_g(a, b):
    """
    Calcola il prossimo valore nella sequenza geometrica di tipo: ..., a, b, valore desiderato.
    Se vuoi trovare il prossimo valore da parte sinistra cambia a e b di posto.
    
    """
    return b**2 / a

def math_function(func_type: str, x: list[float], y: list[float], xi: float, precision: int) -> float:
    #scelta delle funzioni per trovare le medie per x e y 
    match func_type:
            case "linear":
                mean_x = mean_a
                mean_y = mean_a
            case "exponential":
                mean_x = mean_a
                mean_y = mean_g
            case "logarithmic":
                mean_x = mean_g
                mean_y = mean_a
            case "power":
                mean_x = mean_g
                mean_y = mean_g

    #ordinamento dei punti in modo crescente in basea a x
    # perché altrimenti non funziona hhaha
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
        y[0], y[1] = y[1], y[0]

    #calcolo dell'intervallo iniziale
    if xi > max(x) or xi < min(x):
        going_right: bool = abs(xi - x[1]) < abs(xi - x[0])

        #scelta delle funzioni per trovare i prossimo valori per x e y
        match func_type:
            case "linear":
                next_value_x = next_value_a
                next_value_y = next_value_a
            case "exponential":
                next_value_x = next_value_a
                next_value_y = next_value_g
            case "logarithmic":
                next_value_x = next_value_g
                next_value_y = next_value_a
            case "power":
                next_value_x = next_value_g
                next_value_y = next_value_g


        while xi > max(x) or xi < min(x):
            if going_right:
                tx = next_value_x(x[0], x[1])
                ty = next_value_y(y[0], y[1])
                # x[0] = x[1]
                # y[0] = y[1]
                x[1] = tx
                y[1] = ty
            else:
                tx = next_value_x(x[1], x[0])
                ty = next_value_y(y[1], y[0])
                # x[1] = x[0]
                # y[1] = y[0]
                x[0] = tx
                y[0] = ty
    #calcolo
    while (abs(y[0]- y[1]) > 10 ** (-precision)):
        tx = mean_x(x[0], x[1])
        ty = mean_y(y[0], y[1])
        if xi < tx:
            x[1] = tx
            y[1] = ty
        else:
            x[0] = tx
            y[0] = ty

    return round(mean_y(y[0], y[1]), precision)

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
        match i:
            case 0: #"linear":
                pass
            case 1: #"exponential":
                pass
            case 2: #"logarithmic":
                pass
            case 3: #"power":
                pass

        x.append(xj)
        y.append(yj)

    # x per cui vogiamo trovare il risultato
    SPECIAL_VALUES = {
        "e": math.e,
        "pi": math.pi,
        "sqrt2": math.sqrt(2)
    }
    print(f"Puoi inserire un valore speciale per x: {SPECIAL_VALUES}")

    xi = math.inf
    while xi == math.inf:
        xi = input(f"Inserisci il valore di x per cui calcolare la funzione\n")
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
    x = [-1, -3]
    y = [4, 12]
    print(f"x: {x}")
    print(f"y: {y}")

    # x per cui vogliamo trovare il risultato
    xi = -500
    print(f"xi: {xi}") 

    # tipo di funzione: linear, exponential, logarithmic, power
    # cambi valore di i:    0         1           2          3
    i = 0
    func_type = ("linear", "exponential", "logarithmic", "power")
    print(f"Funzione: {func_type[i]}")
    
    #precisione: a quante cifre dopo la virgola deve essere approsimato il risultato
    precision = -1
    if precision > 0:
        print(f"Precisione: {precision} cifre dopo la virgola")
    else:
        print(f"Precisione: fino a {10 ** (-precision)}")
    result = math_function(func_type[i], x, y, xi, precision)
    print(f"Result: {result}")
    print("-"*15)

    #oppure input manuale
    result = math_function(*input_data())
    print("-"*15)

    print(f"Result: {result}")
