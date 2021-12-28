"""
Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
Division by zero should return an empty value.
"""
def remainder(a,b):
    list =[a,b]
    list = sorted(list, reverse = True)
    num = list[0] # Bigger value
    den = list[1] #Smaller value
    if num >= 0 and den >= 0: #+num +den (or 0)
        if num == 0 or den == 0:
            return None
        else:
            return num%den
    else: #Any negative
        if den == 0:
            return 0
        else: # -num +den
            return num%den