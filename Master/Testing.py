import itertools
#filenames = ['testtxt2.txt', 'testtxt.txt']

def file_len(fname):
    return sum(1 for line in open(fname))

x = 'testtxt2.txt'
y = 'testtxt.txt'

def check_if_empty(inputfname):
    if file_len(inputfname) == 0:
        return True
def first_file(inputfname, outputfname):
    if check_if_empty(inputfname):
        print 'you inputted an empty text file!'
    with open(outputfname, 'w') as outfile:
        lengthoffile = file_len(inputfname)
        with open(inputfname) as infile:
            for line in itertools.islice(infile,0, lengthoffile - 2):
                outfile.write(line)

def second_file(inputfname, outputfname,x):
    counter =file_len(x)-1
    if check_if_empty(inputfname):
        print 'you inputted an empty text file!'
    with open(outputfname, 'a') as outfile:
        lengthoffile = file_len(inputfname)
        with open(inputfname) as infile:
            for line in itertools.islice(infile,2, lengthoffile-2):
                i =0
                while (line[i] != ' '):
                    i +=1
                new_string = str(counter)+ (line[i:])
                outfile.write(new_string)
                counter +=1



first_file(x,'output.txt')
second_file(y,'output.txt',x)
