"""
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
I love you
a little
a lot
passionately
madly
not at all
"""
def how_much_i_love_you(nb_petals):
    s = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return s[nb_petals % len(s) - 1] 