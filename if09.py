from re import S


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
    s1=a%10
    s2=a//10
    s=s1*10+s2*1
    if a>=s:
        x="True"
    else :
        x="False"    
    return x
print(main(21))    