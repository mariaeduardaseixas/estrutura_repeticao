# 2. Monitor de Temperatura de Servidor
# Monitorar um valor constante e agir caso ultrapasse o limite.

# Lógica: Implementar um loop que "escuta" um sensor (valor manual) até que o sistema seja desligado.

# Regra: Temperatura limite do servidor: 80 ºC

# Resultado Esperado: Alerta de "Resfriamento ativado".


while True:
    monitor_valor = float(input("Digite a temperatura do servidor: "))

    if monitor_valor < 80:
        print("valor da temperatura adequada")
    elif monitor_valor == 80:
        print("Cuidado o valor está se aproximando")
    else:
        print("Alerta de resfriamento ativado")
    break