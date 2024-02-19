import math


"""
print(dir(math))
help(math.ceil)

print(math.ceil(84.2))
print(len(''))

print(int('3') in [len('a'), len('ab'), len('abc')])
print(len('mom') in [1, 2, 3])
# print([1, 2, 3] in len('mom'))
print(len([1, 2, 3]) == len(['a', 'b', 'c']))
print('3' in [1, 2, 3])
print('a' in ['mom', 'dad'])


"""

values = []
for num in range(1,4):
    values.append(num * 3)
print(values)

for num in range(3,20,8):
    print(num)

playlist = ['lol', 'abc', 'dfg', 'lol','dgf','lol', 'lol', 'dfg','lol']
# while playlist.count('lol') > 3:
#     playlist.pop(playlist.index('lol'))

while playlist.count('lol') > 3:
    playlist.remove('lol')

print(playlist)



numbers = [1, 4, 3]
numbers.sort()
# numbers.reverse()
print(numbers)

veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)


'''

s1 = 'banana'
s2 = 'ana'

print(s1.find(s2, s1.find(s2)+1))
print(s1.find(s2,2))

t1 = 'apple'
t2 = 'p'

print(t1.find(t2, t1.find(t2)+1))
print(t1.find(t2,2))
'''

digits = '0123456789'
result = 100

for digit in digits:
    result = result - int(digit)

print(result)



s = 'carrot'
print(s[-6:3])
print(s[:3])

'''
prefix = 'mad'
print(prefix[:1] + prefix[1:3] + prefix[-2] + prefix[0])

print('abc123'.isalnum())
print('apple'.upper().isupper())
print('apple'.upper().islower())



'''
