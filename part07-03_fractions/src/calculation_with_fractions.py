from fractions import Fraction

def fractionate(amount: int):
    
    one = Fraction(1, 1)
    
    part = one / amount

    return [part for _ in range(amount)]

