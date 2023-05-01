import os
import pathlib
import re
from your_module import Document, CharacterTextSplitter, OpenAIEmbeddings, FAISS

DOCS_FOLDER = "your_docs_folder"
REPO_DOCUMENTS_PATH = "your_repo_documents_path"
DOCUMENT_BASE_URL = "your_document_base_url"
name_filter = "*.md"  # or any other file type filter
separator = " "
chunk_size_limit = 4096
max_chunk_overlap = 1024

# Load documents and split them into chunks for conversion to embeddings
repo_path = pathlib.Path(os.path.join(DOCS_FOLDER, REPO_DOCUMENTS_PATH))
document_files = list(repo_path.glob(name_filter))

def convert_path_to_doc_url(doc_path):
    # Convert from relative path to actual document url
    return re.sub(f"{DOCS_FOLDER}/{REPO_DOCUMENTS_PATH}/(.*)\.[\w\d]+", f"{DOCUMENT_BASE_URL}/\\1", str(doc_path))

documents = [
    Document(
        page_content=open(file, "r").read(),
        metadata={"source": convert_path_to_doc_url(file)}
    )
    for file in document_files
]

text_splitter = CharacterTextSplitter(separator=separator, chunk_size=chunk_size_limit, chunk_overlap=max_chunk_overlap)
split_docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(split_docs, embeddings)
