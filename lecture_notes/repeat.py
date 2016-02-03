import sys

def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    #faster because * calculates len of object once, + does it each time + is called
    #+ and * are called "overloaded" operators because they mean different things for numbers vs strings

    if exclaim:
        result = result + '!!!'
    return result

def main():
    #print repeat('Yay', False)      ## YayYayYay
    #print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!
    name = sys.argv[1]
    if name == 'Guido':
        print repeeeet(name,False) + '!!!'
    else:
       	print repeat(name,True)

if __name__ == '__main__':
    main()