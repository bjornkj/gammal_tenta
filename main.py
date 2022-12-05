from datetime import datetime
from pa_api import download_course_data, get_all_trainers

MENU_TEXT = """
---> MENU <---
1) List all trainers sorted by name
2) List 5 next upcoming courses sorted by date
3) List all courses with a specific trainer
4) List telephone number of most popular trainer
Q) Quit
"""


def course_start_date(course):
    return datetime.fromtimestamp(course['segments'][0]['start'])


def get_trainer_id_with_most_courses(all_courses) -> int:
    trainers = {}  # trainerId : antal_kurser
    for course in all_courses:
        if 'trainerId' in course:
            if course['trainerId'] in trainers:
                trainers[course['trainerId']] += 1
            else:
                trainers[course['trainerId']] = 1
    return max(trainers, key=trainers.get)


def run():
    all_courses = download_course_data()
    while True:
        print(MENU_TEXT)
        menu_choice = input("What say you? ").upper().strip()
        if menu_choice == '1':
            list_trainers(all_courses)
        if menu_choice == '2':
            list_next_five(all_courses)
        if menu_choice == '3':
            list_courser_for_trainer(all_courses)
        if menu_choice == '4':
            print_top_trainer(all_courses)
        if menu_choice.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return


def print_top_trainer(all_courses):
    top_trainer = get_trainer_id_with_most_courses(all_courses)
    # print(f"trainer id of trainer with most courses {top_trainer}")
    #  (10 p): Print the name of the trainer who
    #  (15 p): Also print out the phone
    trainers = get_all_trainers()
    for trainer in trainers:
        if trainer['id'] == top_trainer:
            print(f"{trainer['name']} ({trainer['phone']})")
    # of that trainer.
    # Note: The trainer is an employee of ProAgile,
    # and public data about employees are available
    # from this API endpoint:
    #    https://proagile.se/api/publicEmployees


def list_courser_for_trainer(all_courses):
    # (10 p): Allow user entering only part of name.
    # E.g. if the user enters "fredrik", all courses
    # held by "Fredrik Wendt" will be listed.
    trainer_name = input("Name of trainer:")
    print(f"These courses are held by {trainer_name}:")
    trainers_courses = [course for course in all_courses
                        if trainer_name.lower() in course['trainerName'].lower()]
    for num, course in enumerate(trainers_courses):
        print(f"{num}. {course['courseName']} ({course_start_date(course)})")


def list_trainers(course_data):
    # (5 p):
    # Sort the trainers before printing them.
    print("The trainers at ProAgile are:")
    trainers = []
    for course in course_data:
        trainer = course['trainerName']
        if trainer not in trainers:
            trainers.append(trainer)
    for trainer in sorted(trainers):
        print(f'  {trainer}')


def list_next_five(course_data):
    # (10p):
    # 1. First column is always 2 column wide
    # 2. Second column is always 50 columns wide
    # 3. Third column is as small as possible
    # (5p):
    #  - We want next 5, not all courses printed
    # (5p):
    #  - We want the sorted on startDate, not name
    # (5p):
    #  - We want the output numbered from 1, not 0
    print("Next 5 courses sorted by date:")
    course_data = sorted(course_data, key=lambda c: course_start_date(c))
    for num, course in enumerate(course_data[:5], start=1):
        print(f"{num}. {course['courseName'] : <50} ({course_start_date(course)})")


if __name__ == '__main__':
    run()
