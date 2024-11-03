from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load and save the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

model.save_pretrained('./gpt2-model')
tokenizer.save_pretrained('./gpt2-model')


from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load and save the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

model.save_pretrained('./gpt2-model')
tokenizer.save_pretrained('./gpt2-model')

tokenizer = GPT2Tokenizer.from_pretrained('./gpt2-model')
model = GPT2LMHeadModel.from_pretrained('./gpt2-model')

# Quick test
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors='pt')
output = model.generate(input_ids, max_length=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
