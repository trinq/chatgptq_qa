from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rag_qa_system.document_retrieval import DocumentRetrieval
from dotenv import load_dotenv
import os

load_dotenv()

faiss_index_file = os.getenv("FAISS_INDEX_FILE")
chatgpt_model_name = os.getenv("CHATGPT_MODEL_NAME")

app = FastAPI()
document_retrieval = DocumentRetrieval(index_file=faiss_index_file)

# Rest of the code for the FastAPI app


class DocumentVector(BaseModel):
    id: int
    vector: List[float]

@app.post("/add_document_vector/")
async def add_document_vector(document_vector: DocumentVector):
    # Implement the function to add a document vector to the FAISS index
    pass

@app.post("/search/")
async def search_document_vectors(query_vector: List[float], top_k: int = 5):
    # Implement the function to search the FAISS index for similar vectors
    pass
