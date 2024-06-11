import random

PARAMETERS = ['color', 'num', 'shape', 'shading']
COLORS = ['green', 'purple', 'red', 'black']
NUMBERS = [x for x in range(1,12)]
SHAPES = ['heart', 'diamond', 'clover', "leaf"]
NO_SET = -2
SHOW_HINT = -1
LEN_BOARD = 12

def print_board(board):
    for card in board:
        print(card)


def shuffle_deck(deck):
    print("shuffleing..")
    random.shuffle(deck)
    print("deck: ", deck)

def create_board(deck):
    board = list()
    for i in range(12):
        board.append(deck[i])
        deck.remove(deck[i])
    return board

def take_card():
    deck = list()
    for color in COLORS:
        for shape in SHAPES:
            for num in NUMBERS:
                    deck.append(create_card(color, shape, num))
    shuffle_deck(deck)
    return deck

def create_card(color, shape, shading, number):
    card = {
        "color": color,
        "shape": shape,
        "shading": shading,
        "num": number}
    return card

def play_turn (card):
    play = int(input("what you want to play 1(take one card) 2(hit) 3(double) 4(split) 5(Stand)"))
    while play <= 5 and play >= 1:
        if (play == 1):
            card = take_card()
        if (play == 2):
            cards = int(input("How many cards do you want to take?"))
            for i in range (cards + 1):
                card = take_card()
        if (play == 3):
            for i in range (3):
                card = take_card()
        if (play == 4):
            print("It can't be done right now and fixed in the future")
        elif (play == 5):
            
def create_player():
    player = {
        "name": input("What is your name?"),
        "money": 100,
        "cards": list() == 0
    }

    print(player)
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
        
    













#main()

create_player()