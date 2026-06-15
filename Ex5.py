temperatura = float(input("Digite a temperatura em C° "))

def classificar_temperatura(temp):
    if temp < 0: 
        print(f"Frio extremo, temperatura {temp}°C")
    elif temp < 10:
        print(f"Frio, temperatura {temp}°C")
    elif temp < 25:
        print(f"Ameno, temperatura {temp}°C")
    elif temp < 35:
        print(f"Quente, temperatura {temp}°C")
    else:
        print(f"Muito Quente, temperatura {temp}°C")

classificar_temperatura(temperatura)