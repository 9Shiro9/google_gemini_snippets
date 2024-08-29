import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
print(os.environ['GOOGLE_API_KEY'])


#input > text only => output > text 
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

#input > text and image => output > text 
