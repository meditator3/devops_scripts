import os
import requests # this we need to install via python packges in the tabs below
#it didn't really work in the pychar, but through command line it will work
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='get current weather information')
parser.add_argument('zip', help='zip/postal code to get weather for') # we need to get the zip code to know from where to get the weather
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is US') #-- is flag, its an option

args = parser.parse_args() # this will save the arguments we imported through the parser above

api_key = os.getenv('OWN_API_KEY') # my own key

if not api_key:
    print("ERROR: no 'OWN_API_KEY' provided")
    sys.exit(1) # this will exit the script with an error (1)


url = f"http://api.openweathermap.org/data/2.5/weather=?zip={args.zip},{args.country}%appid={api_key}"

res = requests.get(url) # this is a get request, which calls the url.

if res.status_code != 200: #200 is good, the website responds to me
    print(f"Error talking to weather provider:{res.status_code}" )
    sys.exit(1)

print(res.json) # we print the response in json
