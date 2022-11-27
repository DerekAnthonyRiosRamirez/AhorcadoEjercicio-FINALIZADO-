from animales import words
import random 

# Funcion para obtener la palabra random.
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word and " " in word:
        word = random.choice(words)
    return word.upper()

# Funcion principal.
def hangman():
    # Todo el codigo de abajo se ejecutara siempre y cuando no haya una interrupcion del teclado.
    try:
        word =  get_valid_word(words)
        lives = 6
        special_characteres_and_numbers = ["`", "~", "!", "¡", "@", "²", "#", "³", "$", "¤", "%", "€", "^", "¼", "&", "½", "*", "¾", "(", "‘", ")", "’", "_", "-", "¥", "=", "+", "×", "[", "{", "«", "]", "}", "»", "|", "¬", ";", ":", "¶", "'", "´", ",", "<", "ç", ".", ">", "/", "?", "¿", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        letras_usadas = set()
        word_letters = set(word)

        # Mensaje de bienvenida y presentacion de la palabra como guiones.
        print("\n" + "*" * 100)
        print("Bienvenido a mi juego del ahorcado, intenta adivinar la palabra random que se genera. \nLos guiones que veras abajo son los equivalentes a las letras que tiene la palabra. \nBuena suerte. \n\nPista: las palabras son de animales.")
        print("*" * 100)

        # Aqui muestra la palabra solo para hacer ver mas facil la funcionalidad del juego.
        # print(word)
        

        #Ciclo que acaba hasta que el usuario haya adivinado la palabra o muera.
        while len(word_letters) > 0 and lives > 0:
            print(f"\nTienes {lives} vidas")

            # Se muestran las letras adivinadas y las que faltan, tambien se muestran las letras usadas.
            word_list = [letter if letter in letras_usadas else "_" for letter in word]

            # Codigo que muestra la figura del ahorcado.
            if lives == 6:
                    print("""
                    -------------
                    | /          |
                    |/
                    |
                    |
                    |
                    """)
            elif lives == 5:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |
                    |
                    |
                    """)
            elif lives == 4:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |            | 
                    |            
                    |
                    """)
            elif lives == 3:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|   
                    |            
                    |
                    """)
            elif lives == 2:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`   
                    |            
                    |
                    """)
            elif lives == 1:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`  
                    |           ' 
                    |
                    """)

            print("\nLa palabra por adivinar: ", " ".join(word_list))
            print("Las letras que ha usado son: ", " ".join(letras_usadas))

            # Validaciones de la letra que digita el usuario.  
            letter = input("Digite una letra: ").upper()
            if letter in word_letters:
                word_letters.remove(letter)
                print("\n" + "*" * 100)
                print("Haz adivinado una letra, felicidades.")
                print("*" * 100)
                letras_usadas.add(letter)
            
            # Aqui validamos que el usuario solo pueda digitar una letra y no dos.
            # Tambien validamos que no pueda digitar numeros y caracteres especiales.
            elif letter in special_characteres_and_numbers or len(letter) > 1:
                print("\nPorfavor, digite una letra valida. \n")
            else:
                lives -= 1
                print("\nEsa letra no esta en la palabra, se le quita una vida.\n")
                
        #Aqui termina el ciclo while, teniendo dos finales: o perdiste todas tus vidas, o bien, ganaste.
        if lives == 0:
        
            print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`   
                    |           ' '
                    |
                    """)

            print("\n" + "*" * 100)
            print("Usted a perdido, gracias por participar. CABEZOOOOOOOOOON")
            print("*" * 100)
        else:
                print("\n" + "*" * 100)
                print(f"Felicidades, usted ha adivinado la palabra {word}")
                print("*" * 100)

    # Si hay una interrupcion del teclado, se muestra este mensaje y termina el programa.
    except KeyboardInterrupt:
        print("\n\nGracias por interrumpirme cabezon, bye.")

hangman()
