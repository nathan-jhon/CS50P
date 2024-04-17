import bank

def test_value_hello():
    assert bank.value("Hello") == 0

def test_value_hello_uppercase():
    assert bank.value("HELLO") == 0

def test_value_hello_newman():
    assert bank.value("Hello, Newman") == 0

def test_value_how_you_doing():
    assert bank.value("how you doing?") == 20

def test_value_whats_happening():
    assert bank.value("what's happening?") == 100

def test_value_whats_up():
    assert bank.value("what's up?") == 100

def test_value_invalid_input():
    assert bank.value("invalid input") == 100

