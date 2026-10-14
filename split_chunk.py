
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_chunks():
    file_path = Path(__file__).resolve().parent / "data" / "sample.txt"

    text = file_path.read_text(encoding="utf-8")

    document = Document(
        page_content=text,
        metadata={"source": str(file_path)}
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents([document])

    return chunks


if __name__ == "__main__":
    chunks = get_chunks()
    print("Total chunks:", len(chunks))
