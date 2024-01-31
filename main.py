import os
from datetime import datetime

from dotenv import load_dotenv
import requests

load_dotenv("./exercise.env")

GENDER = "MALE"
WEIGHT = 70
HEIGHT = 173
AGE = 23
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
print(API_KEY)
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint= "https://api.sheety.co/8b4b38be50335851a96a1e3d05a1252b/myworks/workouts"
exercise_text = input("Tell me which exercises you did: ")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(response.text)

for exercise in result["exercises"]:
  sheet_input = {
    "workout": {
       "date": today_date,
       "time": now_time,
       "exercise": exercise["name"].title(),
       "duration": exercise["duration_min"],
       "calories": exercise["nf_calories"]
    }
  }

  bearer_header = {
      "Authorization": "Basic c2l2YWppc2o6MTlNRzFBMDQ0OA=="
  }
  sheet_response = requests.post(sheet_endpoint, json=sheet_input)
  print(sheet_response.status_code)
  data = sheet_response.json()
  print(data)




