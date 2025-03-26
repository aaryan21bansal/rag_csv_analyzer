import openai
from app.config import LLM_PROVIDER, OPENAI_API_KEY
from transformers import pipeline

if LLM_PROVIDER == "huggingface":
    llm = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
elif LLM_PROVIDER == "openai":
    openai.api_key = OPENAI_API_KEY

def generate_response(context, query):
    if LLM_PROVIDER == "huggingface":
        response = llm(f"Context: {context}\nQuery: {query}", max_length=100)
        return response[0]["generated_text"]
    elif LLM_PROVIDER == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a CSV assistant."},
                      {"role": "user", "content": f"Context: {context}\nQuery: {query}"}]
        )
        return response["choices"][0]["message"]["content"]
