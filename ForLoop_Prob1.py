def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)


print(mystery('livil'))


def shift_right(L):
    ''' (list) -> list

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''
    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
        i = i + 1

    L[0] = last_item
    return L

print(shift_right(['a', 'b', 'c', 'd']))


def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
    

    ''' #Another way
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
    '''
    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))



def contains(value, lst):
   """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
   True
   """

   found = False  # We have not yet found value in the list.

   for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True

   ''' # Another way
   for sublist in lst:
        if value in sublist:
            found = True
   '''
   return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))


def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """
    flanders_file = open(file, 'r')
    matches = []

    for line in flanders_file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    flanders_file.close()
    return matches

print(lines_startswith('In Flanders Fields.txt', 'T'))


def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE HERE
    for s in sentences:
        file.write(s)


