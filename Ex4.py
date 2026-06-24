nota1 = float(input("Digite a nota da 1ª Prova "))
nota2 = float(input("Digite a nota da 2ª Prova "))

trabalho1 = float(input("Digite a nota do 1º Trabalho "))
trabalho2 = float(input("Digite a nota do 2º Trabalho "))

media_provas = (nota1 + nota2) / 2

media_trabalhos = (trabalho1 + trabalho2) / 2

media_final = (0.8 * media_provas) + (0.2 * media_trabalhos)


print(f"Sua média nas provas foi de {media_provas:.2f}")
print(f"Sua média nos trabahlos foram {media_trabalhos:.2f}")

if media_final >= 6:
    print(f"Sua média foi {media_final:.2f} você foi Aprovado!")
else:
    print(f"Sua média foi {media_final:.2f} você foi Reprovado!")