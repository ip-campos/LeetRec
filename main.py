import os
from datastructures import *
from problemset import subjects, problem_set, difficulties

def print_welcome():
    os.system("clear")
    print("""
    _______________________
    *                      *
    *  Welcome to LeetRec  *
    *______________________*

    We recommend leetcode problems based on subject and difficulty
    """)

def insert_problem_data():
    subjects_map = HashMap(len(subjects))

    for key in subjects:
        difficulty_map = HashMap(3)

        for difficulty in difficulties:
            difficulty_list = LinkedList()
            difficulty_map.assign(difficulty, difficulty_list)
        subjects_map.assign(key, difficulty_map)

    for problem in problem_set:
        target_list = subjects_map.retrieve(problem[0]).retrieve(problem[1])
        target_list.add_node(problem)
    return subjects_map


    
