import requests
from datetime import datetime
import os

# import configparser
#
# config = configparser.ConfigParser()
# config.read('config.ini')


APP_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

#  Option 1 ************* input user attributes manually ***************

USER_GENDER = "male" 	# Gender as a string
USER_WEIGHT = 80.7  	# Weight as a float in kg
USER_HEIGHT = 180.34 	# Height as a float in cm
USER_AGE = 35 			# Age as an integer

#  Option 2 ************* run program with user input ***************
# do not forget to comment out code that you do not wish to use

# USER_GENDER = input("Enter your gender: ")
# USER_WEIGHT = float(input("Enter your weight (in kg): "))
# USER_HEIGHT = float(input("Enter your height (in cm): "))
# USER_AGE = int(input("Enter your age: "))



headers = {
	"x-app-id": APP_ID,
	"x-app-key": API_KEY,
	"x-remote-user-id": "0"
}

exercise_text = input("Tell me which exercises you did. Now. ")

user_params = {
	"query": exercise_text,
	"gender": USER_GENDER,
	"weight_kg": USER_WEIGHT,
	"height_cm": USER_HEIGHT,
	"age": USER_AGE
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
	sheet_inputs = {
		"sheet1": {
			"date": today_date,
			"time": now_time,
			"exercise": exercise["name"].title(),
			"duration": exercise["duration_min"],
			"calories": exercise["nf_calories"],
		}
	}


sheety_headers = {
	"Content-Type": "application/json",
	"Authorization": f"Bearer {BEARER_TOKEN}"
}

post_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
print(post_response.text)
