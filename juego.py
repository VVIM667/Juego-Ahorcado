from random import *
from os import system
def limpiar():
    system("cls")

def palabra_al_azar():
    peliculas = [
        "toy story", "up", "el rey leon", "aladdin", "la bella y la bestia",
        "blanca nieves", "pinocho", "dumbo", "bambi", "cenicienta",
        "peter pan", "la sirenita", "la bella durmiente", "tarzan",
        "hercules", "mulan", "pocahontas", "el jorobado de notre dame",
        "atlantis", "lilo y stitch", "buscando a nemo", "los increibles",
        "cars", "ratatouille", "wall-e", "enredados", "valiente",
        "intensamente", "zootopia", "moana", "coco", "ralph el demoledor",
        "frozen", "frozen ii", "gran heroe 6", "malefica", "el libro de la selva",
        "la dama y el vagabundo", "robin hood", "el zorro y el sabueso",
        "bernardo y bianca", "basil el raton superdetective", "la espada en la piedra",
        "merlin el encantador", "aventuras en el mundo de oz", "taron y el caldero magico",
        "oliver y su pandilla", "la familia del futuro",
        "winnie the pooh", "el planeta del tesoro", "zafarrancho en el rancho", "tierra de osos"
    ]
    palabra = choice(peliculas)
    return palabra

palabra_secreta_elegida = palabra_al_azar()

def mostrar_palabra_secreta_random(palabra_secreta_elegida, letras_descubiertas):
    print(f"Cantidad de letras: {len(palabra_secreta_elegida)}")
    
    for letra in palabra_secreta_elegida:
        if letra in letras_descubiertas or letra == ' ':
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()  # Para nueva linea al final de la palabra mostrada

def pedir_letra():
    letra="X"
    abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 
    ]
    while letra not in abecedario:
        print()
        letra=input("Da una letra valida (A-Z): ")
        print()
        letra = letra.lower()
    return letra

letras_descubiertas=[]
letras_erroneas=[]

def turno():  # al momento de llamar la funcion hay que mandar llamar la funcion de pedir letra
    vidas = 6

    while vidas > 0:
        limpiar()

        print(f"Vidas: {vidas}")
        mostrar_palabra_secreta_random(palabra_secreta_elegida, letras_descubiertas)
        if letras_erroneas:
            print("Letras incorrectas:", ", ".join(letras_erroneas))

        letra = pedir_letra()

        if letra not in palabra_secreta_elegida:
            vidas -= 1
            letras_erroneas.append(letra)

        elif letra in palabra_secreta_elegida:
            letras_descubiertas.append(letra)
        
        if set(letras_descubiertas) == set(palabra_secreta_elegida.replace(" ", "")):
            limpiar()
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta_elegida}")
            print(f"Te llevo {6 - vidas} intentos")
            break

    if vidas == 0:
        print(f"Te quedaste sin vidas :( la palabra era: {palabra_secreta_elegida}. GAME OVER")

# Ejecucion del juego
turno()
