def celsius_to_fahrenheit(c):
    'Degrees Celsius (C) to degrees Fahrenheit (F)'
    return (c * 1.8) + 32.0

def celsius_to_kelvin(c):
    'Degrees Celsius (C) to degrees Kelvin (K)'
    return c + 273.15

def celsius_to_rankine(c):
    'Degrees Celsius (C) to degrees Rankine (R)'
    return (c * 1.8) + 491.67

def fahrenheit_to_celsius(f):
    'Degrees Fahrenheit (F) to degrees Celsius (C)'
    return (f - 32.0) * 0.555556

def fahrenheit_to_kelvin(f):
    'Degrees Fahrenheit (F) to degrees Kelvin (K)'
    return (f * 0.555556) + 255.37

def fahrenheit_to_rankine(f):
    'Degrees Fahrenheit (F) to degrees Rankine (R)'
    return f + 459.67

def kelvin_to_celsius(k):
    'Degrees Kelvin (K) to degrees Celsius (C)'
    return k - 273.15

def kelvin_to_fahrenheit(k):
    'Degrees Kelvin (K) to degrees Fahrenheit (F)'
    return (k - 255.37) * 1.8

def kelvin_to_rankine(k):
    'Degrees Kelvin (K) to degrees Rankine (R)'
    return k * 1.8

def rankine_to_celsius(r):
    'Degrees Rankine (R) to degrees Celsius (C)'
    return (r - 491.67) * 0.555556

def rankine_to_fahrenheit(r):
    'Degrees Rankine (R) to degrees Fahrenheit (F)'
    return r - 459.67

def rankine_to_kelvin(r):
    'Degrees Rankine (R) to degrees Kelvin (K)'
    return r * 0.555556
