import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Slack webhook configuration
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

# Other configuration variables can be added here 