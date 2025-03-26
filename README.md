# Mistral-7B FastAPI Project

This project is a FastAPI-based implementation using the **Mistral-7B-Instruct-v0.1** model from Hugging Face.

## 🚀 Features
- Integrates **Mistral-7B** for text generation.
- Uses **FastAPI** to create an API for interacting with the model.
- Supports MongoDB with **pymongo**.
- Includes a **Dockerfile** for containerized deployment.

---

## 💂️ Project Structure
```
💁 my_project/
│—— 📁 app/
│   ├—— 📝 main.py           # FastAPI app entry point
│   ├—— 📝 config.py         # Configuration settings
│   ├—— 📁 models/           # Database models
│   ├—— 📁 routes/           # API routes
│   └—— 📁 services/         # Business logic
│
│—— 📁 models/
│   └—— 📝 mistral_model.py  # Code to load and run Mistral-7B
│
│—— 📁 static/               # Static files (if applicable)
│—— 📁 templates/            # HTML templates (if applicable)
│—— 📝 requirements.txt      # Python dependencies
│—— 📝 Dockerfile            # Containerization setup
│—— 📝 README.md             # Project documentation
│—— 📝 .gitignore            # Ignore unnecessary files
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download Mistral-7B Model (Offline Use)
```python
from huggingface_hub import snapshot_download
model_path = snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
print(f"Model downloaded to: {model_path}")
```

### 5️⃣ Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```
Server will be available at: **`http://127.0.0.1:8000`**

---

## 🐳 Run with Docker (Optional)
Build and run the project using Docker:
```bash
docker build -t mistral-fastapi .
docker run -p 8000:8000 mistral-fastapi
```

---

## 🔥 API Endpoints

| Method | Endpoint        | Description             |
|--------|---------------|-------------------------|
| GET    | `/`           | Home Route              |
| POST   | `/generate`   | Generate text using Mistral-7B |

Example usage:
```bash
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "Hello, world!"}'
```

---

## 🛠️ Troubleshooting

### **Module Not Found Errors**
Ensure dependencies are installed:
```bash
pip install -r requirements.txt
```

### **MongoDB Connection Issues**
- Ensure MongoDB is running: `mongod --dbpath <your_db_path>`
- Update `config.py` with correct database settings.

### **Hugging Face Model Access Issues**
If you get a **401 Unauthorized** error:
```bash
huggingface-cli login
```
Log in to your Hugging Face account and accept model terms.

---

## 👨‍💻 Contributors
- Aaryan Bansal - [GitHub](https://github.com/aaryan21bansal)

---

## ⭐️ Support & Feedback
If you like this project, please ⭐ the repository!

---

