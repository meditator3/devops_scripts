# this is supposed to be a script in linux or cli
# to just reverse the order of lines via a filename
#!/usr/bin/env python3.6
import argparse # library which can parse arguments

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()
print(args)

