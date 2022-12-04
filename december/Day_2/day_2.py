# coding: utf-8
"""
---------------------------
File : day_1.py
Create by : jarvis
Puzzle date : 2022-12-01
---------------------------
"""
import os
import sys


# Part 1
def rock_paper_scissors():
    """
    A= Rock B= Paper C= Scissors
    X= 1 Rock Y= 2 Paper Z= 3 Scissors
    Win= 6 Lose= 0 Draw= 3
    ------------------
    Win= A -> Y 8
    Win= B -> Z 9
    Win= C -> X 7
    ----------------
    Draw= A -> X 4
    Draw= B -> Y 5
    Draw= C -> Z 6
    ---------------
    Lose= A -> Z 3
    Lose= B -> X 1
    Lose= C -> Y 2
    :return: Number of points
    """
    win_points = 0
    path = f"{os.path.join(sys.path[0], 'input.txt')}"
    with open(path, 'r') as read:
        for i in read:
            if i[0] == 'A' and i[2] == 'Y':
                win_points = win_points + 8
            elif i[0] == 'B' and i[2] == 'Z':
                win_points = win_points + 9
            elif i[0] == 'C' and i[2] == 'X':
                win_points = win_points + 7
            elif i[0] == 'A' and i[2] == 'X':
                win_points = win_points + 4
            elif i[0] == 'B' and i[2] == 'Y':
                win_points = win_points + 5
            elif i[0] == 'C' and i[2] == 'Z':
                win_points = win_points + 6
            elif i[0] == 'A' and i[2] == 'Z':
                win_points = win_points + 3
            elif i[0] == 'B' and i[2] == 'X':
                win_points = win_points + 1
            elif i[0] == 'C' and i[2] == 'Y':
                win_points = win_points + 2
    print('Number of points:', rock_paper_scissors())


# Part 2
def indication_rounds():
    """
    A= 1 Rock B= 2 Paper C= 3 Scissors
    X= Lose Y= Daw Z= Win
    Win= 6 Lose= 0 Draw= 3
    ------------------
    A -> X 3
    A -> Y 4
    A -> Z 8
    -----------------
    B -> X 1
    B -> Y 5
    B -> Z 9
    -----------------
    C -> X 2
    C -> Y 6
    C -> Z 7
    :return:
    """
    win_points = 0
    path = f"{os.path.join(sys.path[0], 'input.txt')}"
    with open(path, 'r') as read:
        for i in read:
            if i[0] == 'A' and i[2] == 'X':
                win_points = win_points + 3
            elif i[0] == 'A' and i[2] == 'Y':
                win_points = win_points + 4
            elif i[0] == 'A' and i[2] == 'Z':
                win_points = win_points + 8

            elif i[0] == 'B' and i[2] == 'X':
                win_points = win_points + 1
            elif i[0] == 'B' and i[2] == 'Y':
                win_points = win_points + 5
            elif i[0] == 'B' and i[2] == 'Z':
                win_points = win_points + 9

            elif i[0] == 'C' and i[2] == 'X':
                win_points = win_points + 2
            elif i[0] == 'C' and i[2] == 'Y':
                win_points = win_points + 6
            elif i[0] == 'C' and i[2] == 'Z':
                win_points = win_points + 7
    print('Number of points:', indication_rounds())
