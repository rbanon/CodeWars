"""
Kids (-14yo) drink toddy.
Teens (-18yo) drink coke.
Young adults (-21yo) drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.
"""
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    return "drink whisky"
