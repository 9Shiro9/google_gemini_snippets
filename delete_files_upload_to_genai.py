import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
print(os.environ['GOOGLE_API_KEY'])
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Delete file
delete_response = genai.delete_file("files/vjramgtxctl2")
print(delete_response)