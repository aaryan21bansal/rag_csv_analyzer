import pandas as pd
from fastapi import APIRouter, UploadFile, File
from app.database import files_collection
from app.vector_store import vector_store

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file_id = str(files_collection.insert_one({"file_name": file.filename, "data": df.to_dict()}).inserted_id)

    # Add to vector store
    vector_store.add_document(file_id, df.astype(str).values.flatten().tolist())

    return {"file_id": file_id, "message": "Upload successful"}
