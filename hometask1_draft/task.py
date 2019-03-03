def function(text, sep):
    '''
    >>> function('ThisIsCamelCased',_)
    'this_is_camel_cased'
    
    >>> function('ThisIsCamelCased',-)
    'this-is-camel-cased'
    '''
    lst=[]
    for i in text:
        if text[0]==i:
            lst.append(i)
            continue
        if i.isupper():
            lst.append(sep)
            lst.append(i.lower)
    result=''.join(lst)
    return result
            
print(function('ThisIsCamelCased','_'))


#if __name__ == '__main__':
 #   import doctest
  #  doctest.testmod()
    
