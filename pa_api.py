import requests


def download_course_data():
    print("Downloading all future course data... ", end='')
    results = requests.get("https://proagile.se/api/publicEvents")
    result_as_json = results.json()
    print("Done.")
    return result_as_json


def get_all_trainers():
    results = requests.get("https://proagile.se/api/publicEmployees")
    results_as_json = results.json()
    return results_as_json
