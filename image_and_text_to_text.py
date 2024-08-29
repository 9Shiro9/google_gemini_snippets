import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image
import pathlib

load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
print(os.environ['GOOGLE_API_KEY'])

#input > text and image => output > text 
current_directory = os.getcwd()
media = pathlib.Path(current_directory)
model = genai.GenerativeModel("gemini-1.5-flash")
ratio = PIL.Image.open(media / "white_dog.jpg")
response = model.generate_content(["Tell me about this image", ratio])
print(response.text)
