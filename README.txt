Welcome to the Brett Sports Workout Tracker.

If you want to configure your own environmental variables, you need to: 

1. Access config.ini in the root director and innput your Nutritionix API ID, key, Sheety endpoint, and Sheety bearer token.


2. Uncomment the configparser code:

# import configparser
#
# config = configparser.ConfigParser()
# config.read('config.ini')

3. Replace:

APP_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]


with:

APP_ID = config.get('API', 'APP_ID')
API_KEY = config.get('API', 'API_KEY')
SHEETY_ENDPOINT = config.get('SHEETY', 'SHEETY_ENDPOINT')
BEARER_TOKEN = config.get('SHEETY', 'BEARER_TOKEN')

4.  Decide if you want to manually type in your attributes or have the user input in the terminal (see comment in code for additional details).