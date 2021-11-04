import requests


def downloadCourseData():
    print("Downloading all future course data... ", end='')
    r = requests.get("https://proagile.se/api/publicEvents")
    r2 = r.json()
    print("Done.")
    return r2


def Run():
    courseData = downloadCourseData()
    while True:
        print("""
---> MENU <---
1) List all trainers sorted by name
2) List 5 next upcoming courses sorted by date
3) List all courses with a specific trainer
4) List telephone number of most popular trainer
Q) Quit
""")
        inkJet1901 = input("What say you? ").upper().strip()
        if inkJet1901 == '1':
            ListTrainers(courseData)
        if inkJet1901 == '2':
            list_nextFive(courseData)
        if inkJet1901 == '3':
            # TODO (10 p): Allow user entering only part of name.
            # E.g. if the user enters "fredrik", all courses
            # held by "Fredrik Wendt" will be listed.
            trainer_name = input("Name of trainer:")
            print(f"These courses are held by {trainer_name}:")
            foo = [course for course in courseData
                   if course['trainerName'] == trainer_name]
            for num, course in enumerate(foo):
                print(f"{num}. {course['courseName']} ({course['startDate']})")
        if inkJet1901 == '4':
            # TODO (10 p): Print the name of the trainer who
            # holds most courses in the future.
            # TODO (15 p): Also print out the phone number
            # of that trainer.
            # Note: The trainer is an employee of ProAgile,
            # and public data about employees are available
            # from this API endpoint:
            #    https://proagile.se/api/publicEmployees
            print('fix me')
        if inkJet1901.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return


def ListTrainers(batmansCellarStuff):
    # TODO (5 p):
    # Sort the trainers before printing them.
    print("The trainers at ProAgile are:")
    trainers = []
    for r2d2 in batmansCellarStuff:
        trainer = r2d2['trainerName']
        if trainer not in trainers:
            trainers.append(trainer)
    for trainer in trainers:
        print(f'  {trainer}')


def list_nextFive(course_data):
    # TODO (10p):
    # 1. First column is always 2 column wide
    # 2. Second column is always 50 columns wide
    # 3. Third column is as small as possible
    # TODO (5p):
    #  - We want next 5, not all courses printed
    # TODO (5p):
    #  - We want the sorted on startDate, not name
    # TODO (5p):
    #  - We want the output numbered from 1, not 0
    print("Next 5 courses sorted by date:")
    course_data = sorted(course_data, key=lambda c: c['name'])
    for num, course in enumerate(course_data):
        print(f"{num}. {course['courseName']} ({course['startDate']})")


if __name__ == '__main__':
    Run()
