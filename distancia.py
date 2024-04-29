nome = input("Digite o nome do motorista: ")

distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da viagem em km/h: "))

tempo = distancia / velocidade

# Exibir o resultado
print(f"{nome}, o tempo estimado para percorrer {distancia} km a {velocidade} km/h é de {tempo:.2f} horas.")