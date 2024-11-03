# fine_tune.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import torch

# Load GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to load dataset
def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
        overwrite_cache=True
    )

# Function to create data collator
def create_data_collator(tokenizer):
    return DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False  # Set to False for causal language modeling
    )

# Load custom training data
train_file_path = './train_data.txt'  # Path to your training data text file
train_dataset = load_dataset(train_file_path, tokenizer)

# Create data collator
data_collator = create_data_collator(tokenizer)

# Set training arguments
training_args = TrainingArguments(
    output_dir='./gpt2-fine-tuned',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2,
    prediction_loss_only=True,
    logging_dir='./logs',
    logging_steps=100
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator
)

# Start training
if torch.cuda.is_available():
    model.to('cuda')

trainer.train()

# Save the fine-tuned model and tokenizer
model.save_pretrained('./gpt2-fine-tuned')
tokenizer.save_pretrained('./gpt2-fine-tuned')

print("Fine-tuning complete. Model saved to './gpt2-fine-tuned'.")
