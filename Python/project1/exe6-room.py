#accepts URL from user and destination file name from user calling the script
#utilize requests to make an http request to make an HTTP request to the given URL
# has optional flag to state whether or not the response should be JSON or HTML
# writes the contents of the page out to the destination

            # THIS VERSION DOESNT WORK
import requests
from argparse import ArgumentParser
import shutil

parser = ArgumentParser(description='accepts url and destination file name and also JSON or HTML')
parser.add_argument('url', help='write url')
parser.add_argument('destination', help='enter path for file name')
parser.add_argument('--type', default='HTML')
args = parser.parse_args()
print(args)
url = args.url


res = requests.get(url)

if res.status_code == 200:
    content = res.text
    #print(content.)
else:
    print(f"Request failed with status code {res.status_code}")

