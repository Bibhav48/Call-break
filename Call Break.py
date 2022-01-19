import random
from os import system
from time import sleep
import sys

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.status = 'High' if rank=='♠' else 'Low'
        
    def __str__(self):
        return f'{self.suit}{self.rank}'
    
    def value(self):
        if self.suit=='A':
            return 13
        elif self.suit=='K':
            return 12
        elif self.suit=='Q':
            return 11
        elif self.suit=='J':
            return 10
        else:
            return int(self.suit)-1  
    
def str_value(string):
    j,i=string[:-1],string[-1]
    return Card(i,j).value()



class Deck:
    def __init__(self):
        self.cards=[]
        
    def build(self,number_of_decks=1):
        ranks = ['♠','♥','♣', '♦']
        suits = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards=[Card(i,j) for i in ranks for j in suits]*number_of_decks

    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        return ' '.join(map(str,self.cards))


    def draw(self):
        self.cards.pop()
        

class Player:
    def __init__(self):
        self.hand = []
        self.points=0

    def take(self,deck):
        card = deck.cards[0]
        self.hand.append(card)
        deck.cards.remove(card)
            
    def throw(self,index_card):
        self.hand.pop(index_card-1)

    def remove_all(self,deck):
        deck.cards.extend(self.hand)
        self.hand.clear()
            
    
    def __str__(self):
        self.hand.sort(key= lambda x:(x.rank,x.value()))
        return '\t'.join(map(str,range(1,len(self.hand)+1)))+'\n'+'\t'.join(map(str,self.hand))


