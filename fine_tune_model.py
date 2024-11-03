import pandas as pd
import cohere
import time

# Initialize Cohere client
cohere_api_key = 'iHuAKEAXeX9kbpntvNA3x0BICUiBHtINYU5rho93'
co = cohere.Client(cohere_api_key)

# Load the dataset with specified encoding
dataset_path = r"C:\Users\Nikhil Sukthe\Downloads\text\sentiment_train.csv"
df = pd.read_csv(dataset_path, encoding='ISO-8859-1')  # or 'latin1'

# Prepare prompts for generation
# Fill NaN values with empty strings and convert to string type
df['text'] = df['text'].fillna('').astype(str)
prompts = df['text'].tolist()  # Use the 'text' column for prompts

# Generate responses
responses = []
for prompt in prompts:
    prompt = prompt.strip()  # Clean up the prompt
    if prompt:  # Check if the prompt is not empty
        response = co.generate(
            model='command-r-plus-08-2024',
            prompt=prompt,
            max_tokens=50,  # Adjust max tokens as needed
            temperature=0.7,  # Control randomness
            stop_sequences=["\n"],  # Stop when a new line is encountered
        )
        responses.append(response.generations[0].text)  # Collect the generated text
        
        time.sleep(1.5)  # Sleep for 1.5 seconds to avoid hitting the limit
    else:
        responses.append("")  # Append empty string if the prompt is empty

# Print generated responses
for i, prompt in enumerate(prompts):
    print(f"Prompt: {prompt}\nGenerated: {responses[i]}\n")
