#!/usr/bin/env python 3.6
# this is supposed to be a script in linux or cli
# this can be a script that runs without .py!
# much like with help/manual like in linux commands
# that can be utilized like a command inside linux only!
# this one uses filename, to reverse its lines. that's what the script does

# to just reverse the order of lines via a filename

import argparse # library which can parse arguments

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read') # this adds switches to the command/arg
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0') # adding version number
args = parser.parse_args()
print(args)
# can use this file-reverse-CLI.py -h to see the help from the above flags/switches
#open the file
# args is the argument of the user, .filename is the name we've set on the first add_arg
# error handeling with try, like js

with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse() # reserved function of python
        if args.limit:
            lines = lines[:args.limit] # we've set to read from line 0 to limit of argument the user have set
        for line in lines:
            print(line.strip()[::-1]) # reversed order and index

