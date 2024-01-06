# Write your solution here

import urllib.request
import json

def retrieve_all():
    list = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    requested_data = my_request.read()
    courses = json.loads(requested_data)

    for _ in courses:
        if _['enabled'] == True:
            data = (_['fullName'],_['name'], _['year'], sum(_['exercises']))
            list.append(data)

    return list

def retrieve_course(course_name: str):

    dict_ = {   # defining struct
        'weeks': None,
        'students': None,
        'hours': None,
        'hours_average': None,
        'exercises': None,
        'exercises_average': None
    }

    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    requested_data = my_request.read()
    courses = json.loads(requested_data)

    dict_['weeks'] = len(courses) # adding weeks to dict_
    max_students = 0
    dict_['hours'] = 0
    dict_['exercises'] = 0

    for _,__ in courses.items():

        # checking max students in each of the courses
        if __['students'] > max_students:
            max_students = __['students']
            dict_['students'] = max_students

        # calculating hours in all courses
        dict_['hours'] += __['hour_total']
        dict_['exercises'] += __['exercise_total']

    dict_['hours_average'] = int(dict_['hours'] / dict_['students']) # typecasting to int to round off
    dict_['exercises_average'] = int(dict_['exercises'] / dict_['students']) # ''

    return dict_


