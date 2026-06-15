def potencia(x, y):
    if y == 0:
        return 1
    
    resultado = 1
    for i in range(y):
        resultado *= x
    
    return resultado


x = int(input("Digite a base (x): "))
y = int(input("Digite o expoente (y): "))

resultado = potencia(x, y)
print(f"{x}^{y} = {resultado}")