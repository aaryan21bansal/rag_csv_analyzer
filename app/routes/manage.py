from fastapi import APIRouter, HTTPException
from app.database import files_collection

router = APIRouter()

@router.get("/files")
async def list_files():
    files = list(files_collection.find({}, {"_id": 1, "file_name": 1}))
    return {"files": [{"file_id": str(f["_id"]), "file_name": f["file_name"]} for f in files]}

@router.delete("/file/{file_id}")
async def delete_file(file_id: str):
    result = files_collection.delete_one({"_id": file_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}
