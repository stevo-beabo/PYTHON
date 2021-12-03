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

class getCalToday:
	# Defining the class variable
	SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar.events.readonly']

	def main(self):
		# Creates and nullifies the variable "creds"
		self.creds = None
		# If the auth token exists, the "creds" variable is loaded with the token and it's scope
		if os.path.exists('token.json'):
			self.creds = Credentials.from_authorized_user_file('token.json', getCalToday.SCOPES)
		# Checks if the auth token does not exist or is not valid 
		if not self.creds or not self.creds.valid:
			# Attempts to refresh the auth token if it exists but has expired
			if self.creds and self.creds.expired and self.creds.refresh_token:
				self.creds.refresh(Request()) ## Problem with the Google Code or the "Credentials" Function at this time. Does not auto refresh the token!
			# Creates a new auth token using the manually made "credentials.json" that was downloaded from the Google Cloud Console	
			else:
				self.flow = InstalledAppFlow.from_client_secrets_file('credentials.json', getCalToday.SCOPES)
				self.creds = self.flow.run_local_server(port = 0)
			with open('token.json', 'w') as self.token:
				self.token.write(self.creds.to_json())

		# Uses the GoogleApplication Build function to define the parameters for the Calendar

		self.service = build('calendar', 'v3', credentials=self.creds)
		# Defining what our current date and setting our variables for the time ranges we want to capture
		self.get_today = datetime.datetime.now().isoformat() + 'Z'
		self.today = self.get_today.split("T")
	
		self.get_morning_start =  [self.today[0], "05:00:00.000000Z"]
		self.morning_range_start = "T".join(self.get_morning_start)
		self.get_morning_end = [self.today[0], "11:29:59.000000Z"]
		self.morning_range_end = "T".join(self.get_morning_end)

		self.get_afternoon_start =  [self.today[0], "12:00:00.000000Z"]
		self.afternoon_range_start = "T".join(self.get_afternoon_start)
		self.get_afternoon_end = [self.today[0], "17:29:59.000000Z"]
		self.afternoon_range_end = "T".join(self.get_afternoon_end)

		self.get_evening_start =  [self.today[0], "18:00:00.000000Z"]
		self.evening_range_start = "T".join(self.get_evening_start)
		self.get_evening_end = [self.today[0], "23:59:59.000000Z"]
		self.evening_range_end = "T".join(self.get_evening_end)

		# Setting the parameters for the date ranges used against the Calendar
		self.events = self.service

	def morning(self):
		self.morning_events = build('calendar', 'v3', credentials=self.creds).events().list(calendarId='primary', timeMin=self.morning_range_start, timeMax=self.morning_range_end, singleEvents=True, orderBy='startTime').execute()
		self.start_times = []
		
		# Prints the output of what was gathered
		print("**********Morning Events**********")
		for self.event in self.morning_events['items']:
			self.get_start_time = self.event['start'].get('dateTime')
			self.start_times.append(self.get_start_time[11:16])

		print(self.start_times)

	def afternoon(self):
		self.afternoon_events = build('calendar', 'v3', credentials=self.creds).events().list(calendarId='primary', timeMin=self.afternoon_range_start, timeMax=self.afternoon_range_end, singleEvents=True, orderBy='startTime').execute()
		self.start_times = []
		
		# Prints the output of what was gathered
		print("**********Afternoon Events**********")
		for self.event in self.afternoon_events['items']:
			self.get_start_time = self.event['start'].get('dateTime')
			self.start_times.append(self.get_start_time[11:16])
			print(self.get_start_time)

		self.start_times_formatted = "\n\n".join(self.start_times)

		print(self.start_times)
		print(self.start_times_formatted)

	def evening(self):
		self.evening_events = build('calendar', 'v3', credentials=self.creds).events().list(calendarId='primary', timeMin=self.evening_range_start, timeMax=self.evening_range_end, singleEvents=True, orderBy='startTime').execute()

		print("**********Evening Events**********")
		for self.event in self.evening_events['items']:
			self.start_time = self.event['start'].get('dateTime')
			print(self.start_time[11:16], self.event['summary'])

runner = getCalToday()

if __name__ == '__main__':
	runner.main()
#	runner.morning()
	runner.afternoon()
#	runner.evening()

