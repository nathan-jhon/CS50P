# This one is my code
'''
with open("students.csv") as file:
	for line in sorted(file):
		row = line.rstrip().split(",")
		print(f"{row[0]} lives in {row[1]}") '''
"""
students = []

with open("students.csv") as file:
    for line in file:
            name = line.rstrip().split(",")
            student = {"name":name[0], "house": name[1]}
            students.append(student)
def get_name(student):
	return student["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
"""

import csv
students = []
with open("students.csv") as file:
	reader = csv.reader(file)
	for i in reader:
		students.append({"name": i[0], "home": i[1]})
		
def get_name(student):
	return student["name"]
for student in sorted(students, key=get_name):
	print(f"{student['name']} is from {student['home']}")






























