"""
Projeto 02 – Jogo Jokenpô
Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
programa que jogue pedra, papel e tesoura (Jokenpô) com você.
O programa tem que:
• Permitir que eu decida quantas rodadas iremos fazer;
• Ler a minha escolha (Pedra, papel ou tesoura);
• Decidir de forma aleatória a decisão do computador;
• Mostrar quantas rodadas cada jogador ganhou;
• Determinar quem foi o grande campeão de acordo com a quantidade de 
vitórias de cada um (computador e jogador);
• Perguntar se o Jogador quer jogar novamente, se sim inicie, volte a escolha 
de quantidade de rodadas, se não, finalize o programa.

"""
from random import randint
from time import sleep

JOKENPO = ["pedra", "papel", "tesoura"]
flag = True
print("""======== JOKENPÔ GAME ========""")
while flag:
    # Variáveis para contar a pontuação
    pontosJogador = 0
    pontosAi = 0

    rodadas = int(input("Quantas rodadas deseja jogar? "))
    # Menu do jogo
    for r in range(1, rodadas + 1):      
        print(f'ROUND {r}', end="")
        for i in range(3):
            print(".", end="")
            sleep(0.2)
        print("\nFIGHT!!")

        print("""-----------
[1] - PEDRA ✊
[2] - PAPEL ✋
[3] - TESOURA ✌
-----------""")
        while True:
            # Entrada do jogador
            jJogada = int(input("Qual é a sua jogada? "))

            # Alterando a escolha numérica pela string representante
            if jJogada == 1:
                jJogada = JOKENPO[0]
                break
            elif jJogada == 2:
                jJogada = JOKENPO[1]
                break
            elif jJogada == 3:
                jJogada = JOKENPO[2]
                break
            else:
                print("Opção Inválida!")

        print("\nJO..", end="")
        sleep(0.3)
        print("KEN..", end="")
        sleep(0.3)
        print("PÔ\n")
        sleep(0.4)

        # Escolha randômica de jogo pela AI
        aiJogada = JOKENPO[randint(0, 2)]

        # Exibe qual foi o jogo
        print(f'Você: {jJogada.upper()} X Eu: {aiJogada.upper()}')

        # Apuração da jogada
        pontoMeu = '  - Ponto meu! 🤣 -'
        pontoSeu = '  - Ponto seu! 😪 -'
        pontoEmpate = '  - EMPATE! 😮 -'
        if jJogada == JOKENPO[0] and aiJogada == JOKENPO[2]:
            pontosJogador += 1
            print(f'{jJogada.upper()} ganha de {aiJogada.upper()}')
            print(pontoSeu)
        elif aiJogada == JOKENPO[0] and jJogada == JOKENPO[2]:
            pontosAi += 1
            print(f'{aiJogada.upper()} ganha de {jJogada.upper()}')
            print(pontoMeu)
        elif jJogada == JOKENPO[1] and aiJogada == JOKENPO[0]:
            pontosJogador += 1
            print(f'{jJogada.upper()} ganha de {aiJogada.upper()}')
            print(pontoSeu)
        elif aiJogada == JOKENPO[1] and jJogada == JOKENPO[0]:
            pontosAi += 1
            print(f'{aiJogada.upper()} ganha de {jJogada.upper()}')
            print(pontoMeu)
        elif jJogada == JOKENPO[2] and aiJogada == JOKENPO[1]:
            pontosJogador += 1
            print(f'{jJogada.upper()} ganha de {aiJogada.upper()}')
            print(pontoSeu)
        elif aiJogada == JOKENPO[2] and jJogada == JOKENPO[1]:
            pontosAi += 1
            print(f'{aiJogada.upper()} ganha de {jJogada.upper()} 🤣')
            print(pontoMeu)
        elif aiJogada == jJogada:
            print(pontoEmpate)

        # Placar
        print("\n---------------")
        print("     PLACAR    ")
        print("---------------")
        print(f'Você: {pontosJogador} x Eu: {pontosAi}')
        print("---------------\n")

    # Mostra quem venceu
    print("""================
Resultado Final:
================""")
    if pontosJogador > pontosAi:
        print("VOCÊ VENCEU ESSA\nPARTIDA! 👏👏😒\n")
    elif pontosAi > pontosJogador:
        print("EU VENCI! HAHA 🤣\n")
    else:
        print("EMPATAMOS! 🙄")

    # Pergunta se é para jogar de novo
    while True:
        continuar = input("Deseja jogar de novo? [S/N] ").lower()[0]
        if continuar == "s":
            break
        elif continuar == "n":
            if pontosJogador > pontosAi:
                print("\nFicou com medo da revanche, éé?! 🤭\n")
            elif pontosAi > pontosJogador:
                print("\nGGWP! haha Mais sorte\nda próxima vez! 😎\n")
            else:
                print("\nNa próxima a gente vê quem ganha, então! 😆\n")
            flag = False
            break
        else:
            print("Opção inválida!")