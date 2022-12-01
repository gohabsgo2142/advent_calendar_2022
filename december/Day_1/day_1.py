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


def elf_calculation():
    path = f"{os.path.join(sys.path[0], 'december/Day_1/data.txt')}"
    elves, elf_cal_counts, number_eleves = [], 0, 0,

    with open(path, 'r') as elf:
        for i in elf:
            i = i.strip('\n')
            if i == '':
                elves.append(elf_cal_counts)
                elf_cal_counts = 0
                number_eleves = number_eleves + 1
            else:
                elf_cal_counts = int(i) + elf_cal_counts

    top_3_elves = sorted(elves, reverse=True)[:3]
    total_3_elf = top_3_elves[0] + top_3_elves[1] + top_3_elves[2]

    print('Number of elf:', number_eleves)
    print('Answer 1 -> High calories:', top_3_elves[0])
    print('Calories for 3 elfs:', total_3_elf)
