# How to Guide: System Prompt Toolkit

## Description

A variety of methods to send system prompts to frontier models to frame interactions.

# Methods

Different API interaction patterns with varying levels of context handling.

1. Single-Turn

No context retention

single_turn.py

2. Full Context

Entire conversation included

full_context.py

3. Rolling Context

Sliding window of recent messages

rolling_context.py

4. RAG

External context augmentation

rag_augmented_call.py