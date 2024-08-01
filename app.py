from flask import Flask, request, jsonify
from PIL import Image
import openai
import io

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        image = Image.open(file)
        text = extract_text_from_image(image)
        mermaid_code = translate_text_to_mermaid(text)
        return jsonify({"mermaid_code": mermaid_code})

def extract_text_from_image(image):
    # Placeholder for text extraction logic (e.g., OCR)
    return "Extracted text from image"

def translate_text_to_mermaid(text):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Translate the following text to Mermaid code:\n{text}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
