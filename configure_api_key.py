import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
print(os.environ['GOOGLE_API_KEY'])
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])