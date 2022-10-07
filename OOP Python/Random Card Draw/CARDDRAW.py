from random import shuffle

class Cards:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def display(self):
        print("{}, {}" .format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Cards(s, v))
    
    def show(self):
        for c in self.cards:
            c.display()
    
    def shuffle(self):
        shuffle(self.cards)
        
    def drawCard(self):
        return self.cards.pop()
       
              
                
deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.display()