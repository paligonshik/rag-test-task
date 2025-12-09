# RAG Invoice Chat Agent

A RAG-style question-answering system that answers natural language questions about invoice data using OpenAI and pandas.

## Quick Start

### 1. Install Dependencies

```bash
uv sync
```

```
pip install -e .
```

### 2. Set OpenAI API Key

```bash
export OPENAI_API_KEY=your-api-key-here
```

Or create a `.env` file in the project root:
```
OPENAI_API_KEY=your-api-key-here
```

### 3. Run the Streamlit UI

```bash
uv run streamlit run app.py
```

### 4. Run Tests (Generate Results Table)

```bash
uv run python test_agent.py
```

This will generate `TEST_RESULTS.md` with answers to all example questions.

## Architecture

```
User Question
     │
     ▼
┌─────────────────────────────────────┐
│  OpenAI GPT-4o-mini                 │
│  (Code Generation)                  │
│  Prompt: Question + Schema → Code   │
└─────────────────────────────────────┘
     │ pandas code
     ▼
┌─────────────────────────────────────┐
│  Code Executor                      │
│  (Sandboxed pandas execution)       │
│  Input: code + DataFrames           │
│  Output: query results              │
└─────────────────────────────────────┘
     │ data results
     ▼
┌─────────────────────────────────────┐
│  OpenAI GPT-4o-mini                 │
│  (Response Formatting)              │
│  Prompt: Question + Data → Answer   │
└─────────────────────────────────────┘
     │
     ▼
Natural Language Answer
```

## Project Structure

```
├── app.py                      # Streamlit UI
├── test_agent.py               # Test script for all questions
├── data/                       # Excel data files
│   ├── Clients.xlsx
│   ├── Invoices.xlsx
│   └── InvoiceLineItems.xlsx
└── src/
    ├── agent/
    │   └── chat_agent.py       # Main orchestrator
    ├── dataloaders/
    │   └── excel_loader.py     # Data loading
    ├── llm/
    │   ├── client.py           # OpenAI wrapper
    │   └── prompt.py           # System prompts with schema
    └── tools/
        └── code_executor.py    # Safe code execution
```

## Key Design Decisions

### 1. Code Generation over Direct Answering

Instead of asking the LLM to answer questions directly, we have it generate pandas code. This ensures:
- All numbers come from actual data execution
- No hallucination of values
- Transparent, auditable query logic

### 2. Schema-Aware Prompting

The system prompt includes complete schema information:
- Table structures with column names and types
- Foreign key relationships
- Pre-computed calculation formulas
- Query guidelines for common operations

### 3. Pre-merged DataFrame

For complex queries, we provide a pre-joined `merged` DataFrame that:
- Joins all three tables (clients, invoices, line_items)
- Pre-computes `line_total = quantity × unit_price × (1 + tax_rate)`
- Simplifies code generation for aggregation queries

### 4. Sandboxed Execution

The code executor:
- Restricts available built-in functions
- Only exposes pandas and numpy
- Catches and reports execution errors gracefully

## Hallucination Mitigation

1. **No direct number generation**: LLM generates code, not answers
2. **Schema grounding**: Complete schema in every prompt
3. **Execution-based values**: All numbers come from pandas operations
4. **Transparency**: UI shows generated code and raw results

## Assumptions & Limitations

### Assumptions

1. All data fits in memory
2. OpenAI API is available (GPT-5.1)

### Limitations

1. **No multi-turn context**: Each question is independent (no conversation memory for queries)
2. **Single-shot code generation**: No retry with error context
3. **No currency normalization**: Calculations don't auto-convert to USD unless explicitly asked
4. **Simple error handling**: Failed queries return error message, no sophisticated fallback

### Potential Improvements

1. Add conversation memory for follow-up questions
2. Implement retry with error feedback to LLM
3. Add query caching for repeated questions
5. Add data validation and schema enforcement

