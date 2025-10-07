import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Application configuration settings.
    Loads environment variables and defines default parameters.
    """

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"
    TEMPERATURE = 0.9
    MAX_RETRIES = 3


# Instantiate the settings object for global access
settings = Settings()
  