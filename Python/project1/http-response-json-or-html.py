# this script gets url from user using args,
# requests package is used to make an http request
# use optional flag for JSON or HTML output, HTML by default
#  shows content of page

import requests
from argparse import ArgumentParser
import sys
import json

parser = ArgumentParser(description='this gets url from user and displays content in either json or HTML format')
parser.add_argument('--format', help='input JSON or HTML for formatting display of webpage url, HTML defaults', default='HTML')
parser.add_argument('--url', help='your url link') # we use just args.url to access values
args = parser.parse_args()
#
#
# if not args.url:
#     print("You need to input URL")
#     sys.exit(1)
#
# res = requests.get(args.url)
# res_json = res.json()
#if args.format !="JSON":
 #   print(res)
#else: # will copy content of res to a file, and then translate to json using json package
 #   print(res_json)


# AI SCRIPT
def fetch_url_data(url, output_format):
    # Make the HTTP request to the URL
    response = requests.get(url)

    # Check if the user wants the output in JSON format
    if output_format.upper() == 'JSON':
        # Attempt to get JSON data directly
        try:
            data = response.json()
            print(data)
        except ValueError:
            # In case the response is not in JSON format
            print("The URL did not return JSON data.")
    else:
        # If the user asks for HTML, or any format other than JSON
        print(response.text)

if __name__ == "__main__":
    # Set up argument parsing
    parser = ArgumentParser(description="Fetch URL content and display in specified format.")
    parser.add_argument('--url', help="URL to fetch data from", required=True)
    parser.add_argument('--format', help="Format of output: JSON or HTML", default='HTML')
    args = parser.parse_args()

    # Fetch and display the URL data in the specified format
    fetch_url_data(args.url, args.format)