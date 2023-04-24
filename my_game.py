import random

computer_wins = 0
user_wins = 0
rounds = 0


def get_computer_choice():
    choices = ['piedra', 'papel', 'tijera']
    return(random.choice(choices))


def user_choice():
    choices =['piedra', 'papel', 'tijera']
    user_choice = input('Escoja un opcion: piedra papel tijera ::')
    user_choice = user_choice.lower
    if not user_choice in choices:
        print('opcion invalida')
        user_choice()
    return user_choice


def play_again():
    again = input('Quieres jugar de nuevo? si/no')
    again = again.lower
    if again == 'si':
        play()
    elif again == 'no':
        print('Gracias por jugar Adios Puto')
    else:
        print('opcion invalida pelotudo')
        play_again()

def play():
    global user_wins
    global computer_wins
    global rounds
    rounds  += 1

# IMCOMPLETO