"""
Find the Fastest Horses
 - You are given 25 horses, and your task is to determine the three fastest horses among them.
 - You can only race five horses at a time
 - There are no timers available.
 - The only information you can obtain from each race is the order in which the horses finish.

Your goal is to design an algorithm that can find the three fastest horses with the minimum number of races.
"""

import random


def generate_horses():
    """
    Generate a list of 25 horses with different times to finish race
    :return: list of horses
    """
    horses = []
    for i in range(25):
        horses.append(i)
    random.shuffle(horses)
    return horses


if __name__ == '__main__':

    horses = generate_horses()
    print(horses)
