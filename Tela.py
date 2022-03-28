from main import Feel

reacts = ['Péssimo','Mal','Neutro','Bem','Muito bem']

while True:
    assunto = str(input('Qual é o assunto que você deseja reagir?')).strip().capitalize()
    x = Feel(assunto)
    resposta = False
    while resposta == False:
        react = str(input(f'Como você se sentiu em relação a(o) {x.nome} hoje?\n[Péssimo][Mal][Neutro][Bem][Muito bem]')).strip().capitalize()
        if react not in reacts:
            print('Você deve falar uma opção listada.\nObs: Cuide os acentos')
        else:
            resposta = True
    continuar = input(f'Você deseja saber o seu sentimento pelo {x.nome}? [S][N]').strip().upper()
    if continuar == 'S':
        print(f'Seu sentimento pelo {x.nome} é de {x.sentimento}.')
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