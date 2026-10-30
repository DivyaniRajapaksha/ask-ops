---
name: explain-like-5
description: Re-explain the last RAG concept in very simple words with a everyday analogy and a tiny example. Use when the user says "explain like I'm 5", "I don't get it", "simpler", or seems confused.
---

# Explain Like I'm 5

Re-explain the most recent concept (or the one the user names) in a simpler way.

## Format
1. **One-sentence version** (no jargon).
2. **Analogy** from everyday life (library, pizza slices, a judge picking finalists, Ctrl+F). Keep one analogy; do not mix several.
3. **Tiny example** using NimbusPay data (for instance one question and two chunks), with made-up numbers small enough to follow by hand.
4. **Where it sits in the pipeline**: a one-line arrow diagram highlighting the step.
5. **Bridge to the real term**: map each part of the analogy to the technical word (for example "slice = chunk", "judge = reranker").
6. **One question** to check the user got it.

## Rules
- No code unless the user asks.
- Short sentences. Define every technical word the first time.
- If the user is still confused after this, try a different analogy or a smaller example instead of repeating.
