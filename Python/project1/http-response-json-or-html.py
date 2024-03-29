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


if not args.url:
    print("You need to input URL")
    sys.exit(1)

res = requests.get(args.url)

if args.format !="JSON":
   print(res.text)
else: # will copy content of res to a file, and then translate to json using json package
   try:
      res_json = res.json() # if not put in this block and won't have JSON will throw an error instantly
      print(json.dumps(res_json, indent=4))
   except ValueError:
#             # In case the response is not in JSON format
       print("The URL did not return JSON data.")


# to test  HTML:
# python http-response-json-or-html.py --url https://google.com --format HTML
# to test JSON
#$ python http-response-json-or-html.py --url http://ip.jsontest.com/ --format JSON
#{
#    "ip": "147.235.194.23"
#}
# AI SCRIPT
# def fetch_url_data(url, output_format):
#     # Make the HTTP request to the URL
#     response = requests.get(url)
#
#     # Check if the user wants the output in JSON format
#     if output_format.upper() == 'JSON':
#         # Attempt to get JSON data directly
#         try:
#             data = response.json()
#             print(data)
#         except ValueError:
#             # In case the response is not in JSON format
#             print("The URL did not return JSON data.")
#     else:
#         # If the user asks for HTML, or any format other than JSON
#         print(response.text)
#
# if __name__ == "__main__":
#     # Set up argument parsing
#     parser = ArgumentParser(description="Fetch URL content and display in specified format.")
#     parser.add_argument('--url', help="URL to fetch data from", required=True)
#     parser.add_argument('--format', help="Format of output: JSON or HTML", default='HTML')
#     args = parser.parse_args()
#
#     # Fetch and display the URL data in the specified format
#     fetch_url_data(args.url, args.format)
