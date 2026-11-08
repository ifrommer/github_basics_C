# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:38:35 2026

@author: gpt
"""
def introduction():
    print("=" * 45)
    print("          THE ISLAND OF MYSTERY")
    print("=" * 45)
    print()
    print("You have discovered an uncharted island.")
    print("Legend says that an ancient treasure is hidden")
    print("somewhere on the island.")
    print()
    print("Explore, collect clues, and solve the mystery!")
    print()


def get_choice(prompt, choices):
    while True:
        answer = input(prompt).lower().strip()

        if answer in choices:
            return answer

        print("That isn't one of the available choices.")
        print("Please choose:", ", ".join(choices))


def show_inventory(inventory):
    print("\nYOUR INVENTORY")
    print("----------------")

    if len(inventory) == 0:
        print("Your backpack is empty.")
    else:
        for item in inventory:
            print("-", item)


def explore_cave(inventory):
    print("\nYou enter a dark cave.")
    print("You hear water dripping somewhere in the distance.")

    if "golden key" not in inventory:
        print("\nYou discover a golden key on the ground!")
        inventory.append("golden key")
    else:
        print("\nYou've already collected everything here.")

    return "beach"


def explore_jungle(inventory):
    print("\nYou walk deep into the jungle.")
    print("After pushing through some thick vines,")
    print("you discover an old wooden box.")

    if "ancient map" not in inventory:
        print("\nInside the box is an ancient map!")
        inventory.append("ancient map")
    else:
        print("\nThere is nothing else of interest here.")

    return "beach"


def explore_temple(inventory):
    print("\nYou discover an ancient stone temple!")

    if "golden key" not in inventory:
        print("The entrance is locked.")
        print("You need to find a key.")
        return "beach"

    if "ancient map" not in inventory:
        print("You aren't sure how to find the treasure.")
        print("Perhaps there is a map somewhere on the island.")
        return "beach"

    print("\nYou use the golden key to open the temple.")
    print("Inside, you find a large stone door.")
    print("There is a message carved into the door:")
    print()
    print("I shine during the day,")
    print("I disappear at night,")
    print("I give the world warmth and light.")
    print()
    print("What am I?")

    answer = input("Your answer: ").lower().strip()

    if answer == "the sun" or answer == "sun":
        print("\nThe stone door slowly opens!")
        print("Behind it is a room filled with gold!")
        return "treasure"

    print("\nNothing happens.")
    print("Perhaps you should think about the message.")
    return "beach"


def treasure_ending():
    print("\n" + "=" * 45)
    print("              YOU FOUND IT!")
    print("=" * 45)
    print("You have discovered the lost treasure!")
    print("You are now the most famous explorer in the world.")
    print()
    print("But what will you do with your discovery?")

    choice = get_choice(
        "Keep the treasure or share it? ",
        ["keep", "share"]
    )

    if choice == "keep":
        print("\nYou take the treasure and become incredibly rich.")
    else:
        print("\nYou share the treasure with the world.")
        print("Your generosity makes you a legend.")

    print("\nTHE END!")


# Main program

inventory = []
location = "beach"
playing = True

introduction()

while playing:

    if location == "beach":

        print("\nYou are standing on the beach.")
        print("Where would you like to explore?")
        print("1. Enter the cave")
        print("2. Explore the jungle")
        print("3. Visit the ancient temple")
        print("4. Check your inventory")
        print("5. Quit the adventure")

        choice = get_choice("Your choice: ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            location = explore_cave(inventory)

        elif choice == "2":
            location = explore_jungle(inventory)

        elif choice == "3":
            location = explore_temple(inventory)

        elif choice == "4":
            show_inventory(inventory)

        elif choice == "5":
            print("\nYou decide to leave the island.")
            playing = False

    elif location == "treasure":
        treasure_ending()
        playing = False

print("\nThanks for playing The Island of Mystery!")