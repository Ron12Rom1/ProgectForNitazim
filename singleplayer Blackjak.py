import time
import random

help(format)

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
    # time.sleep(2)
    global players
    players = create_playersInfo()
    print("Shuffeling cards...")
    # time.sleep(2.5)
    global deck
    deck = create_deck()
    print("Done! Game is ready.\nGood lack ", players[1]["name"],"!", sep="")
    # time.sleep(1)
    print("\nGame starts in 5...")
    # time.sleep(1)
    print("4...")
    # time.sleep(1)
    print("3...")
    # time.sleep(1)
    print("2...")
    # time.sleep(1)
    print("1...")
    # time.sleep(1)
    print("\n".join([" " for _ in range(40)]))


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

        player = players[1]
        give_players_cards(player, deck)
        print(player)

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

        





main()