from hello import hello

# def test_hello():
#	assert hello("nati") == "hello, nati"
#	assert hello() == "hello, world"
def test_default():
	assert hello() == "hello, world"
def test_arg():
	assert hello("nati") == "hello, nati"
