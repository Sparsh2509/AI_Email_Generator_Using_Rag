from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load vectorstore
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "Write a professional remote internship request email for a startup."

docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\nResult {i+1}")
    print("Source:", doc.metadata["source"])
    print(doc.page_content)