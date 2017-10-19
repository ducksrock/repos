def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """

    punctuationlist = ["!", "?", ".", "-", ","]
    newtext = ""

    for character in text:
       
        if  not (character in punctuationlist):
            newtext += character

    return newtext

    
def remove_spaces(text):
    """This function is used to remove leading and trailing spaces from a string.
    It takes a string and returns a new string with does not have leading and
    trailing spaces. For example:

    >>> remove_spaces("  Hello!  ")
    'Hello!'
    >>> remove_spaces("  Python  is  easy!   ")
    'Python  is  easy!'
    >>> remove_spaces("Python is easy!")
    'Python is easy!'
    >>> remove_spaces("")
    ''
    >>> remove_spaces("   ")
    ''
    """
    
    first = 0
    for characters in text:
        if characters == ' ':
            first += 1
        else:
            break

    procedure1 = text[first:]
    reversetext = procedure1[::-1]

    second = 0
    for characters in reversetext:
        if characters == ' ':
            second += 1
        else:
            break

    procedure2 = reversetext[second:]
    polaropposite = procedure2[::-1]
    
    return polaropposite
    


def normalise_input(user_input):
    """This function removes all punctuation, leading and trailing
    spaces from a string, and converts the string to lower case.
    For example:

    >>> normalise_input("  Go south! ")
    'go south'
    >>> normalise_input("!!! tAkE,. LAmp!?! ")
    'take lamp'
    >>> normalise_input("HELP!!!!!!!")
    'help'
    """
    NoPunctuation = remove_punct(user_input)
    NoSpaces = remove_spaces(NoPunctuation)
    print(NoSpaces)
    Lowercase = NoSpaces.lower()

a = input()
print(normalise_input(a))