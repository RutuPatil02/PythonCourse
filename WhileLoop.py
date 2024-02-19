def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer


        
def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel


def sum_even_numbers(num1, num2, n):
    """(number, number, number) ->number
    Return sum of even numbers from range num1 to num2 with step n.

    >>>sum_even_numbers(1,10,2)
    25
    >>>sum_even_numbers(10,100,10)
    550
        
    """
    sum_num = 0
    i = num1
    while i <= num2:
        if i % 2 == 0:
            sum_num = sum_num + i
        i = i + n

    return sum_num

print(sum_even_numbers(524,10508,2))
# print(sum_even_numbers(10,100,10))



def sum_odd_numbers(num1, num2):
    """(number, number, number) ->number
    Return sum of odd numbers from range num1 to num2.

    >>>sum_odd_numbers(1523,10503)
    54002753
    >>>sum_odd_numbers(1,10)
    25
    >>>sum_odd_numbers(5,10)
    21 
    """
    sum_num = 0
    i = num1
    while i <= num2:
        if i % 2 != 0:
            sum_num = sum_num + i

        i = i + 1

    return sum_num

print(sum_odd_numbers(1523,10503))





playlist = ['lol', 'abc', 'dfg', 'lol','dgf','lol', 'lol', 'dfg','lol']
while playlist.count('lol') > 3:
        playlist.pop(playlist.index('lol'))

print(playlist)

