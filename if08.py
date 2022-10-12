def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if  a%2==1 and a>9:
        sun="two-digit odd number"
    if  a%2==0 and a>9:
        sun="two-digit even number"  
    if  a%2==1 and a<-9:
        sun="two-digit odd number"
    if  a%2==0 and a<-9:
        sun="two-digit even number" 
    if  a%2==1 and a>99:
        sun="three-digit odd number" 
    if  a%2==0 and a>99:
        sun="three-digit even number"  
    if  a%2==1 and a<-99:
        sun="three-digit odd number" 
    if  a%2==0 and a<-99:
        sun="three-digit even number"      
    return sun
print(main(-322))    