import requests
from argparse import ArgumentParser
import os

parser = ArgumentParser(description='accepts url and destination file name and also JSON or HTML')
parser.add_argument('url', help='write url')
parser.add_argument('destination', help='enter path for file name')
parser.add_argument('--format', default='HTML', help='insert format-JSON or HTML default')
args = parser.parse_args()

#print(args.format) # this will print the flags/switch

url = args.url
res = requests.get(url)

if res.status_code == 200:
    if args.format == "HTML":
        content = res.text
        print(content)
        with open(args.destination, 'a') as f: # use 'a' and not r otherwise it won't create a new file
            f.write(content)
    elif args.format =="JSON":
        content = res.json()
        with open(args.destination, 'a') as f:
            f.write(content)
        print(content)
else:
    print(f"Request failed with status code {res.status_code}")
