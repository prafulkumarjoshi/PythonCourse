def format_name(f,l):
    f1 = f.title()
    l1 = l.title()
    print(f1,l1)
    print(f,l)
    return f1, l1
    
print(format_name("sachin","tendulkAR")[0])

def is_leap_year(year):
    """Determine if a year is a leap year

    Args:
        year (int): year

    Returns:
        boolean: returns True if the year is leap or False if it is not
    """
    # Write your code here. 
    # Don't change the function name.
    if year%4==0:
        if year%100==0 and year%400!=0:
            return False
        else:
            return True
    else:
        return False