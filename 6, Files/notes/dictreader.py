
import csv
students = []
with open("students.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student['name']):
	print(f"{student['name']}")

