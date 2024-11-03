from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the model
generator = pipeline('text-generation', model='gpt2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    generated = generator(prompt, max_length=150, num_return_sequences=1)
    return jsonify({'generated_text': generated[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
