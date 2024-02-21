
# print(3 // 4)
# print(8 % 6)

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
  
    result = []
    for k in L:
       if k in d:
          result.append(k)

    return result


print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))

def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] = d[c] + 1

           

# letter_counts = {'i': 0, 'r': 5, 'e': 1}
# add_to_letter_counts(letter_counts, 'eerie')
# print(letter_counts)



def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
      for col in range(len(L)):
          if row == col:
                diagonal.append(L[row][col])
          else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)


# print(get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]]))



def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d: 
             result = result + 1

    return result

# print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
# print(count_values_that_are_keys({1: 1}))
# print(count_values_that_are_keys({1: 2}))
# print('*******************')



def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.     Count how manytimes letter appears in s1 and in s2, and ret    urn the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter),s2.count(letter))


print(count_max_letters('hello', 'world', 'l'))
print(count_max_letters('cat', 'abracadabra', 'a'))
print('*********************')



d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
L = []
for k in d:
    L.extend(d[k])

total = len(L)

# print(total)


# ***********************************************
d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE
#d['a'].append(2)
d['a'].insert(1,2)
d['a'].sort()

print(d)
# >>> {'a': [1, 2, 3], 'b': [5, 7]}

# **********************************************
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
    for k in d:
        if v in d[k]:
            found = True
    return found


print(contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}))
print(contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return (time + utc_offset)%24

'''

print(time_from_utc(+0, 12.0))
print(time_from_utc(+1, 12.0))
print(time_from_utc(-1, 12.0))
print(time_from_utc(+6, 6.0))
# 12.0
print(time_from_utc(-7, 6.0))
# 23.0
print(time_from_utc(-1, 0.0))
#  23.0
print(time_from_utc(-1, 23.0))
#  22.0
print(time_from_utc(+1, 23.0))

'''