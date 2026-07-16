"""
Ingests resolved NOC tickets from data/noc_tickets.db
into the 'noc_tickets' Chroma collection.

Run:
python ingest_noc_tickets.py
"""

import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import sqlite3

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# ---------------- Configuration ---------------- #

CHROMA_DIR = "chroma_store"

COLLECTION = "noc_tickets"

DB_PATH = os.path.join("data", "noc_tickets.db")

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ---------------- Load NOC Tickets ---------------- #

def load_ticket_documents(db_path: str) -> list[Document]:

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM tickets
        WHERE status='Resolved'
    """).fetchall()

    conn.close()

    docs = []

    for row in rows:

        content = f"""
Ticket ID:
{row['ticket_id']}

Category:
{row['category']}

Issue Type:
{row['issue_type']}

Issue Description:
{row['description']}

Resolution:
{row['resolution']}

Status:
{row['status']}
"""

        docs.append(
            Document(
                page_content=content,
                metadata={
                    "source": "noc_ticket",
                    "ticket_id": row["ticket_id"],
                    "category": row["category"],
                    "status": row["status"],
                },
            )
        )

    return docs


# ---------------- Main ---------------- #

def main():

    print("Loading resolved NOC tickets...")

    docs = load_ticket_documents(DB_PATH)

    print(f"{len(docs)} resolved tickets loaded.")

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL
    )

    print("Creating Chroma collection...")

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION,
        persist_directory=CHROMA_DIR,
    )

    print(
        f"Completed successfully.\n"
        f"Stored {vectorstore._collection.count()} ticket vectors."
    )


if __name__ == "__main__":
    main()