import random

def jogar():
    print("----------------------------------")
    print("Bem vindos ao jogo de adivinhação!")
    print("----------------------------------")

    numero_secreto = random.randrange(1,101) # random.randrange gera número aleatorio int em um intervalo de (x até x-1)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Escolha o nível de dificuldade!")
    print("Fácil (1) Médio (2) Difícil (3)")
    nivel = int (input("Nível:"))

    while(nivel <1 or nivel >3): # para aceitar apenas os número válidos (1,2,3)
        print("Nível inválido!")
        print("Escolha o nível de dificuldade!")
        print("Fácil (1) Médio (2) Difícil (3)")
        nivel = int (input("Nível:"))
    if(nivel == 1):
        print("Nível Fácil")
        total_tentativas = 10
    elif(nivel == 2):
        print("Nível Médio")
        total_tentativas = 7
    elif(nivel == 3):
        print("Nível Difícil")
        total_tentativas = 4

    # "for in range", muda o numero de rodadas automatico em um intervalo de x tentativas
    for rodada in range(1, total_tentativas +1 ):
        print( "Rodada {} de {}".format(rodada, total_tentativas))
        tentativa_str = input("Digite um número entre 1 e 100: ")
        tentativa = int(tentativa_str)

        acertou = tentativa == numero_secreto
        maior   = tentativa  > numero_secreto
        menor   = tentativa  < numero_secreto

        if(tentativa < 1 or tentativa > 100):
            print("Atenção, numero inválido!")
            continue

        if (acertou):
            print("Parabéns, você acertou e fez {} pontos". format(pontos))
            break
        else:
            if(maior):
                print("Você errou, você digitou um numero maior")
            elif(menor):
                print("Você errou, você digitou um numero menor")

                pontos_perdidos = abs(numero_secreto - tentativa) # abs = absoluto, ou seja, valor modulado
                pontos = pontos - pontos_perdidos

    print("Fim de jogo")
    print("O número secreto era {}". format(numero_secreto))
    print("Sua pontuação foi de {} pontos". format(pontos))

if(__name__ == "__main__"):
    jogar()