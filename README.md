# How to Guide: System Prompt Toolkit

## Description

A variety of methods to send system prompts to frontier models to frame interactions.

Default System Prompt: Smaug the Dragon 🐉

# Methods

1) API call with a system prompt (single-turn, no context retention)

single_turn.py

2) API call with a system prompt containing the full conversation transcript

full_context.py

3) API call with a system prompt using a rolling context window

rolling_context.py

4) API call augmented with Retrieval-Augmented Generation (RAG) context

rag_augmented_call.py