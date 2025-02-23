# Import necessary libraries
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.qdrant import Qdrant
from phi.embedder.ollama import OllamaEmbedder
from phi.playground import Playground, serve_playground_app

from .constants import PDF_URLS

# Define the collection name for the vector database
collection_name = "medical-research-index"

# Set up Qdrant as the vector database with the embedder
vector_db = Qdrant(
    collection=collection_name,
    url="http://localhost:6333/",
    embedder=OllamaEmbedder()
)

# Define the knowledge base with a medical research PDF URL
knowledge_base = PDFUrlKnowledgeBase(
    urls=PDF_URLS,
    vector_db=vector_db,
)

# Load the knowledge base, comment out after the first run to avoid reloading
knowledge_base.load(recreate=True, upsert=True)

# Create the Agent using Ollama's llama3.2 model and the knowledge base
agent = Agent(
    name="Medical RAG Agent",
    model=Ollama(id="llama3.2"),
    knowledge=knowledge_base,
)

# UI for RAG agent
app = Playground(agents=[agent]).get_app()

# Run the Playground app
if __name__ == "__main__":
    serve_playground_app("medical_rag_agent:app", reload=True)
