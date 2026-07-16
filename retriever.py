

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document


CHROMA_DIR = "chroma_store"

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def build_retriever(

    k_noc=3,
    k_tickets=3,
    k_guides=3,

):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL
    )

    noc_store = Chroma(
        collection_name="noc",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    ticket_store = Chroma(
        collection_name="noc_tickets",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    guide_store = Chroma(
        collection_name="noc_guides",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    noc_retriever = noc_store.as_retriever(
        search_kwargs={"k": k_noc}
    )

    ticket_retriever = ticket_store.as_retriever(
        search_kwargs={"k": k_tickets}
    )

    guide_retriever = guide_store.as_retriever(
        search_kwargs={"k": k_guides}
    )

    def retrieve(query: str) -> list[Document]:

        docs = []

        docs.extend(
            noc_retriever.invoke(query)
        )

        docs.extend(
            ticket_retriever.invoke(query)
        )

        docs.extend(
            guide_retriever.invoke(query)
        )

        return docs

    return RunnableLambda(retrieve)
