from fastapi import APIRouter, HTTPException
from app.database import files_collection
from app.vector_store import vector_store
from app.llm_service import generate_response
from app.models import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_csv(request: QueryRequest):
    file_data = files_collection.find_one({"_id": request.file_id})
    if not file_data:
        raise HTTPException(status_code=404, detail="File not found")

    retrieved_data = vector_store.search(request.query)
    if not retrieved_data:
        return {"response": "No relevant information found."}

    response = generate_response("\n".join(retrieved_data), request.query)
    return {"response": response}
