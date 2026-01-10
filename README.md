# How to Guide: System Prompt Toolkit

## Description

A variety of methods to send system prompts to frontier models to frame interactions.

Default System Prompt: Smaug the Dragon 🐉

# Methods

1) Standard API call with a system prompt (single-turn, no context retention)

standard_single_turn.py

2) Structured API call with a system prompt (single-turn, no context retention)

structured_single_turn.py

3) Structured API call with a system prompt containing the full conversation transcript

structured_full_context.py

4) Structured API call with a system prompt using a rolling context window

structured_rolling_context.py

5) API call augmented with Retrieval-Augmented Generation (RAG) context

rag_augmented_call.py