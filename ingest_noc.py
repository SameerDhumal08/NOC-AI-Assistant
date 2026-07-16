
"""
Ingests data/noc.csv into the 'noc' Chroma collection.

Run:
python ingest_noc.py
"""

import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import pandas as pd

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# ---------------- Configuration ---------------- #

CHROMA_DIR = "chroma_store"

COLLECTION = "noc"

CSV_PATH = os.path.join("data", "noc_sop.csv")

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ---------------- Load NOC CSV ---------------- #

def load_noc_documents(csv_path: str) -> list[Document]:

    df = pd.read_csv(csv_path)

    docs = []

    for _, row in df.iterrows():

        content = f"""
Alert / Question:
{row['question']}

Resolution:
{row['answer']}
"""

        docs.append(
            Document(
                page_content=content,
                metadata={
                    "source": "noc_sop",
                    "category": row["category"],
                    "incident_id": str(row["id"]),
                },
            )
        )

    return docs


# ---------------- Main ---------------- #

def main():

    print("Loading NOC SOP documents...")

    docs = load_noc_documents(CSV_PATH)

    print(f"{len(docs)} NOC entries loaded.")

    print("Loading Embedding Model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL
    )

    print("Creating Chroma Vector Database...")

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION,
        persist_directory=CHROMA_DIR,
    )

    print(
        f"Completed successfully.\n"
        f"Stored {vectorstore._collection.count()} vectors."
    )


if __name__ == "__main__":
    main()