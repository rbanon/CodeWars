"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
"""
def abbrev_name(name):
    n, s = name.upper().split()
    n = n[0]
    s = s[0]
    return n + "." + s