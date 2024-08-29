import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# print(os.environ['GOOGLE_API_KEY'])
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Upload the file and print a confirmation
sample_file = genai.upload_file(path="gemini.pdf",
                                display_name="Gemini 1.5 PDF")
print(sample_file)

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Prompt the model with text and the previously uploaded pdf.
response = model.generate_content([sample_file, "Can you summarize this document as a bulleted list?"])

print("Response to pdf file only :\n" + response.text)

#multiple files
import PIL.ImageFile

sample_file_2 = PIL.Image.open('white_dog.jpg')

prompt = "Summarize the files."

response2 = model.generate_content([prompt,sample_file, sample_file_2])

print("Response to pdf and jpg :" + response2.text)

