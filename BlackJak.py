import random

NUMBERS = [x for x in range(1,14)]
SHAPES = ['heart', 'diamond', 'clover', "leaf"]
NO_SET = -2
SHOW_HINT = -1
LEN_BOARD = 12

def create_deck():
    deck = list()
    for shape in SHAPES:
        for num in NUMBERS:
                deck.append(create_card(shape,  num))
    deck = shuffle_deck(deck)
    return deck

def print_board(board):
    for card in board:
        print(card)


def shuffle_deck(deck):
    print("Shuffleing..")
    random.shuffle(deck)
    print("Done!, Ready to play!")
    return deck

# def create_board(deck):
#     board = list()
#     for i in range(12):
#         board.append(deck[i])
#         deck.remove(deck[i])
#     return board

def take_card(deck):
    #! to make the function work

    return deck

def create_card(shape, number):
    card = {
        "shape": shape,
        "num": number}
    return card

#! WHAT THE HECK IS THIS FUNCTION!?!?!
# def play_turn ():
#     play = int(input("what you want to play 1(take one card) 2(hit) 3(double) 4(split) 5(Stand)"))
#     while play <= 5 and play >= 1:
#         if (play == 1):
#             card = take_card()
#         if (play == 2):
#             cards = int(input("How many cards do you want to take?"))
#             for i in range (cards + 1):
#                 card = take_card()
#         if (play == 3):
#             for i in range (3):
#                 card = take_card()
#         if (play == 4):
#             print("It can't be done right now and fixed in the future")
#         elif (play == 5):
#             pass  ####! This should not be here
            
def create_player():
    player = {
        "name": input("What is your name?"),
        "money": 100,
        "cards": []
    }
    return player



def create_playersInfo():
    players = list()
    for i in range(player_count):
        players.append(create_player())
    return players


##################################################################
##################################################################


def main():
    global player_count
    player_count = -1
    while True:
        try:
            player_count = int(input("How many players will play this game: "))
            if player_count < 1:
                print("At least one player needs to play this game.")
            elif player_count > 6:
                print("Too many players. Maximum is 6.")
            else: break
        except ValueError:
            print("Please enter a number.")
    
        
        #* Create players
    players = create_playersInfo()
    
        #! give players cards

    
        #* Get shuffled deck and give players cards
    deck = create_deck()
    print(deck)


    #* Game Starts
    #----------------------------------------------------------------
    while True:
        





    #----------------------------------------------------------------

    #print(take_card())



    print(players)
    
    













main()

