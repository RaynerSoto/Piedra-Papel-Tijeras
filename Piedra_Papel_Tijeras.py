import random
def game():
    juego = {
        "piedra": "papel",
        "papel": "tijeras",
        "tijeras": "piedra"
    }
    listado = ["piedra", "papel", "tijeras"]
    valor = random.randint(0, 2)
    eleccion = listado[valor]
    print('Hora de jugar al piedra, papel y tijeras')
    valor = input()
    if juego.get(valor.lower(),
                 '') != '':  # Esta validación no es eficiente, pero no he podido utilizar try/catch ya que no se ha aprendido
        if juego[valor.lower()] == eleccion:
            print(f"Gana computadora ya que {eleccion} le gana a {valor}")
        elif juego[eleccion] == valor:
            print(f"Gana el jugador ya que {valor} le gana a {eleccion}")
        else:
            print(f'Empate ya que ambos obtuvieron {eleccion}')
    else:
        print('No es una opción válida')
