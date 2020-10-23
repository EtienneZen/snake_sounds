def fahrenheit_to_celsius (temp):       #Converts fahrenheit to celsius
    """Converts fahrenheit to celsius"""
    return int((temp - 32) * (5 / 9))

def celsius_to_fahrenheit (temp):       #Converts celsius to fahrenheit
    """Converts celsius to fahrenheit"""
    return int(temp * (9/5) + 32)


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))
