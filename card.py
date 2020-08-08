class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #self.value =

    def __str__(self):
        return self.rank + " of " + self.suit