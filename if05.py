def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    sun=0
    if a<0:
        sun+=1
    if b<0:
        sun+=1
    if c<0:
        sun+=1            
    return sun
print(main(5,-6,8))    
    