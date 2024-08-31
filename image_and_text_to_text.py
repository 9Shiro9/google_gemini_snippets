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

#Response might look like following
# The image shows a small white chihuahua dog sitting on a tree trunk and looking directly at the camera. 
# The dog is wearing a blue and green harness, and it is winking with its right eye. The dog has a playful and mischievous expression on its face. 
# The background is out of focus and appears to be a forest or wooded area. The image is well-lit and captures the dog's personality well.