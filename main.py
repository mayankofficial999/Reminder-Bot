import json
import os
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv
from slack_sdk import WebClient
from googleapiclient.discovery import build
from google.oauth2 import service_account
from flask import Flask, request, jsonify
# from slack_sdk.errors import SlackApiError

# Load environment variables from .env file
load_dotenv()

class ReminderBot:
    app = None
    def __init__(self):
        # Set up Flask app
        self.app = Flask(__name__)

        # Set up Slack API client
        slack_token = os.getenv("SLACK_API_TOKEN")
        self.slack_client = WebClient(token=slack_token)

        # Set up Google Calendar API client
        credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/calendar"],
        )
        self.calendar_service = build("calendar", "v3", credentials=credentials)

    def run(self):
        self.app.add_url_rule("/slack/events", view_func=self.slack_event_handler, methods=["POST"])
        self.app.run(host='0.0.0.0', port=5050)
    
    # Define a route to receive Slack events
    def slack_event_handler(self):
        data = request.get_json()
        if "challenge" in data:
            return jsonify({"challenge": data["challenge"]})

        if "event" in data:
            event_data = data["event"]
            print(json.dumps(event_data, indent=4))
            if event_data['type'] == 'reaction_added':
                pass
                #create_calendar_event(event_data)

        return jsonify({"status": "success"})

    # ToDo: Write deadline parsing function from message
    def parseDeadline():
        pass

    # ToDo: Need G-Suite for this functionality
    # Define a function to handle Slack app mentions
    def create_calendar_event(self,event_data):
        # print(self.slack_client.users_info(user=event_data['user']).data)
        # print(self.slack_client.users_info(user=event_data['user']).data['user']['profile']['email'])
        # print(json.dumps(self.slack_client.users_info(user=event_data['user']).data, indent=4))
        # event_text = event_data["text"]
        # event_channel = event_data["channel"]
        # print(event_text)
        # print(event_channel)
        # Get the current date and time
        
        current_time = datetime.now()

        # Set the start date and time
        start_time = current_time.replace(hour=14, minute=30, second=0, microsecond=0)
        start_time = timezone('Asia/Kolkata').localize(start_time).isoformat()

        # Set the end date and time
        end_time = current_time.replace(hour=15, minute=0, second=0, microsecond=0)
        end_time = timezone('Asia/Kolkata').localize(end_time).isoformat()
        # Event details
        event = {
            'summary': 'Meeting',
            'location': 'Conference Room',
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Kolkata',
            },
            'attendees': [
                {'email': 'mayankthegenius999@gmail.com'},
            ],
        }
        
        # # Send the calendar invite
        # calendar_id = 'primary'  # Use 'primary' for the primary calendar of the authenticated user
        # event = self.calendar_service.events().insert(calendarId=calendar_id, body=event).execute()

        # print('Calendar invite sent. Event ID:', event['id'])

# Run the Flask app
if __name__ == "__main__":
    reminderBot = ReminderBot()
    reminderBot.run()
