def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    sun1=a%10
    sun2=a//10
    sun=sun1*10+sun2*1
    if a>sun or a==sun:
        sum="True"
    else  :
        sum="False"    
    return sum
print(main(25))    