import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
print(os.environ['GOOGLE_API_KEY'])
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for file in genai.list_files():
    print(f"{file.display_name}, URI: {file.uri} , Name : {file.name}")