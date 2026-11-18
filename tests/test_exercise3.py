from exercise3 import average, first_word, percent

def test_average_empty():
    assert average([]) == 0

def test_average_normal():
    assert average([1, 2, 3]) == 2.0

def test_first_word_empty():
    assert first_word("") == ""

def test_first_word_normal():
    assert first_word("Hello World") == "Hello"

def test_percent_zero_total():
    assert percent(5, 0) == 0

def test_percent_normal():
    assert percent(5, 10) == 50.0
