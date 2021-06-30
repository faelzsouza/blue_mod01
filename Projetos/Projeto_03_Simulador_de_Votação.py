"""
Projeto 03 – Simulador de Votação
Crie um programa que simule um sistema de votação, ele deve receber votos 
até que o usuário diga que não tem mais ninguém para votar, esse programa 
precisa ter duas funções:
A 1° Função precisa ser chamada autoriza_voto() ela vai receber como 
parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições.
A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que 
virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, 
caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela 
pode escolher de 1 a 5 (crie 3 candidatos para a votação):
1, 2 ou 3 - Votos para os respectivos candidatos
4- Voto Nulo
5 - Voto em Branco
Sua função votacao() tem que calcular e mostrar:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
Qual candidato venceu a votação.
"""
from datetime import datetime
from time import sleep

# FUNÇÕES
#-----------------------------------------------------------------------------------------------------------
def autoriza_voto(anoNasc):
    idade = anoAtual - anoNasc
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

# Função realizar a contagem dos votos caso o voto seja válido
def votacao(func, voto = 0, continuar = 's'):
    if func == 'NEGADO':
        print(CYELLOW, '\nVocê não pode votar ainda!\n', CEND)
        return
    elif voto in candidatos:
        contagemVotos[candidatos[voto]] += 1
    elif voto not in candidatos:
        return
    if continuar == 'n':
        # Limpa console
        print("\033c")
        print(CMAGENTA, 'VOTAÇÃO ENCERRADA!', CEND)
        sleep(1)
        eleito = ''
        maiorVotos = 0
        empate = False
        empateCandidato = ''

        print('\n---------------------')
        print('RESULTADO DA VOTAÇÃO:')
        print('---------------------\n')
        sleep(0.5)
        for i, votos in enumerate(contagemVotos.values(), 1):
            print(f'{candidatos[i]} teve {votos} voto(s)')
            sleep(0.5)
            if i < 4:
                if maiorVotos == votos:
                    empateCandidato = candidatos[i]
                    empate = True
                elif votos > maiorVotos:
                    maiorVotos = votos
                    eleito = candidatos[i]
        print()
        total = sum(contagemVotos.values())
        print(f'Tivemos um total de {CGREEN}{total}{CEND} voto(s)!')
        sleep(1)
        print()
        if empate:
            print(f'{CYELLOW}{eleito} e {empateCandidato} empataram com {maiorVotos} voto(s) cada!{CEND}\n')
        else: 
            print(f'{CGREEN}{eleito}{CEND} venceu com {CGREEN}{maiorVotos} voto(s)!{CEND} 🎉🎉\n')
#-----------------------------------------------------------------------------------------------------------

# VARIÁVEIS

# Mensagens de erro
mApenasNumeros = 'ERRO: Digite apenas números inteiros!'
mAnoInvalido = 'ERRO: Ano inválido!'
mOpcaoInvalida = 'ERRO: Digite uma opção válida!'

# Importar o ano atual
anoAtual = datetime.now().year

# Dicionário com os candidatos
candidatos = {
1: 'CUCA',
2: 'SACI-PERERÊ',
3: 'CURUPIRA',
4: 'BRANCO',
5: 'NULO'
}

# Dicionário para contagem dos votos
contagemVotos = {
'CUCA': 0,
'SACI-PERERÊ': 0,
'CURUPIRA': 0,
'BRANCO': 0,
'NULO': 0
}

# CORES
CRED = '\033[31;1;49m'
CYELLOW = '\033[33;1;49m'
CGREEN = '\033[1;32m'
CMAGENTA = '\033[1;95m'
CEND = '\033[39;0;49m'
BLIGHTBLUE = '\033[1;104m'

flag = True
voto = 0

#-----------------------------------------------------------------------------------------------------------

print(f'{BLIGHTBLUE}PROJETO 03 - SIMULADOR DE VOTAÇÃO (RAFAEL SOUZA){CEND}')

while flag:

    anoNascimento = 0
    while True:
        print('Olá, ELEITOR(A)!')
        # Verifica se o input digitado foi um inteiro
        try:

            anoNascimento = int(input('Digite seu ano de nascimento: '))
            idade = anoAtual - anoNascimento
        except ValueError:

            print(CRED, mApenasNumeros , CEND)
        
        # Mensagem de erro se ano de nascimento maior que o ano atual ou idade maior do que 100
        if anoNascimento > anoAtual or idade > 100:

            print(CRED, mAnoInvalido, CEND)

        elif anoNascimento != 0 and isinstance(anoNascimento, int):
            break
    
    # Mensagem para confirmar se a pessoa que tem o voto opcional deseja votar ou não
    if idade in [16, 17] or idade >= 70:

        while True:

            print(f'Seu voto é {CYELLOW}OPCIONAL{CEND}, deseja mesmo votar? [S/N] ', end='')
            resp = input()[0].lower()

            if resp == 's':

                # Se responder sim a idade vai para 18 para aparecer a parte da votação
                idade = 18
                break

            elif resp == 'n':
                idade = 0
                break
            else:

                print('\n', CRED, mOpcaoInvalida, CEND,'\n')

    if idade >= 18:

        while True:

            # Exibe os candidatos que estão dentro do dicionário candidatos
            print('------------------')
            for c in candidatos:

                print(f'[{CGREEN}{c}{CEND}] {candidatos[c]}')

            print('------------------')

            # Verifica se o input digitado foi um inteiro
            try:

                voto = int(input('Digite o número do seu voto: '))

            except ValueError:

                print('\n',CRED, mApenasNumeros, CEND,'\n')
            
            # Verifica se a opção é válida, ou seja, de 1 a 5
            if 0 > voto or voto > 5:

                print('\n', CRED, mOpcaoInvalida, CEND,'\n')

            elif voto != 0:

                break
    else:
        # Chama a função antecipadamente para gerar a mensagem de erro devido a idade
        votacao(autoriza_voto(anoNascimento))

    while True:

        # Verifica se há mais algum eleitor
        resposta = input('Mais algum eleitor? [S/N] ').lower()[0]
        print()
        if resposta in ['s', 'n']:

            # Limpa console
            print("\033c")
            # Troca flag para False, mostra contagem pela função e encerra o programa
            if resposta == 'n': flag = False
            break

        else:
            # Mensagem de erro, se resposta não for dentro do esperado
            print('\n', CRED, mOpcaoInvalida, CEND,'\n')

    if idade >= 16:
        # Chama a função
        votacao(autoriza_voto(anoNascimento), voto, resposta)