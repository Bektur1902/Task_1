import json

with open('student_info.json') as f:
    student = json.load(f)
print(student)