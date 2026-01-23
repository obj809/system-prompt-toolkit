# System Prompt Toolkit

## Description

A small collection of examples showing different ways to send system prompts and manage conversation context when interacting with large language models.

The goal of this project is to make context handling explicit, simple, and easy to reason about.

## Methods

This project demonstrates different API interaction patterns with increasing levels of context handling.

### Single-Turn  
**File:** `1._single_turn.py`

- Sends a single API call with a system prompt and one user message
- No conversation history is stored or reused
- Each prompt is completely independent

---

### Full Context  
**File:** `2._full_context.py`

- Stores the entire conversation locally
- Sends the full conversation history with every request
- Simulates long-term memory by resending all prior messages

---

### Rolling Context  
**File:** `3._rolling_context.py`

- Maintains a limited, rolling window of recent messages
- Keeps only the most recent user and assistant exchanges
- Discards older messages to limit context size and token usage

---

## Notes on Context

The language model API is stateless.  
Each request is processed independently and contains no memory of previous calls unless prior messages are included in the request.

All conversational “memory” in this project is created by controlling which messages are sent with each API call.

---

## Intended Audience

This project is intended for:

- Beginners learning how LLM APIs work
- Developers experimenting with system prompts
- Anyone curious about context windows and memory behavior