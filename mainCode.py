#Main Code

#Imports
import numpy as np
from playerClass import Player
from playerClass import BasicStratPlayer
import random

            
#Blackjack hand function
def blackjack(basic, bet, initHand, dealerCard, hardCode):
    #Creates deck from a numpy array
    basic.hand = []
    deck = np.array([1,2,3,4,5,6,7,8,9,10,10,10,10])
    hardStay = False
    #fills initially empty hand, with random cards
    if len(basic.hand) == 0:
        basic.hand = [random.choice(deck), random.choice(deck)]

    #hard stay for split aces    
    if basic.hand == [1]:
        hardStay = True
        
    #fill hand
    while (len(basic.hand) < 2):
        basic.hand.append(random.choice(deck))
    print(basic.hand)
    #dealer card creation
    if type(dealerCard) == str:
        dealerCard = random.choice(deck)
    dealerCards = [dealerCard]
    
    if hardStay == False:
        if basic.choice(dealerCard) == 'blackjack':
            #if casino also hit blackjack, tie
            dealerCards.append(random.choice(deck))
            if 1 in (dealerCards):
                if sum(dealerCards)==11:
                    return 0
            return bet*1.5
        #if hardCode uninit / first round
        if type(hardCode) == str:
            if hardCode =='hit':
                basic.hand.append(random.choice(deck))
                return blackjack(bet, basic.hand, dealerCard, hardCode= 4)
            
            if hardCode =='double':
                if len(basic.hand)==2:
                    basic.hand.append(random.choice(deck))
                    bet = bet * 2
                    if sum(basic.hand) > 21:
                        return 0 - bet
                else:
                    return 'double not possible'
            if hardCode == 'split':
                if len(basic.hand) == 2: 
                    if basic.hand[0] == basic.hand[1]:
                        res = blackjack(bet, [basic.hand[0]], dealerCard, 'Split')
                        res+= blackjack(bet, [basic.hand[0]], dealerCard, 'Split')
                        return res 
                    else:
                        return blackjack(bet, basic.hand, dealerCard)
                else:
                    return blackjack(bet, basic.hand, dealerCard)
        else:
            while basic.choice(dealerCard) == 'hit':
                #add card for hit
                basic.hand.append(random.choice(deck))
                #lose if hand busts
                if sum(basic.hand) > 21:
                    return 0 - bet
            #double
            if basic.choice(dealerCard) == 'double':
                #one card and double bet
                basic.hand.append(random.choice(deck))
                bet = bet * 2
                #if bust
                if sum(basic.hand) > 21:
                    return 0 - bet
            #split
            if basic.choice(dealerCard) == 'split':
                #runs sim as differenty hand
                res = blackjack(basic, bet, [basic.hand[0]], dealerCard, hardCode) 
                res += blackjack(basic, bet, [basic.hand[0]], dealerCard, hardCode)
                return res
        while True:
            #dealer side
            dealerCards.append(random.choice(deck))
            dealerScore = sum(dealerCards)
            #Keep track of soft score if dealer has an ace
            softScore = dealerScore
            if dealerScore<=11 and 1 in dealerCards:
                softScore +=10
            #If dealer gets blackjack you lose even if you have 21
            if len(dealerCards) == 2 and softScore == 21:
                return 0 - bet
            #Keeps track of player's score     
            playerScore = sum(basic.hand)
            #Uses soft score if that is better for player
            if playerScore <= 11 and 1 in basic.hand:
                playerScore += 10
            #Dealer stays on all 17s
            if softScore >= 17:
                #If dealer bust, player win
                if softScore > 21:
                    return bet
                #If player has more, player wins
                if playerScore > softScore:
                    return bet
                #Tie means no money
                if playerScore == softScore:
                    return 0
                #If player has lower, player loses bet
                if playerScore < softScore:
                    return 0 - bet
    if hardStay == True:
        #Plays out only dealer's side
        while True:
            dealerCards.append(random.choice(deck))
            dealerScore = sum(dealerCards)
            softScore = dealerScore
            if dealerScore <= 11 and 1 in dealerCards:
                softScore += 10
            #If dealer gets blackjack you lose
            if len(dealerCards) == 2 and softScore == 21:
                return 0 - bet
            playerScore = sum(basic.hand)
            #Uses soft score if that is better for player
            if playerScore <= 11 and 1 in basic.hand:
                playerScore += 10
            #Dealer stays on all 17s
            if softScore >= 17:
                #If dealer bust, player wins
                if softScore > 21:
                    return bet
                #If player has more, player wins
                if playerScore > softScore:
                    return bet
                #Tie means no money
                if playerScore == softScore:
                    return 0
                #If player has lower, player loses bet
                if playerScore < softScore:
                    return 0 - bet
    
    
#Simulation function
#  run multiple hands to test house edge with strategy vs. number of games
def simulation():
    print("How many matches?")
    matches = input()
    percent = 0
    result = []
    
    p1 = BasicStratPlayer()
    p = 'q'
    q = len('q')
    #Loops for the user-inputed amount
    for i in range(int(matches)):
        percent += blackjack(p1, 10, p[:q], 'q', 4);
    return -100 * (percent / int(matches))
    
#Calls on simulation
print(simulation())