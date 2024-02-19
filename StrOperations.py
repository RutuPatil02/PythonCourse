
# We can compare two strings for their dictionary order, comparing them letter by letter:
print('abracadabra' < 'ace')
# >> True
print('abracadabra' > 'ace')
# >>> False
print('a' <= 'a')
# >>> True
print('A' < 'B')
# >>> True
print('a' < 'A')
# >>> False

# Testing For Substrings
# The operator in checks whether a string appears anywhere inside another one (that is, whether a string is a substring of another).

print('c' in 'aeiou')
# >>> False
print('cad' in 'abracadabra')
# >>> True

s = 'Call Me Maybe'
print(s[-13:-9])
print(s[0:4])

s = s[0:-5] + 'Perhaps'
print(s)

