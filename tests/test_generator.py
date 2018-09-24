import unittest, math
from tools import tempconversion

def test_kelvin_to_fahrenheit():
    t_to_k = math.ceil(tempconversion.kelvin_to_fahrenheit(4))
    assert t_to_k == -452

def test_kelvin_to_celsius():
    t_to_k = math.ceil(tempconversion.kelvin_to_celsius(4))
    assert t_to_k == -269

def test_kelvin_to_rankine():
    t_to_k = math.ceil(tempconversion.kelvin_to_rankine(4))
    assert t_to_k == 8

def test_rankine_to_fahrenheit():
    t_to_k = math.ceil(tempconversion.rankine_to_fahrenheit(4))
    assert t_to_k == -455

def test_rankine_to_celsius():
    t_to_k = math.ceil(tempconversion.rankine_to_celsius(4))
    assert t_to_k == -270

def test_rankine_to_kelvin():
    t_to_k = math.ceil(tempconversion.rankine_to_kelvin(4))
    assert t_to_k == 3

def test_celsius_to_kelvin():
    t_to_k = math.ceil(tempconversion.celsius_to_kelvin(4))
    assert t_to_k == 278

def test_celsius_to_rankine():
    t_to_k = math.ceil(tempconversion.celsius_to_rankine(4))
    assert t_to_k == 499

def test_celsius_to_fahrenheit():
    t_to_k = math.ceil(tempconversion.celsius_to_fahrenheit(4))
    assert t_to_k == 40

def test_fahrenheit_to_kelvin():
    t_to_k = math.ceil(tempconversion.fahrenheit_to_kelvin(4))
    assert t_to_k == 258

def test_fahrenheit_to_celsius():
    t_to_k = math.ceil(tempconversion.fahrenheit_to_celsius(4))
    assert t_to_k == -15

def test_fahrenheit_to_rankine():
    t_to_k = math.ceil(tempconversion.fahrenheit_to_rankine(4))
    assert t_to_k == 464
