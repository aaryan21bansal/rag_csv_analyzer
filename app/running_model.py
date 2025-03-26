from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Use the correct path to your downloaded model
model_path = r"C:\\Users\\aarya\\.cache\\huggingface\\hub\\models--mistralai--Mistral-7B-Instruct-v0.1\snapshots\\2dcff66eac0c01dc50e4c41eea959968232187fe"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Load model
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Test inference
prompt = "Tell me a joke about AI."
inputs = tokenizer(prompt, return_tensors="pt").to(device)
output = model.generate(**inputs, max_length=100)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)
