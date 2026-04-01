import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()


def build_vectorstore():

   
    loader = DirectoryLoader(
        "Email_Templates_idea",
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    docs = loader.load()
    print(f"Loaded {len(docs)} documents")

    
    for doc in docs:
        filename = os.path.basename(doc.metadata["source"])
        doc.metadata["filename"] = filename

    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)

    
    # Use the free API endpoint instead of local models to save massive RAM
    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=os.getenv("HF_TOKEN")
    )

    
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    vectorstore.save_local("faiss_index")

    print("Vectorstore built successfully using HuggingFace embeddings!")

if __name__ == "__main__":
    build_vectorstore()