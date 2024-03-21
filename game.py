import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_fails = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Seleccione la dificultad\n1 - Facil\n2 - Media\n3 - Dificil")
nivel= input(">>>")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

match nivel:
    case "1":
        vocales= "aeiouáéíóú"
        word_displayed = "".join(letter if letter in vocales else "_" for letter in secret_word)
    case "2":
        word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    case "3":
        word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

i= 0
while i<max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya ha sido adivinada
    if letter != "":
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
    
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
    
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            i+= 1
    else:
        print("Error")
        continue
 
    # Mostrar la palabra parcialmente adivinada
    letters = []
 
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    
    match nivel:
        case "1":
            word_displayed = "".join([letter if letter in vocales or letter in guessed_letters else "_" for letter in secret_word])
        case "2":
            word_displayed = secret_word[0] + "".join([letter if letter in guessed_letters else "_" for letter in secret_word[1:-1]]) + secret_word[-1]
        case "3":
            word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado {max_fails} fallos.")
    print(f"La palabra secreta era: {secret_word}")