import os
import google.generativeai as genai
from landOfWisdomApp.oAuth import OAuth

class Orion:
    def __init__(self):
        # Load credentials
        self.creds = OAuth.load_creds()

        # Configure the generative AI API with the credentials
        genai.configure(credentials=self.creds)

        # Specify generation configuration
        self.generation_config = {
            "temperature": 0.65,
            "top_p": 1,
            "top_k": 0,
            "max_output_tokens": 2048,
            "stop_sequences": [
                "مع تحيات اوريون",
            ],
            "response_mime_type": "text/plain",
        }

        # Create the model
        self.model = genai.GenerativeModel(
            model_name="tunedModels/land-of-wisdom-njjl159nh2fu",
            generation_config=self.generation_config,
        )

    def take_message(self, message):
        """Generate content based on the input message."""
        input_data = f"input: {message}\noutput: "
        response = self.model.generate_content([input_data])
        response = {
            "response": f"{response.text}"
        }
        return response

# # Example usage:
# orion = Orion()
# response = orion.take_message("helo")
# print(response)
