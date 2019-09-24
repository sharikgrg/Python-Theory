# #Nested list and dictionaries
#
# nested_list = ['bread', 'sugar', [1,2,3,4, 'spice']]
#
#
# # print(nested_list[2])
# # # to access the list inside the list
# # variable_bread = nested_list[2]
# # print(variable_bread[4])
#
# print(nested_list[2] [4])
# print(nested_list[2] [5] ['name']

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'complete modules': ['sword', 'augmneted senses', 'no face', 'no']
}

students = {
    'student1': student1,
    'student2': {
    'name': 'Stirling archer',
    'stream': 'chaos',
    'grade': 10,
    'complete modules': ['danger', 'robust liver', 'mummy issues', 'espionage']
    }
}

for k in students:
    for ki in students[k]:
        print (ki, students[k][ki])

# for student_key in students:
#     count_1 = 1
#     for key in students[student_key]:
#         print(count_1, ':', key, students[student_key][key])
#         count_1 += 1
# for key in students:
#     print(key, students[key])
# for key in student1:
#     print(key, ':', student1[key])
#
# for key in students['student1' 'student2']:
#     print(key, ':', students['student1' 'student2'][key])



# breakpoint()
#
# print(students['student1']['name'])
# print(students['student2']['name'])