import time
import random

# função para obter a temperatura atual
def get_temperature():
    # simulando a obtenção da temperatura de um sensor
    return random.uniform(18.0, 30.0)

# loop principal do programa
while True:
    # obtém a temperatura atual
    temperature = get_temperature()

    # exibe a temperatura atual
    print(f"Temperatura atual: {temperature:.2f}°C")

    # verifica se a temperatura está fora do intervalo desejado (20 a 25 graus Celsius)
    if temperature < 20.0:
        print("A temperatura está abaixo do limite mínimo!")
    elif temperature > 25.0:
        print("A temperatura está acima do limite máximo!")

    # espera 5 segundos antes de verificar a temperatura novamente
    time.sleep(5)
