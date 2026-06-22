print("=================")

usuario = input("Digite seu nome: ")

saldo = 1000
senha_login = "@12345"

while True:
    senha = input("Digite sua senha: ")

    if senha == senha_login:
        print("Acesso Permitido!")
        break
    else:
        print("Senha incorreta!")

while True:
        print("================")
        print("1 - Consultar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = int(input("Escolha: "))

        match opcao:
                    case 1:
                        print(f"Seu saldo é R${saldo}")
                    case 2:
                        valor = float(input("Quanto depositar? "))
                        saldo += valor
                        print(f"Depositado! Novo saldo: R${saldo}")
                    case 3:
                        valor = float(input("Quanto sacar? "))
                        if valor > saldo:
                            print("Saldo insuficiente!")
                        else:
                            saldo -= valor
                            print(f"Saque realizado! Novo saldo: R${saldo}")
                    case 4:
                        print("Saindo...")
                        break