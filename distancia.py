distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da viagem em km/h: "))

tempo = distancia / velocidade

print(f"Para percorrer {distancia} km a uma velocidade média de {velocidade} km/h, levará aproximadamente {tempo:.2f} horas.")