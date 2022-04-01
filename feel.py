"""
FEEL is an app/site that allows you to react to things in your day.
For example, you are a fan of a football team and on any given Sunday,
you watch a match that your team loses by rout.
You react in FEEL, saying how you are feeling about the team at that moment.
FEEL will respond later on how is your relationship with the team.

O FEEL é um app/site que permite você reagir a coisas de seu dia.
Por exemplo, você é fã de um time de futebol e em um Domingo qualquer,
você assiste uma partida que seu time perde de goleada.
Você reage no FEEL, dizendo como está se sentindo em relação ao time naquele instante.
O FEEL responderá depois como está sua relação com o time.
"""

class Feel:
    def __init__(self,nome):
        self.nome = nome
        self.sentimento = 50


    def react(self,react=str):
        if react == 'Bem':
            self.sentimento += 12
        if react == 'Muito bem':
            self.sentimento += 18
        if react == 'Neutro':
            self.sentimento -= 7
        else:
            if react == 'Mal':
                self.sentimento -= 15
            if react == 'Péssimo':
                self.sentimento -= 20


    def show(self):
        if self.sentimento >= 90:  # [90, ]
            return 'Isso é um caso de AMOR!'
        if self.sentimento >= 65:  # [65, 89]
            return 'Adorando'
        if self.sentimento >= 50:  # [50, 64]
            return 'Curtindo'
        if self.sentimento > 30:  # [31, 49]
            return 'Relação conturbada'
        else:  # [ , 30]
            return 'Odiando'


    def __str__(self) -> str:
        return self.nome

