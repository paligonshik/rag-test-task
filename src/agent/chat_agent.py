"""Chat agent that orchestrates the RAG pipeline."""

from dataclasses import dataclass
from pathlib import Path

from src.dataloaders.excel_loader import DataContext, load_data
from src.llm.client import OpenAIClient
from src.tools.code_executor import CodeExecutor, ExecutionResult
from src.config.settings import get_settings
settings = get_settings()
@dataclass
class ChatResponse:
    """Response from the chat agent."""

    answer: str
    generated_code: str
    execution_result: ExecutionResult
    question: str


class ChatAgent:
    """Main chat agent that ties together LLM, data, and execution."""

    def __init__(
        self,
        data_dir: str | Path = "data",
        openai_api_key: str | None = None,
        model: str = settings.model,
    ) -> None:
        # Load data
        self.data_context = load_data(settings.data_dir)

        # Initialize LLM client
        self.llm_client = OpenAIClient(api_key=openai_api_key, model=model)

        # Initialize code executor with loaded dataframes
        self.executor = CodeExecutor(self.data_context.get_dataframes_dict())

    def ask(self, question: str) -> ChatResponse:
        """Answer a question about the invoice data.

        Args:
            question: Natural language question.

        Returns:
            ChatResponse with answer and metadata.
        """
        # Step 1: Generate pandas code
        code_response = self.llm_client.generate_query_code(question)
        generated_code = code_response.content

        # Step 2: Execute the code
        execution_result = self.executor.execute(generated_code)

        # Step 3: Format the response
        if execution_result.success:
            result_str = execution_result.to_string()
            format_response = self.llm_client.format_response(question, result_str)
            answer = format_response.content
        else:
            # If execution failed, try to provide a helpful error message
            answer = (
                f"I encountered an error while processing your question: "
                f"{execution_result.error}\n\n"
                f"Please try rephrasing your question."
            )

        return ChatResponse(
            answer=answer,
            generated_code=generated_code,
            execution_result=execution_result,
            question=question,
        )

    def ask_with_retry(self, question: str, max_retries: int = 2) -> ChatResponse:
        """Ask a question with retry on failure.

        Args:
            question: Natural language question.
            max_retries: Maximum number of retries on execution failure.

        Returns:
            ChatResponse with answer and metadata.
        """
        last_response = None

        for attempt in range(max_retries + 1):
            response = self.ask(question)

            if response.execution_result.success:
                return response

            last_response = response

            # If this isn't the last attempt, we could potentially add
            # error context to help the LLM generate better code
            # For now, we just retry with the same question

        # Return the last response (which has an error)
        return last_response if last_response else response

