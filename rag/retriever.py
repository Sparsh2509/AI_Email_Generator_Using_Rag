from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def retrieve_context(query):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    vectorstore = FAISS.load_local("faiss_index", embeddings)
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    return "\n".join([doc.page_content for doc in docs])