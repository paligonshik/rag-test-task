"""Streamlit UI for the RAG Invoice Chat Agent."""

import streamlit as st
from dotenv import load_dotenv

from src.agent.chat_agent import ChatAgent

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Invoice Chat Agent",
    page_icon="📊",
    layout="wide",
)

# Custom CSS for better styling
st.markdown(
    """
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .code-block {
        background-color: #1e1e1e;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: 'Monaco', 'Consolas', monospace;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Title and description
st.title("📊 Invoice Data Chat Agent")
st.markdown(
    """
Ask questions about clients, invoices, and line items in natural language.
The agent will generate code to query the data and provide grounded answers.
"""
)


# Initialize the agent (cached to avoid reloading data)
@st.cache_resource
def get_agent() -> ChatAgent:
    """Initialize and cache the chat agent."""
    return ChatAgent(data_dir="data")


# Sidebar with example questions
with st.sidebar:
    st.header("📝 Example Questions")
    st.markdown(
        """
    **Simple Queries:**
    - List all clients with their industries
    - Which clients are based in the UK?
    - Which invoices are marked as "Overdue"?

    **Medium Queries:**
    - List all invoices for Acme Corp
    - Show invoices issued in March 2024

    **Complex Queries:**
    - For each client, compute total billed in 2024
    - Which client has the highest total billed?
    - Top 3 services by revenue
    """
    )

    st.divider()

    st.header("ℹ️ About")
    st.markdown(
        """
    This agent uses:
    - **OpenAI GPT-5.1** for code generation
    - **Pandas** for data querying
    - **Streamlit** for the UI

    All numbers come from actual data - no hallucinations!
    """
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Show code and results for assistant messages
        if message["role"] == "assistant" and "metadata" in message:
            metadata = message["metadata"]

            with st.expander("🔍 View Generated Code"):
                st.code(metadata["code"], language="python")

            with st.expander("📊 View Raw Results"):
                if metadata["success"]:
                    st.text(metadata["result_str"])
                else:
                    st.error(metadata["error"])

# Chat input
if prompt := st.chat_input("Ask a question about the invoice data..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                agent = get_agent()
                response = agent.ask(prompt)

                # Display the answer
                st.markdown(response.answer)

                # Store metadata for history
                metadata = {
                    "code": response.generated_code,
                    "success": response.execution_result.success,
                    "result_str": response.execution_result.to_string(),
                    "error": response.execution_result.error,
                }

                # Show expandable details
                with st.expander("🔍 View Generated Code"):
                    st.code(response.generated_code, language="python")

                with st.expander("📊 View Raw Results"):
                    if response.execution_result.success:
                        st.text(response.execution_result.to_string())
                    else:
                        st.error(response.execution_result.error)

                # Add to history
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response.answer,
                        "metadata": metadata,
                    }
                )

            except Exception as e:
                error_msg = f"Error: {e!s}"
                st.error(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg}
                )

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

