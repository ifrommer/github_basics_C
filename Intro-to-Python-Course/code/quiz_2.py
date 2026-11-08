# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:44:56 2026

@author: Math
"""
def introduction():
    print("=" * 45)
    print("          THE ULTIMATE TRIVIA CHALLENGE")
    print("=" * 45)
    print("Test your knowledge and see how high you can score!")
    print()


def get_choice(prompt, choices):
    while True:
        answer = input(prompt).lower().strip()

        if answer in choices:
            return answer

        print("Please choose one of:", ", ".join(choices))


def play_quiz(category, questions, answers, hints):

    score = 0
    streak = 0
    best_streak = 0

    print("\nStarting the", category, "quiz!")
    print("You earn 2 points for a correct answer.")
    print("You can ask for a hint, but then earn only 1 point.")
    print("Type 'skip' if you don't know an answer.")

    for i in range(len(questions)):

        print("\nQUESTION", i + 1, "OF", len(questions))
        print(questions[i])

        used_hint = False

        while True:
            response = input("Your answer: ").lower().strip()

            if response == "hint":
                if used_hint:
                    print("You've already used your hint!")
                else:
                    print("HINT:", hints[i])
                    used_hint = True

            elif response == "skip":
                print("The answer was:", answers[i])
                streak = 0
                break

            elif response == answers[i]:
                print("CORRECT!")

                if used_hint:
                    score = score + 1
                else:
                    score = score + 2

                streak = streak + 1

                if streak > best_streak:
                    best_streak = streak

                print("Current score:", score)
                print("Current streak:", streak)
                break

            else:
                print("Not quite! Try again or type 'hint' or 'skip'.")

                # Give the player one more chance.
                response = input("Try again: ").lower().strip()

                if response == answers[i]:
                    print("CORRECT!")
                    score = score + 2
                    streak = streak + 1

                    if streak > best_streak:
                        best_streak = streak

                    print("Current score:", score)
                    print("Current streak:", streak)
                    break
                else:
                    print("The answer was:", answers[i])
                    streak = 0
                    break

    print("\n" + "=" * 35)
    print("             RESULTS")
    print("=" * 35)

    print("Category:", category)
    print("Final score:", score)
    print("Possible points:", len(questions) * 2)
    print("Best correct-answer streak:", best_streak)

    if score == len(questions) * 2:
        print("PERFECT SCORE! You're a trivia superstar!")
    elif score >= len(questions):
        print("Great job! You know your stuff!")
    else:
        print("Nice try! Time to brush up on your trivia!")

    return score


# Questions for the different categories

science_questions = [
    "What planet is known as the Red Planet?",
    "What gas do plants absorb from the atmosphere?",
    "What is the center of an atom called?",
    "What is the largest planet in our solar system?"
]

science_answers = [
    "mars",
    "carbon dioxide",
    "nucleus",
    "jupiter"
]

science_hints = [
    "It is named after the Roman god of war.",
    "It has the chemical formula CO2.",
    "It contains protons and neutrons.",
    "It has a famous giant red storm."
]


geography_questions = [
    "What is the capital of France?",
    "Which continent is Egypt in?",
    "What is the largest ocean?",
    "What country is famous for the Great Wall?"
]

geography_answers = [
    "paris",
    "africa",
    "pacific",
    "china"
]

geography_hints = [
    "The Eiffel Tower is located there.",
    "It is the continent containing the Sahara Desert.",
    "It is larger than the Atlantic Ocean.",
    "Its capital is Beijing."
]


# Main program

playing = True

while playing:

    print("\nChoose your trivia category:")
    print("1. Science")
    print("2. Geography")
    print("3. Quit")

    choice = get_choice("Your choice: ", ["1", "2", "3"])

    if choice == "1":
        play_quiz(
            "Science",
            science_questions,
            science_answers,
            science_hints
        )

    elif choice == "2":
        play_quiz(
            "Geography",
            geography_questions,
            geography_answers,
            geography_hints
        )

    else:
        playing = False

print("\nThanks for playing!")