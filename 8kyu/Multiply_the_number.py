"""
You have to multiply each number by 5 raised to the number of digits of each numbers
"""
# Operate. Power (base,exponent)
def multiply(n):
    return n * pow(5, len(str(abs(n))))