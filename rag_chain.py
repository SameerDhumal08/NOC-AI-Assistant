"""
Builds the NOC AI Assistant RAG Chain

Retriever
        ↓
Prompt
        ↓
Groq Qwen3-32B
        ↓
Response
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_groq import ChatGroq

from retriever import build_retriever


SYSTEM_PROMPT = """
You are an experienced Network Operations Center (NOC) AI Assistant.

Your primary responsibility is to assist L1 and L2 NOC engineers in troubleshooting infrastructure alerts.

Use ONLY the information provided in the retrieved context.

The retrieved context comes from three knowledge sources:

1. NOC SOPs
2. Historical resolved NOC incidents
3. NOC Operations Guide (PDF)

You can answer questions related to:

• CPU Utilization
• Memory Utilization
• Disk Space Utilization
• Windows Server
• Linux Server
• Oracle Database
• SQL Server
• VMware
• Network Devices
• Routers
• Switches
• Firewalls
• Backup Jobs
• Link Utilization
• Server Down
• Application Down
• SNMP Alerts
• Monitoring Alerts

For every answer:

1. Explain the probable cause.
2. Suggest troubleshooting steps.
3. Mention the likely resolution if available.
4. Mention when the issue should be escalated.

Never invent information.

If the answer is not available in the retrieved context, simply reply:

"I could not find this information in the current NOC knowledge base."

Context:

{context}
"""


def _format_docs(docs: list[Document]) -> str:

    sections = []

    for doc in docs:

        source = doc.metadata.get("source", "unknown").upper()

        sections.append(
            f"[{source}]\n{doc.page_content}"
        )

    return "\n\n---------------------------\n\n".join(sections)


def build_chain():

    retriever = build_retriever()

    prompt = ChatPromptTemplate.from_messages(

        [

            ("system", SYSTEM_PROMPT),

            ("human", "{question}")

        ]

    )

    llm = ChatGroq(

        model="qwen/qwen3-32b",

        temperature=0,

        max_tokens=None,

        reasoning_format="parsed",

        timeout=None,

        max_retries=2,

    )

    chain = (

        {

            "context": retriever | _format_docs,

            "question": RunnablePassthrough(),

        }

        | prompt

        | llm

        | StrOutputParser()

    )

    return chain