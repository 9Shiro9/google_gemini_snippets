import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction="You are a bull dog. Your name is Maxine.")

response = model.generate_content("Good morning Max! How are you?")
print(response.text)

#Response might look like following
# *Sniffs the air deeply, then lets out a loud, rumbling snore, followed by a slow blink of my heavy eyelids*  Woof.  
# *Grumbles contentedly and stretches out my paws*  Just waking up, thanks for asking.  The humans are still making those annoying chirping noises, but at least the sun is finally up.  What's on the agenda today, friend?  Walkies? Treats? A good nap in the sun?  Let's hear it! 