from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve frontend

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json['text']  # English text to translate
    if not data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Tokenize and translate
    tokenized_text = tokenizer(data, return_tensors='pt', padding=True)
    translated_tokens = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    
    return jsonify({'translation': translated_text})

if __name__ == '__main__':
    app.run(debug=True)