reaisDigitado = float(input("Digite o valor que deseja converter R$ "))

def mostrar_menu():
        print("================")
        print("1 - Dólar")
        print("2 - Euro")
        print("3 - Libra")
        print("4 - Lene")
while True:
        mostrar_menu()
        opcao = int(input("Digite uma opção: "))
        

        match opcao:
            case 1:
                reais_dolar = reaisDigitado / 5.18
                print(f"{reaisDigitado} reais = {reais_dolar:.2f} Dólar")
                break
            case 2:
                reais_euro = reaisDigitado / 5.88
                print(f"{reaisDigitado} reais = {reais_euro:.2f} Euro")
                break
            case 3:
                reais_libra = reaisDigitado / 6.82
                print(f"{reaisDigitado} reais = {reais_libra:.2f} Libras")
                break
            case 4:
                reais_lene = reaisDigitado * 0.0318
                print(f"{reaisDigitado} reais = {reais_lene:.2f} Lenes")
                break
            case _:
                print("Opção digitada inválida!")
            
