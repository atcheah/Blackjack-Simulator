#Player Class

#Imports
import random

#Player Class
class Player(object):
    #Init function of basic interface for players, not for instantion
    def __init__(self):
        self.hardCount = 0
        self.softCount = 0
        self.aceCount = 0
        self.cards = 0
        self.hand = []
        self.goodCards = [1,7,8,9,10]
    def __repr__(self):
        return "style: %s | points: %d | money: %d" %(self.style, self.points(), self.money)    

class BasicStratPlayer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return super().__repr__()
    
    def choice(self, dealerCard):
        self.hardCount = sum(self.hand)
        self.cards = len(self.hand)
        self.aceCount = 1*(1 in self.hand)
        self.softCount = self.hardCount
        
        if self.cards < 2:
            return 'Not enough cards '
        if self.hardCount <= 11:
            self.softCount = self.hardCount + 10 * self.aceCount
        if self.cards == 2 and self.softCount == 21:
            return 'blackjack'
        if self.softCount >= 19:
            return 'stay'
        if self.hand == [9,9] and dealerCard not in [1,7,10]:
            return 'split'
        if self.hardCount >= 17 :
            return 'stay'
        if self.cards > 2:
            if self.hardCount == self.softCount:
                if self.hardCount <= 11:
                    return 'hit'
                if self.hardCount == 12 and dealerCard <= 3:
                    return 'hit'
                if dealerCard in self.goodCards:
                    return 'hit'
                return 'stay'
            if self.softCount <= 17:
                return 'hit'
            if self.softCount == 18 and dealerCard in [1,9,10]:
                return 'hit'
            return 'stay'
        if self.cards == 2:
            if self.hand[0] == self.hand[1]:
                card = self.hand[0]
                if card == 1:
                    return 'split'
                if card == 8 and dealerCard!=1:
                    return 'split'
                if card in [2,3,7] and dealerCard not in [1,8,9,10]:
                    return 'split'
                if card == 6 and dealerCard not in self.goodCards:
                    return 'split'
                if card == 4 and dealerCard in [5,6]:
                    return 'split'
            if self.hardCount == self.softCount:
                if self.hardCount == 11 and dealerCard != 1:
                    return 'double'
                if self.hardCount == 10 and dealerCard not in [1,10]:
                    return 'double'
                if self.hardCount == 9 and dealerCard not in ([2] + self.goodCards):
                    return 'double'
                if self.hardCount <= 11:
                    return 'hit'
                if self.hardCount == 12 and dealerCard <= 3:
                    return 'hit'
                if dealerCard in self.goodCards:
                    return 'hit'
                return 'stay'
            if self.hardCount != self.softCount:
                if self.softCount == 18:
                    if dealerCard not in ([2] + self.goodCards):
                        return 'double'
                    if dealerCard in [2,7,8]:
                        return 'stay'
                if self.softCount == 17 and dealerCard in [3,4,5,6]:
                    return 'double'
                if self.softCount in [15,16] and dealerCard in [4,5,6]:
                    return 'double'
                if self.softCount in [13,14] and dealerCard in [5,6]:
                    return 'double'
                return 'hit'