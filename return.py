import random

computer_wins = 0
player_wins = 0
rounds = 0

def get_computer_choice():
    choices = ["piedra", "papel", "tijera"]
    return random.choice(choices)

def User_choice():
    choices = ["piedra", "papel", "tijera"]
    user_choice = input("elige una opcion: piedra, papel o tijera: ")
    user_choice = user_choice.lower()
    if not  user_choice in choices:
        print("opcion invalida")
        user_choice()
    return user_choice

def play_again():
    again = input("quieres jugar de nuevo? si/no: ")
    again = again.lower()
    if again == "si":
        play()
    elif again == "no":
        print("gracias por jugar")
    else:
        print("opcion invalida")
        play_again()

def play():
    global computer_wins
    global player_wins
    global rounds
    rounds += 1
    print(f"ronda {rounds}")
    print(f"computadora: {computer_wins} - jugador: {player_wins}")
    computer_choice = get_computer_choice()
    user_choice =  User_choice()
    print(f"computadora eligio {computer_choice}")
    print(f"jugador eligio {user_choice}")
    if computer_choice == user_choice:
        print("empate")
    elif computer_choice == "piedra" and user_choice == "papel":
        print("jugador gana")
        player_wins += 1
    elif computer_choice == "piedra" and user_choice == "tijera":
        print("computadora gana")
        computer_wins += 1
    elif computer_choice == "papel" and user_choice == "piedra":
        print("computadora gana")
        computer_wins += 1
    elif computer_choice == "papel" and user_choice == "tijera":
        print("jugador gana")
        player_wins += 1
    elif computer_choice == "tijera" and user_choice == "piedra":
        print("jugador gana")
        player_wins += 1
    elif computer_choice == "tijera" and user_choice == "papel":
        print("computadora gana")
        computer_wins += 1
    else:
        print("opcion invalida")
    if rounds < 3:
        play()
    else:
        if computer_wins > player_wins:
            print("computadora gana LAS RONDAS")
        elif computer_wins < player_wins:
            print("jugador gana LAS RONDAS")
        else:
            print("empate")
        play_again()
    
play()
