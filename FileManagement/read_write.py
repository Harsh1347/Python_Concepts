# Readin Files
# METHOD 1
# make sure to close the file after using this method

f = open('text.txt','r') #default is opening for reading. r-> reading w-> writing a-> appending r+ -> read write both
print(f.name)
f.close()

# METHOD 2 (Context Manager)
# no need to explicitly close the file

with open('text.txt','r') as f:
    f_contents = f.readline()
    print(f_contents,end='') # end of the line is '' and not '\n'

    f_contents = f.readline()
    print(f_contents)

# for large text files we can iterate using loop

with open('text.txt','r') as f:
    print(f.tell()) # f.tell tells the position at which we are
    f.seek(10) # seek is used to manipulate the position
    print(f.tell())
    for line in f:
        print(line,end='') 
    print(f.tell())

# Writing in File

with open('test2.txt','w') as f:
    f.write('Hello test2')

# copying content of one file to another

with open('text.txt','r') as rf:
    with open('text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)