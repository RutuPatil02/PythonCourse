list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1[-1])

'''
def interrupted(s):
    s[-1] = "-"

greeting = "how are you"
interrupted(greeting)
print(greeting)

'''



def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          print(s[i])
          i = i + 1

    return result

print(mystery('abc123'))
# >>>abc
print(mystery('123'))
# >>>
print(mystery('123abc'))
# >>>

# gives error
# print(mystery('abc')) 


"""

We say that lists are mutable: they can be modified. All the other types we have seen so far 
(str, int, float and bool) are immutable: they cannot be modified.

Here are several examples of lists being modified:

>>> classes = ['chem', 'bio', 'cs', 'eng']
>>>
>>> # Elements can be added:
>>> classes.append('math')
>>> classes
['chem', 'bio', 'cs', 'eng', 'math']
>>>
>>> # Elements can be replaced:
>>> classes[1] = 'soc'
>>> classes
['chem', 'soc', 'cs', 'eng', 'math']
>>>
>>> # Elements can be removed:
>>> classes.pop()
'math'
>>> classes
['chem', 'soc', 'cs', 'eng']
Aliasing
Consider the following code:

>>> lst1 = [11, 12, 13, 14, 15, 16, 17]
>>> lst2 = lst1
>>> lst1[-1] = 18
>>> lst2
[11, 12, 13, 14, 15, 16, 18]



"""