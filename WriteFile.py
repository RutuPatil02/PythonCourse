import tkinter.filedialog

from_filename = tkinter.filedialog.askopenfilename()

to_filename = tkinter.filedialog.asksaveasfilename()

''' Read from_file'''
from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()


'''Now write content from from_file to to_file'''
to_file = open(to_filename, 'w')
to_file.write('Copy\n')

to_file.write(contents)
to_file.close()



