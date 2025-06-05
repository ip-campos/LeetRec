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

def print_topics(runs):
    if runs == 0:
        print("\nAvailable topics:")
        for idx, subject in enumerate(subjects):
            print(idx+1, "- ", subject)
        return
    else:
        show_topics = str(input("\nDo you want to see the list of available topics again? type 'y' for yes or 'n' for no: ")).lower()
        if show_topics == "y":
            print_topics()
        elif show_topics != "y" and show_topics != "n":
            print("\nInvalid input, try again...")
            print_topics(runs)

def get_topic():
    try:
        user_input = int(input("\nWhat topic are you studying today? Type the corrensponding number: "))
    except:
        print("Invalid input, try again...")
        return get_topic()
    if user_input > len(subjects) or user_input < 0:
        print("Invalid input, try again...")
        return get_topic()
    user_topic = subjects[user_input-1]
    return user_topic

def get_difficulty():
    difficulties = {"e": "Easy", "m": "Medium", "h": "Hard"}
    user_input = input("\nChoose a difficulty level. Enter 'e' for Easy, 'm' for Medium and 'h' for Hard: ").lower()
    try:
        difficulty = difficulties[user_input]
        return difficulty
    except:
        print("Invalid input, try again...")
        get_difficulty()


subjects_map = insert_problem_data()

selected_topic = ""
runs = 0

print_welcome()
while len(selected_topic) == 0:

    print_topics(runs)
        
    topic_map = subjects_map.retrieve(get_topic())

    difficulty = get_difficulty()

    problem_list = topic_map.retrieve(difficulty)
        
