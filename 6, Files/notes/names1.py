"""
names = []
with open("with.txt") as file:
	for line in file:
		names.append(line.rstrip())
for i in sorted(names):

	print(i)
"""
import emoji
with open("with.txt") as file:
	for line in sorted(file):  # reverse=True
		print(emoji.emojize("Hello :waving_hand: ") + line.strip())
