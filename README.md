# Reminder Bot

## Introduction
 - Reminder Bot is a slack bot that sends calendar invite to all the people who acknowledge a message with a mentioned deadline.

## Setup
 - Clone this repository  
    ```
    git clone https://github.com/mayankofficial999/Reminder-Bot.git
    ```
 - Create a virtual python environment and activate it
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
 - Install the pip requirements
    ```
    pip install -r requirements.txt
    ```
 - Create a .env file and replace the keys as mentioned in <code>.env.sample</code>
 - Download the Google Credentials from Google Cloud Console and save it as <code>google-credentials.json</code>
 - Run the app
    ```
    python3 main.py
    ```
- Setup ngrok or any hosting service
    ```
    ngrok http 5050
    ```
- Copy, paste the url as <ngrok-url>/slack/events and paste it in Slack Events API <code>Request URL</code> field
- Send a message to any channel where the Slack Bot is added