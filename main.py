"""
Find the Fastest Horses
 - You are given 25 horses, and your task is to determine the three fastest horses among them.
 - You can only race five horses at a time
 - There are no timers available.
 - The only information you can obtain from each race is the order in which the horses finish.

Your goal is to design an algorithm that can find the three fastest horses with the minimum number of races.
"""

import random
import argparse
import os


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


def write_horses_to_file(horses, filename):
    """
    Write the list of horses to a text file
    :param horses: list of horses
    :param filename: name of the output file
    """
    try:
        with open("instances/"+filename, 'w') as file:
            for horse in horses:
                file.write(str(horse) + '\n')
    except IOError:
        # An error occurred while writing to the file
        print(f"An error occurred while writing to the file '{filename}'.")


def read_horses_from_file(filename):
    """
    Read the list of horses from a text file
    :param filename: name of the input file
    :return: list of horses
    """
    horses = []
    try:
        with open("instances/"+filename, 'r') as file:
            for line in file:
                horses.append(int(line.strip()))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return horses









if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Horse Racing')
    parser.add_argument('filename', default='horses.txt', help='Name of the output file (default: horses.txt)')
    args = parser.parse_args()

    filename = args.filename
    if ".txt" not in filename:
        filename = filename+".txt"

    if not os.path.exists("instances/"+filename):
        print("Instance not found. Generating horses...")
        horses = generate_horses()
        print(f"Saving horses to instances/{filename}")
        write_horses_to_file(horses, filename)
    else:
        print("Instance found. Reading...")
        horses = read_horses_from_file(filename)


