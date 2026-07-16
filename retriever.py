

# CHROMA_DIR  = "chroma_store"
# EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# def build_retriever(
#     k_faq: int = 3,
#     k_tickets: int = 3,
#     k_guides: int = 3,
# ) -> RunnableLambda:
#     embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

#     faq_store = Chroma(
#         collection_name="faq",
#         embedding_function=embeddings,
#         persist_directory=CHROMA_DIR,
#     )
#     tickets_store = Chroma(
#         collection_name="tickets",
#         embedding_function=embeddings,
#         persist_directory=CHROMA_DIR,
#     )
#     guides_store = Chroma(
#         collection_name="guides",
#         embedding_function=embeddings,
#         persist_directory=CHROMA_DIR,
#     )

#     faq_retriever     = faq_store.as_retriever(search_kwargs={"k": k_faq})
#     tickets_retriever = tickets_store.as_retriever(search_kwargs={"k": k_tickets})
#     guides_retriever  = guides_store.as_retriever(search_kwargs={"k": k_guides})

#     def retrieve(query: str) -> list[Document]:
#         return (
#             faq_retriever.invoke(query)
#             + tickets_retriever.invoke(query)
#             + guides_retriever.invoke(query)
#         )

#     return RunnableLambda(retrieve)

"""
Builds a merged retriever across all NOC Chroma collections:

- noc          : NOC FAQ / SOP
- noc_tickets  : Resolved NOC incidents
- noc_guides   : NOC PDF guide
"""

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
