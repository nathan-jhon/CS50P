# Note we can user any var name instade of file.write() file.close().
"""
j = open("test.txt", "w")
for i in range(3):
	name = input("name: ")
	j.write(name + "\n")
j.close()
"""
# Note this code is from the cs50p class
""" 
name = input("name: ")
j = open("test.txt", "a")
j.write(name + "\n")
j.close()

"""

# With
'''
for nati in range(3):
	name = input("name: ")
	with open("with.txt", "a") as i:
		i.write(name + "\n")
'''
with open("with.txt", "r") as file:
	lines = file.readlines()
	
for line in lines:
	# print(f"hello, {line}") We can use 
	print("hello", line.rstrip())
























