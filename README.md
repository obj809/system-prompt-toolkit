# How to Guide: System Prompt Toolkit

## Description

A variety of methods to send system prompts to frontier models to frame interactions.

# Methods

Different API interaction patterns with varying levels of context handling.

1. Single-Turn

Sends a single API call with a system prompt only. No conversation history is preserved between requests.

File: single_turn.py

2. Full Context

Includes the entire conversation transcript in the system prompt for every API call.

File: full_context.py

3. Rolling Context

Maintains a limited, rolling window of recent messages to balance context retention and token usage.

File: rolling_context.py

4. RAG

Augments the prompt with externally retrieved context (e.g. documents, embeddings, or vector search results).

File: rag_augmented_call.py