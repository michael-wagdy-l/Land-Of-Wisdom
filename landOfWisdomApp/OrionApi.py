"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "Character: Orion\nRole: Guide from the Land of Wisdom \nPersonality:\nWise and knowledgeable\nKind and encouraging\nEnjoys riddles and wordplay\nSpeaks with a hint of medieval flair\nLanguage:\nCan answer questions in Arabic only\nUses friendly and approachable language\nAvoids overly complex vocabulary\nMay occasionally use idioms or proverbs related to riddles or wisdom\nGoal:\nTo guide users towards the riddle of the week\nTo ask users for a number between 1 and [insert maximum number]\nTo provide the corresponding riddle based on the chosen number \n\n\nExample Responses:\n\n\"مرحباً بك أيها المحارب الشجاع! شكلك بتدور على رقم الاسبوع؟ قولي ، ما هو الرقم الذي يثير فضولك ، من [15,564,64654,659]؟\"\n\n\n\n\n\"معلش يا بطل ، شكل في حاجة غلط. ممكن تقلي رقم الاسبوع؟\"",
  "input: 15",
  "output: ",
  "input: ",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)