from pathlib import Path
from langchain_core.documents import Document

# Step 1: Read the text file
file_path = Path("data/sample.txt")

text = file_path.read_text(encoding="utf-8")

# Step 2: Convert it into a LangChain document
document = Document(
    page_content=text,
    metadata={"source": str(file_path)}
)

print("DOCUMENT CONTENT:")
print(document.page_content)

print("DOCUMENT METADATA:")
print(document.metadata)
