import tkinter.filedialog

# from_filename = tkinter.filedialog.askopenfilename()

# to_filename = tkinter.filedialog.asksaveasfilename()

# ''' Read from_file'''
# from_file = open(from_filename, 'r')
# contents = from_file.read()
# from_file.close()


# '''Now write content from from_file to to_file'''
# to_file = open(to_filename, 'w')
# to_file.write('Copy\n')

# to_file.write(contents)
# to_file.close()



def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE HERE
    for s in sentences:
        file.write(s)
    file.write('\n')

    '''# Another way
    file.write(sentences)
    
    '''

# Calling function that writes sentences to file
w_to_file = tkinter.filedialog.asksaveasfilename()
write_to_filename1 = open(w_to_file, 'w')

sentences_to_write = '''Hello there!
This is my new Python Program.
To write to a file.
See you!
'''

write_to_file(write_to_filename1, sentences_to_write)

write_to_filename1.close()

