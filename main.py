import json
import random

def odenamiento_bublesort(lista_ordenar):

    for i in range(len(lista_ordenar)):
            for j in range(i +1, len(lista_ordenar)):
                if lista_ordenar[i] < lista_ordenar [j]:
                    numero_movido = lista_ordenar[i]
                    lista_ordenar[i] = lista_ordenar[j]
                    lista_ordenar[j] = numero_movido
    return lista_ordenar

def menu_principal():
    print("======= Juego Ahorcado Menu =======")
    print("1. Jugar")
    print("2. Puntajes")
    print("3. Salir")

def obtener_idioma():
    while True:
        print("======= Escoja el idioma de la palabra =======")
        print("ES. para ESPAÑOL")
        print("EN. para INGLES")
        idioma = input("Ingrese El Idioma: ").lower()
        if idioma == "es":
            break
        elif idioma == "en":
            break
        else:
            print("Opcion no valida.")
    return idioma

def importar_palabras_lista(data):
    palabras_es = []
    palabras_en = []

    for palabra in data["ahorcado"]:
        palabras_es.append(palabra["ES"])
        palabras_en.append(palabra["EN"])
    return palabras_es, palabras_en

def palabra_random(lista_es, lista_en):
    numero_random = random.randint(0, 9)

    for i in range(len(lista_es)):
        palabra_random_es = lista_es[numero_random]

    for i in range(len(lista_en)):
        palabra_random_en = lista_en[numero_random]
    return palabra_random_es, palabra_random_en


def mostrar_puntajes():
    lista_nombres = []
    lista_puntajes = []
    
    for palabra in scores["puntaje"]:
        lista_nombres.append(palabra["NOMBRE"])
        lista_puntajes.append(palabra["PUNTAJE"])

    # Inicializar a None para los primeros 5 puntajes
    top_nombres = [None] * 5
    top_puntajes = [None] * 5
    
    # Ordenar los puntajes usando el algoritmo de burbuja
    for i in range(len(lista_puntajes)):
        for j in range(0, len(lista_puntajes)-i-1):
            if lista_puntajes[j] is not None and lista_puntajes[j+1] is not None and lista_puntajes[j] < lista_puntajes[j+1]:
                # Intercambiar los puntajes
                lista_puntajes[j], lista_puntajes[j+1] = lista_puntajes[j+1], lista_puntajes[j]
                # Intercambiar los nombres
                lista_nombres[j], lista_nombres[j+1] = lista_nombres[j+1], lista_nombres[j]
    
    # Obtener los primeros 5 puntajes
    for i in range(min(5, len(lista_puntajes))):
        top_nombres[i] = lista_nombres[i]
        top_puntajes[i] = lista_puntajes[i]
    
    # Crear el mensaje con los top 5
    mensaje = "\n\n\n==========TOP 5 MEJORES==========\n\n"
    for i in range(5):
        if top_puntajes[i] is not None:
            mensaje += f"{i+1}. {top_nombres[i]}: {top_puntajes[i]} PTS\n"
    
    return mensaje

def guardar_puntaje(nombre, puntaje, lista):
    nuevo_puntaje = {"NOMBRE": nombre, "PUNTAJE": puntaje}
    lista.append(nuevo_puntaje)

    file = open("scores.json", "w")
    json.dump(scores, file, indent=4)
    file.close()



def juego(palabra):
    contador_vidas = 6
    contador_puntos = 0
    palabra_oculta = ["_"]  * len(palabra)
    letras_adivinadas = set()
    
    while True:
        palabra_oculta_str = ""
        
        # el jugador pone una letra
        letra = input("Ingresa una letra: ").lower()
        
        # si pone mas de una letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        if letra in letras_adivinadas:
            print("letra fue ya utilizada")
            continue
        letras_adivinadas.add(letra)
        
        # Si la letra no esta resta 1 al contador y si no sigue.
        if letra not in palabra:
            contador_vidas -= 1
            print(f"La letra {letra} no está en la palabra.")
        else:
            print("Muy bien!, Adivinaste una letra")
            contador_letras = palabra.count(letra)
            contador_puntos += contador_letras

        # For que va construyendo la palabra oculta.
        for i in range(len(palabra_oculta)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
        for letra in palabra_oculta:
            palabra_oculta_str += letra

        
        # Gano el juego.
        if palabra == palabra_oculta_str:
            contador_puntos = len(palabra)
            print(f"GANASTE!, conseguiste {contador_puntos} puntos")
            break
        elif contador_vidas == 6:
            print("""
         ------
         |    |
              |
              |
              |
              |
        ---------
        """)

        elif contador_vidas == 5:
            print("""
            ------
            |    |
            O    |
                 |
                 |
                 |
            ---------
            """)

        elif contador_vidas == 4:
            print("""
            ------
            |    |
            O    |
            |    |
                 |
                 |
            ---------
            """)


        elif contador_vidas == 3:
            print(  """
            ------
             |    |
             O    |
            /|    |
                  |
                  |
            ---------
            """)


        elif contador_vidas == 2:
            print(  """
            ------
             |    |
             O    |
            /|\   |
                  |
                  |
            ---------
            """)        


        elif contador_vidas == 1:
            print("""
            ------
             |    |
             O    |
            /|\   |
            /     |
                  |
            ---------
            """)


        elif contador_vidas == 0:
            print(  """
            ------
             |    |
             O    |
            /|\   |
            / \   |
                  |
            ---------
            """)
            print(f"GAME OVER!, conseguiste {contador_puntos} puntos")
            print(f"La palabra era: {palabra}")
            break

        print("Palabra actual" ,palabra_oculta_str)
        print ("las letras utilizadas son: ", list(letras_adivinadas))
        print(f"Intentos Restantes: {contador_vidas}")
    return contador_puntos

# Abrimos el data.json y lo pasa a un dicionario.
file = open("data.json", "r")
data = json.load(file)
file.close()

#Abrimos el scores.json y lo pasa a un dicionario
file = open("scores.json", "r")
scores = json.load(file)
file.close()



lista_es, lista_en = importar_palabras_lista(data)
puntaje_guardar = 0



while True:
    menu_principal()
    opcion = input("Ingrese la opcion: ")

    if opcion == "1":
        palabra_es, palabra_en = palabra_random(lista_es, lista_en)
        idioma = obtener_idioma()
        if idioma == "es":
            puntaje_guardar = juego(palabra_es)
            nombre_guardar = input("Ingrese su nombre: ")
            guardar_puntaje(nombre_guardar, puntaje_guardar, scores["puntaje"])
            print("Puntaje Guardado!")
        elif idioma == "en":
            puntaje_guardar = juego(palabra_en)
            nombre_guardar = input("Ingrese su nombre: ")
            guardar_puntaje(nombre_guardar, puntaje_guardar, scores["puntaje"])
            print("Puntaje Guardado!")
        else:
            print("Opcion no valida.")
    elif opcion == "2":
        print(mostrar_puntajes())
    elif opcion == "3":
        break
    else:
        print("Opcion no valida.")

