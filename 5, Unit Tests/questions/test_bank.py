# Import the bank module
import bank

# Define test functions for the value function
def test_value_hello():
    # Check if the value function returns 0 for "Hello"
    assert bank.value("Hello") == 0

def test_value_hello_uppercase():
    # Check if the value function returns 0 for "HELLO"
    assert bank.value("HELLO") == 0

def test_value_hello_newman():
    # Check if the value function returns 0 for "Hello, Newman"
    assert bank.value("Hello, Newman") == 0

def test_value_how_you_doing():
    # Check if the value function returns 20 for "how you doing?"
    assert bank.value("how you doing?") == 20

def test_value_whats_happening():
    # Check if the value function returns 100 for "what's happening?"
    assert bank.value("what's happening?") == 100

def test_value_whats_up():
    # Check if the value function returns 100 for "what's up?"
    assert bank.value("what's up?") == 100

def test_value_invalid_input():
    # Check if the value function returns 100 for "invalid input"
    assert bank.value("invalid input") == 100

