from plates import is_valid

def test_valid_plate():
    assert is_valid("AB1234") == True

def test_too_short_plate():
    assert is_valid("A") == False

def test_too_long_plate():
    assert is_valid("ABCDEFG") == False

def test_first_two_characters_not_letters():
    assert is_valid("12ABCD") == False
def test_contains_whitespace():
    assert is_valid("AB CD23") == False

def test_contains_mixed_case():
    assert is_valid("AbCdEf") == True


def test_all_letters():
    assert is_valid("ABCDEF") == True

def test_empty_string():
    assert is_valid("") == False
def test_zero_placement():
    assert is_valid("AB0234") == False

def test_contains_dot():
    assert is_valid("AB.CD") == False

def test_contains_space():
    assert is_valid("AB CD") == False

def test_contains_exclamation():
    assert is_valid("AB!CD") == False

def test_contains_question_mark():
    assert is_valid("AB?CD") == False

