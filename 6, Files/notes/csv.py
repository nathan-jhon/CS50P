# This one is my code
'''
with open("students.csv") as file:
	for line in sorted(file):
		row = line.rstrip().split(",")
		print(f"{row[0]} lives in {row[1]}") '''
students = []

with open("students.csv") as file:
    for line in file:
            name = line.rstrip().split(",")
            student = {"name":name[0], "house": name[1]}
            students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

