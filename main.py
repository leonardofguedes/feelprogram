"""
O FEEL é um app/site que permite você reagir a coisas de seu dia.
Por exemplo, você é fã de um time de futebol e em um Domingo qualquer, assiste uma partida que seu time perde de goleada.
Você reage no FEEL, dizendo como está se sentindo em relação ao time naquele instante. O FEEL responderá depois como está sua relação com o time.
"""

class Feel:
    def __init__(self,nome):
        self.nome = nome
        self.sentimento = 50


    def react(self,react):
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
        if self.sentimento >= 65:
            return 'Adorando'
        if self.sentimento >= 50:
            return 'Curtindo'
        if self.sentimento <= 30:
            return 'Odiando'
        else:
            return 'Relação conturbada'
        
