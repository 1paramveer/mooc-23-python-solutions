# # Write your solution here

# # struct planned
# # [                             --> parent_list
# #     {                         --> child_dict
# #         'name': '', 
# #         'start_time': '',
# #         'end_time': ''
# #     }
# # ]

# import csv

# def cheaters():
#     parent_list = []
    
#     with open("start_times.csv") as stFile:
#         for line in csv.reader(stFile, delimiter=";"):
#             temp = {}
#             temp['name'] = line[0]
#             temp['start_time'] = line[1]
#             parent_list.append(temp)

#     with open("submissions.csv") as subFile:
#         for line in csv.reader(subFile, delimiter=";"):
            
#             for students in parent_list:
#                 if line[0] == students['name']:
#                     students['end_time'] = line[3]
#                     students['task'] = line[1]
#                     students['points'] = line[2]

#     return parent_list

# import csv
# from datetime import *
# def cheaters():
#     cheaters = []

#     with open('start_times.csv') as stFile:
#         with open('submissions.csv') as subFile:

#             for st_line in csv.reader(stFile, delimiter=';'):
#                 for sub_line in csv.reader(subFile, delimiter=';'):
                    
#                     if st_line[0] == sub_line[0]:
#                         time_difference = datetime.strptime(st_line[1], "%H:%M") - datetime.strptime(sub_line[-1], "%H:%M")
#                         hours = timedelta(time_difference.seconds // 3600)
                        
#                         if hours > timedelta(hours=3):
#                             if st_line[0] not in cheaters:
#                                 cheaters.append(st_line[0])


#     return cheaters

# print(cheaters())


import csv
from datetime import datetime, timedelta

def cheaters():
    cheaters = {}
    
    with open('start_times.csv') as stFile:
        st_reader = csv.reader(stFile, delimiter=';')
        st_dict = {row[0]: row[1] for row in st_reader}
    
    with open('submissions.csv') as subFile:
        sub_reader = csv.reader(subFile, delimiter=';')
        for sub_line in sub_reader:
            submission_time = datetime.strptime(sub_line[-1], "%H:%M")
            student_id = sub_line[0]
            if student_id in st_dict:
                start_time = datetime.strptime(st_dict[student_id], "%H:%M")
                time_difference = submission_time - start_time
                if time_difference > timedelta(hours=3):
                    cheaters[student_id] = time_difference
    
    return [i for i in cheaters.keys()]

# print(cheaters())
