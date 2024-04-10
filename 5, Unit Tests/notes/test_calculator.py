from calculator import square
def test_square():
	assert square(2) == 4
	assert square(1) == 1
	assert square(3) == 9 
	assert square(-3) == 9
	assert square(-2) == 4
