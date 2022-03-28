from main import Feel
from time import sleep

def carregando():
    tempo = '.'*50
    for c in tempo:
        print(c, end='')
        sleep(0.2)
    print('')

reacts = ['Péssimo','Mal','Neutro','Bem','Muito bem']

def tela():
    while True:
        assunto = str(input('Qual é o assunto que você deseja reagir?')).strip().capitalize()
        x = Feel(assunto)
        resposta = False
        while resposta == False:
            r = str(input(f'Como você se sentiu em relação a(o) {x.nome} hoje?\n[Péssimo][Mal][Neutro][Bem][Muito bem]')).strip().capitalize()
            x.react(r)
            if r not in reacts:
                print('Você deve falar uma opção listada.\nObs: Cuide os acentos')
            else:
                resposta = True
        continuar = input(f'Você deseja saber o seu sentimento pelo {x.nome}? [S][N]').strip().upper()
        if continuar == 'S':
            print(f'Seu sentimento pelo {x.nome} é:')
            carregando()
            print(f'<<<{x.show()}>>>')
            repeat = str(input('Quer continuar? [S][N]')).strip().upper()
            if repeat == 'N':
                break
            else:
                pass
        else:
            repeat = str(input('Quer continuar? [S][N]')).strip().upper()
            if repeat == 'N':
                break
            else:
                pass

tela()
