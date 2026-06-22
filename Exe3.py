tamanho_arquivo = float(input("Digite o tamanho do arquivo MB: "))

velocidadeMbps = float(input("Digite a velocidade do link de Internet: "))

tempo_aproximado = (tamanho_arquivo / velocidadeMbps)

tempo_segundos = (tamanho_arquivo * 8) / velocidadeMbps
tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")


