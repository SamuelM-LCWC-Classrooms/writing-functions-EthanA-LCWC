import task
from unittest.mock import patch
import pytest

def test_temperature_converter_celsius_to_fahrenheit():
    assert task.temperature_converter(100, "C") == "212 F"
    assert task.temperature_converter(0, "C") == "32 F"
    assert task.temperature_converter(-40, "C") == "-40 F"
    assert task.temperature_converter(50, "C") == "122 F"
    assert task.temperature_converter(25, "C") == "77 F"

def test_temperature_converter_fahrenheit_to_celsius():
    assert task.temperature_converter(32, "F") == "0 C"
    assert task.temperature_converter(68, "F") == "20 C"
    assert task.temperature_converter(-40, "F") == "-40 C"
    assert task.temperature_converter(212, "F") == "100 C"

def test_reverse_basic_strings():
    assert task.reverse("hello") == "olleh"
    assert task.reverse("world") == "dlrow"
    assert task.reverse("Python") == "nohtyP"
    assert task.reverse("OpenAI") == "IAnepO"

def test_reverse_single_character():
    assert task.reverse("a") == "a"
    assert task.reverse("Z") == "Z"

def test_reverse_empty_string():
    assert task.reverse("") == ""

def test_reverse_palindrome():
    assert task.reverse("madam") == "madam"
    assert task.reverse("racecar") == "racecar"

def test_reverse_special_characters():
    assert task.reverse("12345") == "54321"
    assert task.reverse("!@#$%") == "%$#@!"
    assert task.reverse("hello!") == "!olleh"
    
def test_fib_base_cases():
    assert task.fib(0) == 0
    assert task.fib(1) == 1

def test_fib_small_numbers():
    assert task.fib(2) == 1
    assert task.fib(3) == 2
    assert task.fib(4) == 3
    assert task.fib(5) == 5

def test_fib_larger_numbers():
    assert task.fib(6) == 8
    assert task.fib(7) == 13
    assert task.fib(8) == 21
    assert task.fib(10) == 55

def test_fib_edge_case():
    assert task.fib(20) == 6765
