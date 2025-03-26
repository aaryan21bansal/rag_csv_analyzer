from huggingface_hub import snapshot_download

model_path = snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
print(f"Model downloaded to: {model_path}")
