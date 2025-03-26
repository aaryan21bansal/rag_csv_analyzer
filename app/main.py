from fastapi import FastAPI
from app.routes import upload, query, manage

app = FastAPI(title="RAG CSV Analyzer")

app.include_router(upload.router)
app.include_router(query.router)
app.include_router(manage.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
