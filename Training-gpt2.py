import pandas as pd
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling, Dataset

# Load the tokenizer and fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained('./gpt2-fine-tuned')  # Replace with your fine-tuned path if different
model = GPT2LMHeadModel.from_pretrained('./gpt2-fine-tuned')

# Function to load and prepare data from CSV files
def load_data_from_csv(file_path, tokenizer, max_length=128):
    data = pd.read_csv(file_path)
    
    if 'text' not in data.columns:
        raise ValueError(f"CSV file {file_path} must have a 'text' column")
    
    # Tokenize and encode the text
    inputs = [tokenizer.encode(text, truncation=True, max_length=max_length, return_tensors='pt') for text in data['text']]
    input_ids = torch.cat(inputs, dim=0)
    
    # Create a Dataset from input_ids
    return Dataset.from_tensor_slices({'input_ids': input_ids})

# Load your datasets (training and validation)
train_prompt_dataset = load_data_from_csv(r"C:\Users\Nikhil Sukthe\Downloads\Text-AI\train_prompts.csv", tokenizer)
train_essay_dataset = load_data_from_csv(r"C:\Users\Nikhil Sukthe\Downloads\Text-AI\train_essay.csv", tokenizer)
sentiment_dataset = load_data_from_csv(r"C:\Users\Nikhil Sukthe\Downloads\Text-AI\sentiment.csv", tokenizer)

# Combine prompt and essay datasets for training
train_dataset = train_prompt_dataset.concatenate(train_essay_dataset)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # Causal language modeling (auto-regressive)
)

# Define training arguments for further training
training_args = TrainingArguments(
    output_dir='./gpt2-trained',
    overwrite_output_dir=True,
    num_train_epochs=5,  # Adjust as needed for your project
    per_device_train_batch_size=4,  # Modify based on GPU capacity
    evaluation_strategy='epoch',
    save_strategy='epoch',
    logging_dir='./logs',
    logging_steps=50,
    learning_rate=3e-5,  # Customize based on your requirements
    weight_decay=0.01,
    warmup_steps=500,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_essay_dataset,
    data_collator=data_collator
)

# Move the model to GPU if available
if torch.cuda.is_available():
    model.to('cuda')

# Train the model
trainer.train()

# Save the model after training
model.save_pretrained('./gpt2-trained')
tokenizer.save_pretrained('./gpt2-trained')

print("Training process complete. Model saved to './gpt2-trained'.")
