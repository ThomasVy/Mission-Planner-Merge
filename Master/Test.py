import itertools

def file_len(fname):
    return sum(1 for line in open(fname))

def check_if_empty(inputfname):
    if file_len(inputfname) == 0:
        return True

def first_file(inputfname, outputfname):
    if check_if_empty(inputfname):
        print 'you inputted an empty text file!'
        exit(1)
    with open(outputfname, 'w') as outfile:
        lengthoffile = file_len(inputfname)
        with open(inputfname) as infile:
            for line in itertools.islice(infile,0, lengthoffile - 2):
                outfile.write(line)

def second_file(inputfname, inputfname2, outputfname):
    counter = file_len(inputfname2)-3
    i = 1
    j = 1
    if check_if_empty(inputfname):
        print 'you inputted an empty text file!'
        exit(1)
    with open(outputfname, 'a') as outfile:
        with open(inputfname) as infile:
            lengthoffile = file_len(inputfname)
            for line in itertools.islice(infile, 2, lengthoffile-2):
                if i > 9:
                    j = 2
                new_string = str(counter) + line[j:]
                outfile.write(new_string)
                counter +=1
                i += 1
        with open(inputfname2) as infile:
            lengthoffile = file_len(inputfname2)
            for line in itertools.islice(infile, lengthoffile - 2, lengthoffile):
                if i > 9:
                    j = 2
                new_string = str(counter) + line[j:]
                outfile.write(new_string)
                counter += 1
                i += 1

x = raw_input('Please enter the name of the first waypoints file. Do not foget the file type! (.waypoints)')
y = raw_input('Please enter the name of the second waypoints file. Do not foget the file type! (.waypoints)')

first_file(x,'Test3.waypoints')
second_file(y, x, 'Test3.waypoints')