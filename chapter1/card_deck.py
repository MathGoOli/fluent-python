
from random import choice
import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])

class FrencDeck:
    """ makes a deck of card and has [] operator"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position): # this method delegates to [] operator
        return self._cards[position]

class CardSorter:
    """ card sorter class is for namespace """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    @classmethod
    def spades_high(cls, card: Card) -> int:
        rank_value = FrencDeck.ranks.index(card.rank)
        return rank_value * len(cls.suit_values) + cls.suit_values[card.suit]
    

    
if __name__ == '__main__':
    deck = FrencDeck()

    # print(len(deck))
    # print(deck[-1])

    # for card in deck:
    #     print(card)

    # print(choice(deck))

    for card in sorted(deck, key=CardSorter.spades_high):
        print(card)