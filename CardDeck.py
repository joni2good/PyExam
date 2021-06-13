class Card:
    def __init__(self, value, face):
        self.value = value
        self.face = face

    def __str__(self):
        return 'value: ' + str(self.value) + ', face: ' + self.face


class Deck:
    def __init__(self, cards = []):
        self.cards = cards

    def __len__(self):
        cnt = 0
        for card in self.cards:
            cnt += 1
        return cnt

    def __getitem__(self, key):
        return self.cards[key]

    def __add__(self, cards):
        return Deck(self.cards + cards)

    def __repr__(self):
        string = ""
        for card in self.cards:
            string += 'card{Card face: ' + card.face + ', Card value: ' + str(card.value) + '}\n'
        return string

    def __str__(self):
        string = ""
        for card in self.cards:
            string += 'Card face is ' + card.face + ' and Card value is ' + str(card.value) + '\n'
        return string

    def __setitem__(self, key, card):
        self.cards[key] = card
        return True

    def __delitem__(self, key):
        self.cards.pop(key)
        return True


card1 = Card(1, 'jonas er grim')
card2 = Card(9, 'ruder')
card3 = Card(2, 'klør')
card4 = Card(7, 'hjerter')
card5 = Card(6, 'spar')
deck = Deck([card1, card2])
print(len(deck))
deck = deck + [card3, card4]
print(len(deck))
print(deck[2])
print(deck)
print(repr(deck))
print(deck[3])
deck[3] = card5
print(deck[3])
print(deck)
del deck[3]
print(deck)
