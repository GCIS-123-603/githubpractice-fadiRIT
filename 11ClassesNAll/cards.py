class Card:
    def __init__(self,rank_value, suit_value):
        self.rank = rank_value
        self.suit = suit_value
        self.name = self.rank,"of",self.suit
        self.shorthand = str(self.rank)+self.suit[0]


a_card = Card(5,"hearts")
b_card = Card(12,'Quartz')

print(a_card.name,b_card.name)