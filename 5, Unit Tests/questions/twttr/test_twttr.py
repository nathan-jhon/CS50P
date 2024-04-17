from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"

def test_shorten_with_vowels():
    assert shorten("apple") == "ppl"
def test_shorten_with_numbers():
    assert shorten("12345") == "12345"

def test_shorten_with_punctuation():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"

def test_shorten_mixed_case():
    assert shorten("apple") == "ppl"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_only_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_with_special_characters():
    assert shorten("hello, world!") == "hll, wrld!"

