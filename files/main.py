import random
import hangman_words
import hangman_art
import os

os.system('clear')

word_list = hangman_words.word_list
stages = hangman_art.stages
word = random.choice(word_list)
print(hangman_art.logo)

resposta = []
letras_usadas = []
for palavra in range(len(word)):
    resposta += "_"

final_do_jogo = False
lifes = 6

while not final_do_jogo:
    letra = input("Adivinhe uma letra: ").lower()
    os.system('clear')
    if letra not in letras_usadas:
        for position in range(len(word)):
            index = word[position]
            if index == letra:
                resposta[position] = index
                letras_usadas.append(letra)
        print(f"{' '.join(resposta)}")
    else:
        lifes -= 1
        print("Essa letra já foi utilizada!")
        print(f"Tentativas restantes: {lifes}")
    if letra not in word:
        lifes -= 1
        print("Essa letra não está na palavra")
        print(f"Tentativas restantes: {lifes}")
        if lifes == 0:
            final_do_jogo = True
            print("Você perdeu!")
            print(f"A palavra selecionada era: {word}")
    if "_" not in resposta:
        final_do_jogo = True
        print("Você venceu")
    print(stages[lifes])
