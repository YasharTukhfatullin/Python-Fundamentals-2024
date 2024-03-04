"""
Dictionary Comprehension = create dictionaries using an expression can replace for loops and certain lambda functions.

dictionary = {key: expression for (key, value) in iterable}
dictionary = {key: expression for (key, value) in iterable if conditional}
dictionary = {key: (if/else) for (key, value) in iterable}
dictionary = {key: function(value) for (key, value) it iterable}
"""

cities_in_fahrenheit = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

# dictionary = {key: expression for (key, value) in iterable}
cities_in_celsius = {
    key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_fahrenheit.items()
}
print(cities_in_celsius)
print("=============================================")

weather = {
    "New York": "snowing",
    "Boston": "sunny",
    "Los Angeles": "sunny",
    "Chicago": "raining",
}

# dictionary = {key: expression for (key, value) in iterable if conditional}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)
print("=============================================")

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

# dictionary = {key: (if/else) for (key, value) in iterable}
desc_cities = {
    key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities.items()
}
print(desc_cities)
print("=============================================")


def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"


new_cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

# dictionary = {key: function(value) for (key, value) it iterable}
desc_new_cities = {key: check_temp(value) for (key, value) in new_cities.items()}
print(desc_new_cities)
