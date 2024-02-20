flanders_filename = 'In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')
for line in flanders_file:
	print(line, end='')
	
flanders_file.close()



print('\n*******Readline**********')
flanders_file = open(flanders_filename, 'r')
print(flanders_file.readline(), end='')
print(flanders_file.readline(), end='')
print(flanders_file.readline(), end='')
line = flanders_file.readline()
print(line.rstrip('\n'))
flanders_file.close()

print('\n********Readlines*********')
flanders_file = open(flanders_filename, 'r')
print(flanders_file.readlines())

flanders_file.close()

print('\n******Read File***********')
flanders_file = open(flanders_filename, 'r')
print(flanders_file.read())

flanders_file.close()

