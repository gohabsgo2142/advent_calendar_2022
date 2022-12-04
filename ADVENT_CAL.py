# coding: utf-8
"""
---------------------------
File : ADVENT_CAL.py
Create by : jarvis
Puzzle date : 2022-12-01
---------------------------
"""

import argparse
from december.Day_1 import day_1 as d1
from december.Day_2 import day_2 as d2


def get_args() -> argparse.Namespace:
    """Define the argpas command line args."""
    parser = argparse.ArgumentParser(description="Advent calendar project")
    parser.add_argument('-d', '--dates', type=int, help='Add the report to QA_DB')
    return parser.parse_args()


if get_args() is not None:
    """Start the logic"""

if get_args().dates == 1:
    d1.elf_calculation()

if get_args().dates == 2:
    d2.rock_paper_scissors()
    d2.indication_rounds()
