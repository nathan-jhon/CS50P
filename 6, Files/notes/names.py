# Note we can user any var name instade of file.write() file.close().
"""
j = open("test.txt", "w")
for i in range(3):
	name = input("name: ")
	j.write(name + "\n")
j.close()
"""

name = input("name: ")
j = open("test.txt", "a")
j.write(name + "/n")
j.close()
