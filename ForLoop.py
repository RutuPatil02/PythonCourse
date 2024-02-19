def count_vowels(s):
    """ (str) -> int

    Return the number of vowels in s. Do not treat letter y as a vowel
    
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0    
    """

    num_vowels = 0
    
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels


def collect_vowels(s):
    """ (str) -> str

    Return the vowels from s.  Do not treat the letter
    y as a vowel.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    """

    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels



def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that     
    appear atleast once in s2. The characters in the result 
    will appear in the same order as they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''

    res = ''    
    for i in s1:
        if i in s2:
            res = res + i

    return res



def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item      
    

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats