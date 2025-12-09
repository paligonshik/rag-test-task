"""Test script for the chat agent."""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to load .env from multiple locations
from dotenv import load_dotenv

load_dotenv()  # Current directory
load_dotenv(Path(__file__).parent.parent / ".env")  # Parent directory
load_dotenv(Path.home() / "rag-test-task" / ".env")  # Original repo location

from src.agent.chat_agent import ChatAgent


def test_questions() -> list[tuple[str, str]]:
    """Test all example questions and return results."""

    questions = [
        # Main questions from README.md example section:
        "List all clients with their industries.",
        "Which clients are based in the UK?",
        "List all invoices issued in March 2024 with their statuses.",
        'Which invoices are currently marked as "Overdue"?',
        "For each service_name in InvoiceLineItems, how many line items are there?",
        "List all invoices for Acme Corp with their invoice IDs, invoice dates, due dates, and statuses.",
        "Show all invoices issued to Bright Legal in February 2024, including their status and currency.",
        "For invoice I1001, list all line items with service name, quantity, unit price, tax rate, and compute the line total (including tax) for each.",
        "For each client, compute the total amount billed in 2024 (including tax) across all their invoices.",
        "Which client has the highest total billed amount in 2024, and what is that total?",
        # Optional/extra questions from README.md:
        "Across all clients, which three services generated the most revenue in 2024? Show the total revenue per service.",
        "Which invoices are overdue as of 2024-12-31? List invoice ID, client name, invoice_date, due_date, and status.",
        "Group revenue by client country: for each country, compute the total billed amount in 2024 (including tax).",
        "For the service “Contract Review”, list all clients who purchased it and the total amount they paid for that service (including tax).",
        "Considering only European clients, what are the top 3 services by total revenue (including tax) in H2 2024 (2024-07-01 to 2024-12-31)?",
    ]

    agent = ChatAgent(data_dir="data")
    results = []

    for i, question in enumerate(questions, 1):
        print(f"\n{'='*80}")
        print(f"Question {i}: {question}")
        print("=" * 80)

        try:
            response = agent.ask(question)
            print(f"\nGenerated Code:\n{response.generated_code}")
            print(f"\nExecution Success: {response.execution_result.success}")
            if not response.execution_result.success:
                print(f"Error: {response.execution_result.error}")
            print(f"\nAnswer:\n{response.answer}")
            results.append((question, response.answer))
        except Exception as e:
            error_str = str(e)
            print(f"Error: {error_str}")
            # Check for rate limit / quota errors
            if "429" in error_str or "quota" in error_str.lower():
                print("\n⚠️  OpenAI API quota exceeded. Please check your billing.")
                results.append((question, "API quota exceeded - please add credits to your OpenAI account"))
            else:
                results.append((question, f"Error: {error_str}"))

    return results


def generate_results_text(results: list[tuple[str, str]]) -> str:
    """Generate a readable text listing Q/A pairs in order."""
    lines = ["# Test Results", ""]
    for i, (question, answer) in enumerate(results, 1):
        lines.append(f"Q{i}: {question}\n")
        lines.append(f"{answer}\n")
    return "\n".join(lines)


if __name__ == "__main__":
    print("Testing Invoice Chat Agent...")
    results = test_questions()

    # Generate and save a more readable results text (not a table)
    output_text = generate_results_text(results)
    with open("TEST_RESULTS.md", "w") as f:
        f.write(output_text)

    print("\n\nResults saved to TEST_RESULTS.md")

