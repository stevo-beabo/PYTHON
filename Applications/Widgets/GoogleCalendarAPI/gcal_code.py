# Code built by following tutorial (https://www.youtube.com/watch?v=eRHvfNKcwMQ)
# Google Documents for this quickstart found here (https://developers.google.com/calendar/api/quickstart/python)

import os
import requests
import datetime
import json

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
#from requests.structures import CaseInsensitiveDict

# Defining variables
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar.events.readonly']
#all_events = []

def main():
	# Creates and nullifies the variable "creds"
	creds = None
	# If the auth token exists, the "creds" variable is loaded with the token and it's scope
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	# Checks if the auth token does not exist or is not valid 
	if not creds or not creds.valid:
		# Attempts to refresh the auth token if it exists but has expired
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		# Creates a new auth token using the manually made "credentials.json" that was downloaded from the Google Cloud Console	
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port = 0)
		with open('token.json', 'w') as token:
			token.write(creds.to_json())

	# Uses the GoogleApplication Build function to define the parameters for the Calendar

	service = build('calendar', 'v3', credentials=creds)
	# Defining what our current date and setting our variables for the time ranges we want to capture
	get_today = datetime.datetime.now().isoformat() + 'Z'
	today = get_today.split("T")
	
	get_am_start =  [today[0], "05:00:00.000000Z"]
	am_range_start = "T".join(get_am_start)
	get_am_end = [today[0], "11:59:59.000000Z"]
	am_range_end = "T".join(get_am_end)

	get_pm1_start =  [today[0], "12:00:00.000000Z"]
	pm1_range_start = "T".join(get_pm1_start)
	get_pm1_end = [today[0], "17:59:59.000000Z"]
	pm1_range_end = "T".join(get_pm1_end)

	get_pm2_start =  [today[0], "18:00:00.000000Z"]
	pm2_range_start = "T".join(get_pm2_start)
	get_pm2_end = [today[0], "23:59:59.000000Z"]
	pm2_range_end = "T".join(get_pm2_end)

	# Setting the parameters for the date ranges used against the Calendar
	events = service
	am_events = build('calendar', 'v3', credentials=creds).events().list(calendarId='primary', timeMin=am_range_start, timeMax=am_range_end, singleEvents=True, orderBy='startTime').execute()
	pm1_events = build('calendar', 'v3', credentials=creds).events().list(calendarId='primary', timeMin=pm1_range_start, timeMax=pm1_range_end, singleEvents=True, orderBy='startTime').execute()
	pm2_events = build('calendar', 'v3', credentials=creds).events().list(calendarId='primary', timeMin=pm2_range_start, timeMax=pm2_range_end, singleEvents=True, orderBy='startTime').execute()
	
	# Prints the output of what was gathered
	print("**********Morning Events**********")
	for event in am_events['items']:
		start_time = event['start'].get('dateTime')
		print(start_time[11:16], event['summary'])

	print("**********Afternoon Events**********")
	for event in pm1_events['items']:
		start_time = event['start'].get('dateTime')
		print(start_time[11:16], event['summary'])

	print("**********Evening Events**********")
	for event in pm2_events['items']:
		start_time = event['start'].get('dateTime')
		print(start_time[11:16], event['summary'])

if __name__ == '__main__':
	main()


