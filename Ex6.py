reaisDigitado = float(input("Digite o valor que deseja converter R$ "))

reais_dolar = reaisDigitado / 5.18
reais_euro = reaisDigitado / 5.88
reais_libra = reaisDigitado / 6.82
reais_lene = reaisDigitado * 0.0318

while True:
    print("================")
    print("1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Lene")
    opcao = int(input("Digite uma opção: "))
    
    match opcao:
        case 1:
            print(f"{reaisDigitado} reais = {reais_dolar:.2f} Dólar")
            break
        case 2:
            print(f"{reaisDigitado} reais = {reais_euro:.2f} Euro")
            break
        case 3:
            print(f"{reaisDigitado} reais = {reais_libra:.2f} Libras")
            break
        case 4:
            print(f"{reaisDigitado} reais = {reais_lene:.2f} Lenes")
            break
        case _:
            print("Opção digitada inválida!")
            