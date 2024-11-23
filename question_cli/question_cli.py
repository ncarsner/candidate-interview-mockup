"""Contains the logic for the command line interface."""

import json
# import random
import os

from questions import get_random_question


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "../data/questions.json"), "r"
    ) as f:
        questions = json.load(f)

    roles = list({role for question in questions for role in question["roles"]})

    print("Select a role:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")

    role_index = int(input("Select a role: ")) - 1
    role = roles[role_index]

    while True:
        question = get_random_question(role)
        print(f"\nQuestion: {question['text']}")
        
        cont = input("Another question? (Y to continue, any other key to exit): ").strip().lower()
        if cont == '':
            break


if __name__ == "__main__":
    main()
