from pydantic import BaseModel

class FileUploadResponse(BaseModel):
    file_id: str
    message: str

class QueryRequest(BaseModel):
    file_id: str
    query: str

class QueryResponse(BaseModel):
    response: str
