import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import streamlit as st
from dotenv import load_dotenv
from rag_chain import build_chain

load_dotenv()

SAMPLE_QUESTIONS = [
    "CPU utilization is above 90% on Linux server",
    "CPU utilization is above 90% on Windows server",
    "Memory utilization alert received on Windows server",
    "Memory utilization alert received on Linux server",
    "Disk utilization exceeded threshold",
    "Server is not reachable from monitoring",
    "Port Down alert detected on Cisco Switch",
    "Link Flapping detected on network interface",
    "Database listener is down",
    "Application service is not responding",
    "Firewall interface is down",
    "SNMP service is not responding"
]

st.set_page_config(
    page_title="NOC AI Assistant",
    page_icon="🖥️",
    layout="centered",
)

@st.cache_resource
def get_chain():
    return build_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🖥️ NOC AI Assistant")
    st.caption("Powered by RAG · Qwen3-32B on Groq")
    st.caption("👨‍💻 Developed by Sameer Dhumal")
    st.divider()

    st.markdown("### Common NOC Alerts")
    st.caption("Click any alert to ask instantly.")
    for q in SAMPLE_QUESTIONS:
        if st.button(q, use_container_width=True):
            st.session_state.pending_question = q

    st.divider()
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []

# ── Main ─────────────────────────────────────────────────────────────────────
st.title("NOC AI Assistant")
st.caption("""
    Ask questions related to:

    • CPU Utilization
    • Memory Utilization
    • Disk Space
    • Windows Server
    • Linux Server
    • Database
    • Network Devices
    • Firewall
    • Switches
    • Routers
    • SOP Troubleshooting
    """)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Resolve question from chat input or sidebar button click
question = st.chat_input("Describe your issue…")
if st.session_state.pending_question:
    question = st.session_state.pending_question
    st.session_state.pending_question = None

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        chain = get_chain()
        response = st.write_stream(chain.stream(question))

    st.session_state.messages.append({"role": "assistant", "content": response})
