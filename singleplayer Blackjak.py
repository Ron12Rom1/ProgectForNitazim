import time
import random

def intro():
    print("Welcome to the gratest game of all games!\n(By Ron Bruk & Itay something)")
    print("""
 /$$$$$$$  /$$                     /$$          /$$$$$           /$$                                                                  
| $$__  $$| $$                    | $$         |__  $$          | $$                                                                  
| $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$      | $$  /$$$$$$ | $$   /$$                                                            
| $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/      | $$ |____  $$| $$  /$$/                                                            
| $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  | $$  /$$$$$$$| $$$$$$/                                                             
| $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$  | $$ /$$__  $$| $$_  $$                                                             
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$/|  $$$$$$$| $$ \  $$                                                            
|_______/ |__/ \_______/ \_______/|__/  \__/ \______/  \_______/|__/  \__/                                                            
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
 /$$$$$$$                  /$$$$$$$                                                      /$$       /$$$$$$ /$$                        
| $$__  $$                | $$__  $$                                                    | $$      |_  $$_/| $$                        
| $$  \ $$ /$$   /$$      | $$  \ $$  /$$$$$$  /$$$$$$$         /$$$$$$  /$$$$$$$   /$$$$$$$        | $$ /$$$$$$    /$$$$$$  /$$   /$$
| $$$$$$$ | $$  | $$      | $$$$$$$/ /$$__  $$| $$__  $$       |____  $$| $$__  $$ /$$__  $$        | $$|_  $$_/   |____  $$| $$  | $$
| $$__  $$| $$  | $$      | $$__  $$| $$  \ $$| $$  \ $$        /$$$$$$$| $$  \ $$| $$  | $$        | $$  | $$      /$$$$$$$| $$  | $$
| $$  \ $$| $$  | $$      | $$  \ $$| $$  | $$| $$  | $$       /$$__  $$| $$  | $$| $$  | $$        | $$  | $$ /$$ /$$__  $$| $$  | $$
| $$$$$$$/|  $$$$$$$      | $$  | $$|  $$$$$$/| $$  | $$      |  $$$$$$$| $$  | $$|  $$$$$$$       /$$$$$$|  $$$$/|  $$$$$$$|  $$$$$$$
|_______/  \____  $$      |__/  |__/ \______/ |__/  |__/       \_______/|__/  |__/ \_______/      |______/ \___/   \_______/ \____  $$
           /$$  | $$                                                                                                         /$$  | $$
          |  $$$$$$/                                                                                                        |  $$$$$$/
           \______/                                                                                                          \______/ \n\n⁽ᵀʰᶦˢ ᵍᵃᵐᵉ ᶦˢ ˢᶦⁿᵍᵉˡᵖˡᵃʸᵉʳ⁾\n\n\n\n""")
    
    print("Initializing player...")
    #time.sleep(2)
    global players
    players = create_playersInfo()
    #time.sleep(1)
    print("Shuffeling cards...")
    #time.sleep(2.5)
    global deck
    deck = create_deck()
    print("Done! Game is ready.\nGood lack ", players[1]["name"],"!", sep="")
    #time.sleep(1)
    print("\nGame starts in 5...")
    #time.sleep(1)
    print("4...")
    #time.sleep(1)
    print("3...")
    #time.sleep(1)
    print("2...")
    #time.sleep(1)
    print("1...")
    #time.sleep(1)
    print("\n".join([" " for _ in range(40)]))


NUMBERS = [int(2),int(3),int(4),int(5),int(6),int(7),int(8),int(9),int(10),"J","Q","K","A"]
SHAPES = ['heart', 'diamond', 'clover', "leaf"]
NO_SET = -2
SHOW_HINT = -1
LEN_BOARD = 12

def create_deck():
    deck = list()
    for shape in SHAPES:
        for num in NUMBERS:
                deck.append(create_card(shape,  num))
    # deck = random.shuffle(deck)
    return deck

def create_card(shape, number):
    card = {
        "shape": shape,
        "num": number}
    return card

def create_playersInfo():
    players = list()
    players.append({
        "name": "Dealer",
        "money": 100,
        "cards": []
    })
    players.append(create_1player())
    return players

def create_1player():
    player = {
        "name": input("What is your name?   "),
        "money": 100,
        "cards": [],
        "bet": 0
    }
    return player

def give_players_cards(player, deck):
    for i in range(2):
        card = random.choice(deck)
        deck.remove(card)
        player["cards"].append(card)

def give_players_1_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    player["cards"].append(card)
    

def print_card(card):
    if card["shape"] == "diamond":
        print("♦ " + str(card['num']))
    elif card["shape"] == "heart":
        print("♥ " + str(card['num']))
    elif card["shape"] == "clover":
        print("♣ " + str(card['num']))
    elif card["shape"] == "leaf":
        print("♠ " + str(card['num']))

def draw_table_END():
     print("\n\n\nDealer's cards: ")
     for card in players[0]["cards"]:
         print_card(card)
     print("\nYour cards: ")
     for card in players[1]["cards"]:
         print_card(card)
         print()
     print("Dealer's score: ", get_score_1_card(players[0]["cards"][0]))
     print("Your score: ", get_score_1_card(players[1]["cards"][0]))
    
def draw_table_1_card():
    print("\n\n\n\nYour cards: ")
    for i in range(len(player["cards"])-1):
        print_card(player["cards"][i])
    print("You're score: ", get_score_1_card(player["cards"]))
    print("\n\nDealer's cards: ")
    print_card(dealer["cards"][0])
    print("Dealer's score: ", get_score_1_card(dealer["cards"]))
    


def get_score_1_card(cards):
    score = 0
    for i in range(len(cards)-1):
        if cards[i]["num"] == "J":
            score += 11
        elif cards[i]["num"] == "Q":
            score += 12
        elif cards[i]["num"] == "K":
            score += 13
        elif cards[i]["num"] == "A":
            score += 14
        else:
            score += cards[i]["num"]
    return score

def play_turn (deck):
    play = int(input("what you want to play: 1(take one card) 2(hit) 3(double) 4(split) 5(Stand)"))
    while play <= 5 and play >= 1:
        if (play == 1):
            give_players_1_card(deck)
            draw_table_1_card()
            play = -1
        if (play == 2):
            cards = int(input("How many cards do you want to take?"))
            for i in range (cards + 1):
                ...
        if (play == 3):
            for i in range (3):
                ...
        if (play == 4):
            print("It can't be done right now and fixed in the future")
        elif (play == 5):
            pass  


def main():
        """Evry one place a bet

         Give players 2 cards (open and close) (dealer too) (if dealer under 16 take another one and if above 18 he cant take notheing)

         ask players to choose to take a card or pass or do split(only if two of a kind)

        for each player check if score higher then 21 if not 
        check if score lower then dealer's score

        select the winner"""


        intro()
        print("(Game started)\n\n")
        #print(players)

        global player, dealer
        player = players[1]
        dealer = players[0]
        give_players_cards(player, deck)
        give_players_cards(dealer, deck)
        print(player)
        print(dealer)

        print("Please make a bet (you have " + str(player["money"]) + ")")

        while True:
            try:        
                player["bet"] = int(input(": "))
                break
            except ValueError:
                print("Please enter a number.")

        while True:
            if player["money"] - player["bet"] < 0:
                print("You cant do that, You only have " + str(player["money"]))
                player["bet"] = int(input("Enter you're bet: "))
            else:
                player["money"] -= player["bet"]
                print("You are left with " + str(player["money"]))
                break

        
        draw_table_1_card()

        play_turn(deck)



main()