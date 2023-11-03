import xml.etree.ElementTree as ET
import openai
import os
from copy import deepcopy

def translate_text(text, target_language):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f'Translate the following English text to "{target_language}": "{text}"'}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error while translating text: {e}")
        return ""

# Function to translate an XML file to multiple languages
def translate_xml(input_file, languages):
    # Create the "output" directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Iterate through the XML and translate text in each tag for each language
    for language in languages:
        translated_tree = deepcopy(root)  # Create a deep copy of the root element
        for element in translated_tree.iter():
            if element.text and len(element.text.strip()) != 0:
                element.text = translate_text(element.text, language)

        # Save the translated XML to a file in the "output" folder
        output_file = os.path.join(output_dir, f"output_{language}.xml")
        try:
            ET.ElementTree(translated_tree).write(output_file, xml_declaration=True, encoding="utf-8")
            print(f"Translated to {language} and saved to {output_file}")
        except Exception as e:
            print(f"Error while saving translated XML: {e}")

