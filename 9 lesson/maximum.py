
def maximum(*args):
    maxi='start'
    """
    >>> maximum(3, 2, 8)
    8
    >>> maximum(1, 5, 9, -2, 2)
    9
    >>> maximum()    
    """
    for i in args:
        if maxi=='start':
            maxi=i
            continue
        if i>maxi:
            maxi=i
    return maxi

print(maximum(3,2,8))
print(maximum(1, 5, 9, -2, 2))
print(maximum(-1,-3,-5))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
