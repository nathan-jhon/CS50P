"""
import csv
with open("students.csv", 'a') as file:
	writer = csv.writer(file)
	for i in range(3):
		x = input("name: ")
		y = input("home: ")
		writer.writerow([x, y])
"""

# DictWriter
import csv
name = input("name: ")
home = input("home: ")
with open("students.csv", 'a') as file:
	writer = csv.DictWriter(file, fieldnames=["name", "home"])
	writer.writerow({"name": name, "home": home})
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
