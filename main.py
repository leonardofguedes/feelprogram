from feel import Feel
from time import sleep

reacts = ['Péssimo', 'Mal', 'Neutro', 'Bem', 'Muito bem'] #reacts permitidas no programa

def carregando(): #função de carregar a página (estilo apenas)
    tempo = '.'*50
    for c in tempo:
        print(c, end='')
        sleep(0.2)
    print('')

lista_assuntos = [] #lista de assuntos reagidos


def procurar_assunto_por_nome(nome): #função para conferir se o assunto já foi reagido anteriormente (se está na lista)
    for assunto in lista_assuntos:
        if assunto.nome == nome:
            return assunto



def receber_react(nome): #função captar a reação do cliente
    while True:
        r = input(f'Como você se sentiu em relação a(o) {nome} hoje?\n[Péssimo][Mal][Neutro][Bem][Muito bem] ').strip().capitalize()
        if r not in reacts:
            print('Você deve escolher uma das opções listadas.\nObs: Cuide os acentos')
        else:
            return r


def mostra_sentimento(assunto): #função mostrar o sentimento do cliente
    print(f'Seu sentimento pelo {assunto.nome} é:')
    carregando()
    print(f'<<< {assunto.show()} >>>')

def tela():

    while True:
        nome = input('Qual é o assunto que você deseja reagir?').strip().capitalize()
        assunto = procurar_assunto_por_nome(nome)

        if assunto:
            print('Você já interagiu sobre esse assunto antes.')
            continuar = input(f'Você quer avaliar o {assunto} novamente? [S][N] ').upper().strip()
            if continuar == 'S':
                r = receber_react(nome)
                assunto.react(r)

                print('Recebemos sua nova reação.')

                continuar = input(f'Você deseja saber o seu sentimento pelo {assunto}? [S][N] ').strip().upper()
                if continuar == 'S':
                    mostra_sentimento(assunto)


        else:
            assunto = Feel(nome)
            lista_assuntos.append(assunto)

            r = receber_react(nome)
            assunto.react(r)

            continuar = input(f'Você deseja saber o seu sentimento pelo {assunto.nome}?[S][N]').strip().upper()
            if continuar == 'S':
                mostra_sentimento(assunto)
            else:
                assuntos = [f'{a}' for a in lista_assuntos]
                print(f'Suas reações são sobre os seguintes assuntos:\n{assuntos}')