def loading():
    for i in range(1,101):
        string=f'{i}% |'+'|'*round(i//2)+' '*(50-round(i//2))+'|'
        print(string,end='',flush=True)
        sleep(0.01)
        if i!=100:
            print('\b'*len(string),end='')
        else:
            print()


############################################################ Main pogram #################################################################

my_deck = Deck()
my_deck.build()

player1 =Player()
player2 =Player()
player3 =Player()
player4 =Player()

Players_list=[input(f"Enter Player{i}'s name: ") for i in range(1,5)]

game = 0
points=[0 for i in range(4)]

while game !=4:
    if game>0:
        my_deck = Deck()
        my_deck.build()
    total_cards_used=[]
    calls = []
    while ('♠' not in [str(i)[-1] for i in player1.hand]) or ('♠' not in [str(i)[-1] for i in player2.hand]) or ('♠' not in [str(i)[1] for i in player3.hand]) or ('♠' not in [str(i)[-1] for i in player4.hand]):
        my_deck.shuffle()
        if player1.hand:
            player1.remove_all(my_deck)
            player2.remove_all(my_deck)
            player3.remove_all(my_deck)
            player4.remove_all(my_deck)

        for i in range(13):
            player1.take(my_deck)
            player2.take(my_deck)
            player3.take(my_deck)
            player4.take(my_deck)
            
    for i in range(1,5):
        print(f"\nLoading {Players_list[i-1]}'s cards")
        loading()
        print(globals()[f'player{i}'])
        call = int(input("Number of wins you want to call: "))
        calls.append(call)
        system('cls')


    if game==0:
        order=range(1,5)
    elif game==1:
        order=[2,3,4,1]
    elif game==2:
        order=[3,4,1,2]
    elif game==3:
        order=[4,1,2,3]


    print("\nLet's start the game")
    while len(player1.hand)!=0:
        if not order:
            order=[1,2,3,4]
        current_cards=[]
        for i in order:
            if total_cards_used:
                print("Total cards used are:-")
                for cards in total_cards_used:
                    print(*cards)
                print('\n')
            if i!=order[0]:
                print("Cards used by players are:-")
                print(*current_cards)
            print(f"\nLoading {Players_list[i-1]}'s cards")
            loading()

            current_player=globals()[f'player{i}']
            print(globals()[f'player{i}'])
            
            while True:
                try:
                    throw_card_pos=int(input("Enter the Position of card you want to use: "))
                    throw_card=str(current_player.hand[throw_card_pos-1])
                    break
                except:
                    if str(sys.exc_info()[0]) == "<class 'KeyboardInterrupt'>":
                        exit()
                    
            if i!=order[0]:
                while True:
                    if (throw_card[-1]==current_cards[0][-1]):
                        if str_value(throw_card) > max([str_value(i) for i in current_cards if str(i)[-1]==throw_card[-1]]):
                            break
                        elif (((max([i.value() for i in current_player.hand if ((str(i)[-1]==current_cards[0][-1]))])  < max([str_value(i) for i in current_cards if i[-1]==throw_card[-1]])))):
                            break
                        if '♠' in [i[-1] for i in current_cards]:
                            if throw_card[-1] != '♠':
                                break
                            print("Haat ma thulo tash xa ta")
                        else:
                            print("Haat ma thulo tash xa ta")

                    elif (throw_card[-1]=='♠') and current_cards[0][-1] not in [str(i)[-1] for i in current_player.hand] :
                        if '♠' not in [i[-1] for i in current_cards]:
                            break
                        elif throw_card[:-1]>max([i[:-1] for i in current_cards if i[-1]=='♠']):
                            break
                        else:
                            print('Hukkum kina waste garne?')
                        
                    elif current_cards[0][-1] not in [str(i)[-1] for i in current_player.hand]:
                        if '♠' not in [str(i)[-1] for i in current_player.hand]:
                            break
                        elif '♠' in [i[-1] for i in current_cards] and current_cards[0][-1] not in [str(i)[-1] for i in current_player.hand]:
                            if max([str_value(i) for i in current_cards if i[-1]=='♠']) > max([i.value() for i in current_player.hand if str(i)[-1]=='♠']):
                                break
                        else:
                            print('♠ tass xa ta tyo faal na')
                    else:
                        print(f'Yo ta {throw_card[-1]} ko tash ho. "{current_cards[0][-1]}" ko ki "♠" ko chaiyo.')
                        

                    throw_card_pos=int(input(f"Please Enter the Position of card again: "))
                    throw_card=str(current_player.hand[throw_card_pos-1])

            current_cards.append(throw_card)
            
            (globals()[f'player{i}']).throw(throw_card_pos)
            if i!=order[-1]:
                if i==4:
                    print(f"\nPass the device to {Players_list[0]}")
                else:
                    print(f"\nPass the device to {Players_list[i]}")
            sleep(2)
            system('cls')

        total_cards_used.append(current_cards)
        if '♠' not in [i[-1] for i in current_cards]:
            for i in current_cards:
                if i[-1]==current_cards[0][-1]:
                    winner_pos=[str_value(i) for i in current_cards if i[-1]].index(max([str_value(i) for i in current_cards if i[-1]==current_cards[0][-1]]))
        
        elif [i[-1] for i in current_cards].count('♠')==1:
            winner_pos=[i[-1] for i in current_cards].index('♠')

        else:
            for i in current_cards:
                if i[-1]==current_cards[0][-1]:       
                    winner_pos=[str_value(i) for i in current_cards].index(max([str_value(i) for i in current_cards if i[-1]=='♠']))
                    

        print(f'{Players_list[order[winner_pos]-1]} won this round')
        winner = globals()[f'player{order[winner_pos]}']
        winner.points +=1
        if order[winner_pos]==1:
            order=range(1,5)
        elif order[winner_pos]==2:
            order=[2,3,4,1]
        elif order[winner_pos]==3:
            order=[3,4,1,2]
        elif order[winner_pos]==4:
            order=[4,1,2,3]


        print('Points:')
        for i in range(1,5):
            print(f"{Players_list[i-1]}: {globals()[f'player{i}'].points}")
        if not current_player.hand:
            print(f"\nPass the device to {Players_list[order[0]-1]} ")
        sleep(5)
        loading()
        
        system('cls')

        pts = [globals()[f'player{i}'].points for i in range(1,5)]
    print(f"Winner of game {game+1} is {Players_list[pts.index(max(pts))]}")
    for i in range(1,5):
        if calls[i-1]<=globals()[f'player{i}'].points:
            points[i-1] += 1
        else:
            points[i-1] -=1

    print('Overall points:')
    for i in range(1,5):
        print(f"{Players_list[i-1]}: {points[i-1]}")
    
    game += 1
if points.count(max(points))==1:
    print(f"The OVERALL WINNER is {Players_list[points.index(max(pts))]}")
else:
    high=[]
    for i in range(4):
        if i!=max(points):
            pts[i]=0
    if pts.count(max(points))==1:
        print(f"The OVERALL WINNER is {Players_list[pts.index(max(pts))]}")
    else:
        print(f"The OVERALL WINNER are",end=' ')
        for i in range(4):
            if pts[i]!=0:
                print(Players_list[i],end=' ')
            
