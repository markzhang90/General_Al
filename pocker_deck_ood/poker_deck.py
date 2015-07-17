# pocker deck
from random import shuffle


class Card:
    suit_dic = {1: 'Diamond',
                2: 'Hearts',
                3: 'Clubs',
                4: 'Spades'}

    num_dic = {1: '1',
               2: '2',
               3: '3',
               4: '4',
               5: '5'}

    def __init__(self, suit, num):
        self.suit = self.suit_dic.get(suit)
        self.num = self.num_dic.get(num)

    def get_suit(self):
        return self.suit

    def get_num(self):
        return self.num

    def to_string(self):
        return "%s - %s" % (self.suit, self.num)


class Deck:
    car_list = []

    def __init__(self):
        for i in range(1, 5):
            for j in range(1, 5):
                self.car_list.append(Card(i, j))

    def shuffled_cards(self):
        shuffle(self.car_list)
        return self.car_list

    def show_cards(self):
        for x in Deck.shuffled_cards():
            print x.to_string()


Deck = Deck()
Deck.show_cards()
