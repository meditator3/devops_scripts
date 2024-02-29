# this is supposed to be a script in linux or cli
# to just reverse the order of lines via a filename

import argparse # library which can parse arguments
import sys
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read') # this adds switches to the command/arg
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0') # adding version number
args = parser.parse_args()
print(args)

#open the file
# args is the argument of the user, .filename is the name we've set on the first add_arg
# error handeling with try, like js
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print("Error: this file does not exist! {err}")
    #to make it as an error, otherwise it won't be marked as an error
    sys.exit(1)
else:
    with f:
       lines = f.readlines()
       lines.reverse() # reserved function of python
    if limit:
            lines = lines[:limit] # we've set to read from line 0 to limit of argument the user have set
    for line in lines:
            print(line.strip()[::-1]) # reversed order and index

