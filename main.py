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

def print_topics():
        print("\nAvailable topics: ")
        for idx, subject in enumerate(subjects):
            print(idx+1, "- ", subject)
        return
    
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
        return get_difficulty()

def print_problems(problem_list):
    problems_head = problem_list.head
    while problems_head:
        print("--------------------------")
        print(f"Name: {problems_head.get_value()[2]}")
        print(f"Link: {problems_head.get_value()[3]}")
        problems_head = problems_head.get_next_node()
    return

def repeat():
    ans = input("\nDo you want to find other problems? Enter 'y' for yes and 'n' for no: ").lower()

    if ans == "y":
        return main()
    elif ans != "n":
        print("Invalid input, try again...")
        return repeat()




subjects_map = insert_problem_data()

print_welcome()
def main():

    print_topics()

    topic = get_topic()
        
    topic_map = subjects_map.retrieve(topic)

    difficulty = get_difficulty()

    problem_list = topic_map.retrieve(difficulty)

    print(f"\nYou chose:\nTopic: {topic}\nDifficulty: {difficulty}")
    
    if problem_list.length >0:
        print(f"\nHere are the recommended problems:")
        print_problems(problem_list)

    else:
        print("\nThere are no recommended problems with this topic and level of difficulty.")

    repeat()

    print("\nThank you for using LeetRec!\nSee you next time!")







main()

        
