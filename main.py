"""
CLI entry point for the NOC AI Assistant.

Run:
python main.py
"""

import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from dotenv import load_dotenv
from rag_chain import build_chain

load_dotenv()


def main():

    print("=" * 60)
    print("        NOC AI ASSISTANT")
    print("=" * 60)

    print("\nSupported Topics:")
    print("-------------------------------------------")
    print("• CPU Utilization")
    print("• Memory Utilization")
    print("• Disk Space")
    print("• Linux Server")
    print("• Windows Server")
    print("• Oracle Database")
    print("• SQL Server")
    print("• VMware")
    print("• Network Devices")
    print("• Router")
    print("• Switch")
    print("• Firewall")
    print("• Backup Failure")
    print("• Server Down")
    print("• Application Down")
    print("• SNMP Alerts")
    print("• Link Utilization")
    print("• SOP Troubleshooting")
    print("-------------------------------------------")

    print("\nType your issue below.")
    print("Type 'quit' to exit.\n")

    chain = build_chain()

    while True:

        question = input("NOC Engineer > ").strip()

        if not question:
            continue

        if question.lower() in ("quit", "exit", "q"):
            print("\nThank you for using NOC AI Assistant.")
            break

        print("\nAI Assistant:\n")

        for chunk in chain.stream(question):
            print(chunk, end="", flush=True)

        print("\n")


if __name__ == "__main__":
    main()