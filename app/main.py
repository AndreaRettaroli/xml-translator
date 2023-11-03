import os
import openai
from translator import translate_xml
from dotenv import load_dotenv

def main():
    load_dotenv()
    # Read the API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OpenAI API key is not set in the OPENAI_API_KEY environment variable.")
    
    openai.api_key = api_key

    # Define the input XML file and the list of languages
    input_folder = "input"
    input_file = os.path.join(input_folder, "input.example.xml")
    languages = ["es"]  # Add more languages as needed ["es", "fr", "de"]
    translate_xml(input_file, languages)

if __name__ == "__main__":
    main()