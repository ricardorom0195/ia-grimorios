"""UTILS FILE"""

import random

def get_trebol():
    number_list = [1, 2, 3, 4]
    probabilities = [0.65,0.20,0.10,0.05]
    select = random.choices(number_list, weights=probabilities, k=1)
    final = select[0] + 1 if select[0] != 1 else random.choice([1,2])
    return final
