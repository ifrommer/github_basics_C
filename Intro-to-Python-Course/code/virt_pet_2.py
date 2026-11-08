# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:46:31 2026

@author: Math
"""
def introduction():
    print("=" * 45)
    print("             DRAGON KEEPER")
    print("=" * 45)
    print()
    print("Congratulations! You have adopted a baby dragon.")
    print("Your job is to keep your dragon happy and healthy.")
    print()
    print("You have 12 turns to take care of your dragon.")
    print("Watch its hunger, energy, and happiness!")
    print()


def get_choice(prompt, choices):
    while True:
        answer = input(prompt).lower().strip()

        if answer in choices:
            return answer

        print("Please choose one of:", ", ".join(choices))


def change_stat(value, amount):
    value = value + amount

    if value < 0:
        value = 0

    if value > 10:
        value = 10

    return value


def show_status(name, hunger, energy, happiness):
    print("\n" + "=" * 35)
    print(name.upper(), "'S STATUS")
    print("=" * 35)

    print("Hunger:    ", hunger, "/ 10")
    print("Energy:    ", energy, "/ 10")
    print("Happiness: ", happiness, "/ 10")

    if hunger >= 8:
        print(name, "is very hungry!")

    if energy <= 2:
        print(name, "is very tired!")

    if happiness <= 2:
        print(name, "is feeling sad.")

    if hunger <= 2 and energy >= 7 and happiness >= 8:
        print(name, "is doing wonderfully!")


def feed_dragon(name, hunger, happiness):
    print("\nYou give", name, "a delicious dragon treat!")
    hunger = change_stat(hunger, -4)
    happiness = change_stat(happiness, 1)

    return hunger, happiness


def play_with_dragon(name, hunger, energy, happiness):
    print("\nYou play a game of dragon tag!")

    hunger = change_stat(hunger, 2)
    energy = change_stat(energy, -2)
    happiness = change_stat(happiness, 3)

    return hunger, energy, happiness


def let_dragon_sleep(name, hunger, energy):
    print("\n", name, "curls up and takes a nap.")

    hunger = change_stat(hunger, 1)
    energy = change_stat(energy, 4)

    return hunger, energy


def cuddle_dragon(name, hunger, energy, happiness):
    print("\nYou give", name, "a big hug.")

    hunger = change_stat(hunger, 1)
    energy = change_stat(energy, -1)
    happiness = change_stat(happiness, 2)

    return hunger, energy, happiness


# Main program

name = input("What would you like to name your dragon? ").strip()

if name == "":
    name = "Sparky"

hunger = 3
energy = 7
happiness = 6

turns = 0
max_turns = 12
playing = True

introduction()

print("Your dragon's name is", name, "!")

while playing and turns < max_turns:

    print("\nWhat would you like to do?")
    print("1. Feed your dragon")
    print("2. Play with your dragon")
    print("3. Let your dragon sleep")
    print("4. Cuddle your dragon")
    print("5. Check status")
    print("6. Quit")

    choice = get_choice(
        "Your choice: ",
        ["1", "2", "3", "4", "5", "6"]
    )

    if choice == "5":
        show_status(name, hunger, energy, happiness)

    elif choice == "6":
        playing = False

    else:

        if choice == "2" and energy < 2:
            print("\nYour dragon is too tired to play!")
            print("Try letting it sleep first.")

        else:
            # Time passes whenever an activity is performed.
            hunger = change_stat(hunger, 1)
            energy = change_stat(energy, -1)

            if choice == "1":
                hunger, happiness = feed_dragon(
                    name, hunger, happiness
                )

            elif choice == "2":
                hunger, energy, happiness = play_with_dragon(
                    name, hunger, energy, happiness
                )

            elif choice == "3":
                hunger, energy = let_dragon_sleep(
                    name, hunger, energy
                )

            elif choice == "4":
                hunger, energy, happiness = cuddle_dragon(
                    name, hunger, energy, happiness
                )

            turns = turns + 1

            print("\nTurns remaining:", max_turns - turns)

            show_status(name, hunger, energy, happiness)

            if hunger == 10:
                print("\nOh no! Your dragon is too hungry!")
                print("You need to take better care of it.")
                playing = False

            elif happiness == 0:
                print("\nYour dragon is very unhappy.")
                print("It needs more attention!")
                playing = False


# End of game

print("\n" + "=" * 40)
print("              GAME OVER")
print("=" * 40)

show_status(name, hunger, energy, happiness)

if hunger < 10 and happiness > 0 and turns == max_turns:
    print("\nCongratulations!")
    print("You successfully cared for", name, "for 12 turns!")

elif hunger < 10 and happiness > 0:
    print("\nYou finished taking care of", name, ".")

else:
    print("\nBetter luck next time!")

print("\nThanks for playing DRAGON KEEPER!")