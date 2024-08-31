import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)
#Response here might look like following
#That's lovely! Two dogs are twice the fun, and twice the love. What breeds are they? 
# Are they best friends, or do they sometimes get into mischief? 🐶 😄

response = chat.send_message("How many paws are in my house?")
print(response.text)
#Response here might look like following
#You have two dogs, and each dog has four paws, so there are a total of **8 paws** in your house! 🐾 