import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def check_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    return sum(cards)


def blackjack():
    is_game_finished = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    computer_choice = ["y", "n"]
    player_score = 0
    computer_score = 0

    # Player
    for player_card in range(0, 2):
        player_cards.append(random.choice(cards))
        player_score = check_score(player_cards)
    print(f"Player's cards: {player_cards}")
    print(f"Current player's score {player_score}")
    print(" ")
    # Computer
    for computer_card in range(0, 2):
        computer_cards.append(random.choice(cards))
        computer_score = check_score(computer_cards)
    print(f"Computers's cards: {computer_cards[0]}")

    if player_score == 0:
        print("You've got black jack")
        play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
        if play == 'y':
            clear()
            blackjack()
    if computer_score == 0:
        print("Computer has got blackjank, you lost")
        play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
        if play == 'y':
            clear()
            blackjack()

    print(" ")
    while not is_game_finished:
        player_decision = input("Type 'y' to get another card, type 'n' to pass ")

        while computer_score != 0 and computer_score < 17:
            computer_decision = random.choice(computer_choice)
            computer_cards.append(random.choice(cards))
            computer_score = check_score(computer_cards)
        if player_score > 21:
            is_game_finished = True
            play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
            if play == 'y':
                clear()
                blackjack()
            if computer_score > 17 and computer_score <= 21:
                if computer_decision == 'y':
                    computer_cards.append(random.choice(cards))
                    computer_score = check_score(computer_cards)
            if computer_score > 21 and 11 in computer_cards:
                computer_score -= 10
                computer_score += 1
            if computer_score > 21:
                print("Computer's score has exceeded the 21")
                print(f"Computers's cards: {computer_cards}")
                print(f"Current computer's score {computer_score}")
                print("")
                print(f"Player's cards: {player_cards}")
                print(f"Current player's score {player_score}")

                is_game_finished = True
                play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
                if play == 'y':
                    clear()
                    blackjack()

        print(f"Computers's cards: {computer_cards[0]}")

        print(" ")

        if player_decision == 'y':
            player_cards.append(random.choice(cards))
            if player_score > 21 and 11 in player_cards:
                player_score -= 11
                player_score += 1
            else:
                player_score = check_score(player_cards)
                print(f"Player's cards: {player_cards}")
                print(f"Current player's score {player_score}")
                print("")
        if player_score > 21:
            print("You have lost, your score has exceeded the 21")
            print(f"Computer cards: {computer_cards}")
            print(f"Current computer's score {computer_score}")
            is_game_finished = True
            play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
            if play == 'y':
                clear()
                blackjack()
            else:
                break
        if player_decision == 'n':
            final_score = player_score
            if final_score > computer_score and final_score <= 21:
                print(f"You have won having {final_score} with cards {player_cards} ")
                print(f"Computer cards: {computer_cards}")
                print(f"Current computer's score {computer_score}")
                is_game_finished = True
                play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
                if play == 'y':
                    clear()
                    blackjack()

            if player_score < computer_score and computer_score > 21:
                print(f"You have won having {final_score} with cards {player_cards} ")
                print(f"Computer cards: {computer_cards}")
                print(f"Current computer's score {computer_score}")
                is_game_finished = True
                play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
                if play == 'y':
                    clear()
                    blackjack()

            elif final_score == computer_score:
                print("It's a draw")
                print(f"Computer cards: {computer_cards}")
                print(f"Current computer's score {computer_score}")
                is_game_finished = True
                play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
                if play == 'y':
                    clear()
                    blackjack()

            else:
                print(f"You have lost having {final_score} with cards {player_cards} ")
                print(f"Computer cards: {computer_cards}")
                print(f"Current computer's score {computer_score}")
                is_game_finished = True
                play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ")
                if play == 'y':
                    clear()
                    blackjack()


play = input("Do you want to play a game of BlackJack, type 'y' or 'n' ").lower()
logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | | | |  _  ___| | ___   _  ___| | 
        | \  /|K /\  |     | '_ \| |/ _` |/ | |/ / |/ _` |/ | |/ /
        |  \/ | /  \ |     | |_) | | (_| | (|   <| | (_| | (|   < 
        `-----| \  / |     |_./|_|\,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """
print(logo)
if play == 'y':
    blackjack()