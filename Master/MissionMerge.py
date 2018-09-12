import itertools
import ConfigParser
import json
import os, sys

def file_len(fname):
    return sum(1 for line in open(fname))

def check_if_exists(inputfname):
    try:
        if os.stat(inputfname).st_size > 0:
            print "The file was found successfully"
        else:
            print "The inputted file is empty"
            exit(1)
    except OSError:
        print "No file!"
        exit(1)


def first_file(inputfname, output):
    check_if_exists(inputfname)
    lengthoffile = file_len(inputfname)
    with open(output, 'w') as outfile:
        with open(inputfname) as infile:
            for line in itertools.islice(infile, 0, lengthoffile - 2):
                outfile.write(line)

def middle_file(inputfname, output):
    counter = file_len(output) - 1
    i = 0
    j = 1
    check_if_exists(inputfname)
    with open(output, 'a') as outfile:
        with open(inputfname) as infile:
            lengthoffile = file_len(inputfname)
            for line in itertools.islice(infile, 2, lengthoffile - 2):
                i = 0
                while (line[i] >= '0' and line[i] <='9'):
                    i += 1
                new_string = str(counter) + line[i:]
                outfile.write(new_string)
                counter +=1

def last_file(inputfname, output):
    counter = file_len(output) - 1
    with open(output, 'a') as outfile:
        with open(inputfname) as infile:
            lengthoffile = file_len(inputfname)
            for line in itertools.islice(infile, lengthoffile - 2, lengthoffile):
                i = 0
                while (line[i] >= '0' and line[i] <='9'):
                    i+=1
                new_string = str(counter) + line[i:]
                outfile.write(new_string)
                counter += 1

config = ConfigParser.ConfigParser()
config.read('Points.conf')
inputs = config.get('Missions', 'input')
inputs = json.loads(inputs)
output = config.get('Missions', 'output')


first_file(inputs[0], output)
a = 1
for input in inputs[1:len(inputs)]:
    middle_file(inputs[a], output)
    a += 1
last_file(inputs[0], output)