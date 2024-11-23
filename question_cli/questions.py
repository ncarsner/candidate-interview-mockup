"""Contains the logic for handling questions.
"""

import json
import os
import random

def load_questions():
    with open(os.path.join(os.path.dirname(__file__), '../data/questions.json')) as f:
        return json.load(f)

def get_random_question(role):
    questions = load_questions()
    role_questions = [q for q in questions if role in q['roles']]
    return random.choice(role_questions)