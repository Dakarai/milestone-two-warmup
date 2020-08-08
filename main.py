import random

suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
war_cards_count = 3


class Card:

    def __init__(self, suit, rank):
        self.suit = suit[0].lower()
        self.rank = rank
        self.value = values[rank]

    def __repr__(self):
        return self.rank + "" + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name.capitalize()
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


if __name__ == '__main__':
    # create players
    player_one = Player("One")
    player_two = Player("Two")

    # create deck object and shuffle it
    new_deck = Deck()
    new_deck.shuffle()

    # split shuffled deck between players
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    play_game = True
    round_number = 0

    while play_game:
        round_number += 1
        print(f"Round {round_number}")

        if len(player_one.all_cards) == 0:
            print('Player One has lost!')
            play_game = False
            break
        elif len(player_two.all_cards) == 0:
            print('Player Two has lost!')
            play_game = False
            break

        # start a new round
        player_one_cards = [player_one.remove_one()]
        player_two_cards = [player_two.remove_one()]

        end_of_round = False
        while not end_of_round:
            # evaluate round
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                end_of_round = True
                print(player_one_cards)
                print(player_two_cards)
                print(player_one)
                print(player_two)
                break
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)
                end_of_round = True
                print(player_one_cards)
                print(player_two_cards)
                print(player_one)
                print(player_two)
                break
            else:
                for _ in range(war_cards_count):
                    if len(player_one.all_cards) > 0:
                        player_one_cards.append(player_one.remove_one())
                    if len(player_two.all_cards) > 0:
                        player_two_cards.append(player_two.remove_one())
