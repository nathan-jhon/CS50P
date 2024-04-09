from calculator import square

def main():
	test_it()
def test_it():
	assert square(3) == 9 , "3 squred does not eqal 9"
	assert square(2) == 4 , "2 squred does not eqal 4"
if __name__ == "__main__":
	main()
