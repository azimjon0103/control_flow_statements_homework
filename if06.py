def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    sun1=0
    sun2=0
    if a<0:
        sun1+=1
    if b<0:
        sun1+=1
    if c<0:
        sun1+=1   
    sun=0
    if a>0:
        sun2+=1
    if b>0:
        sun2+=1
    if c>0:
        sun2+=1         
    if sun1>sun2:
        s="there are a lot of negative numbers"
    if sun1<sun2:
        s="there are a lot of positive numbers"   
    return s    
print(main(-9,5,-3))    