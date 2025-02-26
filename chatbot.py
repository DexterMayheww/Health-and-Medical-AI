from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CHROMA_PATH = r"chroma_db"

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5, google_api_key=GOOGLE_API_KEY)

vector_store = Chroma(
    collection_name="example_connection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)
retriever = vector_store.as_retriever(search_kwargs={'k': 5})

def get_chatbot_response(message, history=None):
    retriever.invoke(message)

    rag_prompt = f"""
    You are a professional therapist who answers questions empathetically and without judgment based on the individual's problems.

    The question: {message}

    Conversation history: {history}
    """

    response = llm.invoke(rag_prompt)
    return response.content if response.content else "I'm here to help!"
