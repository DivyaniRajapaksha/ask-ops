---
name: rag-review
description: Review the user's RAG code against industry best practices (chunk metadata, ACL filtering, grounded prompts, secrets, tests, logging). Use when the user says "review my code", finishes a step, or before a milestone is marked done.
---

# RAG Code Review

Review only the code the user wrote for the current milestone. Do not rewrite it; point to the line, explain the problem, and let the user fix it.

## Output format
1. **What works** (1 or 2 lines, be honest).
2. **Must fix** (bugs, security, data leaks).
3. **Should improve** (clarity, robustness, tests).
4. **One thing to learn** (a single concept worth remembering).

## Checklist
**Ingestion and chunking**
- Every chunk has: chunk_id, text, doc_title, section, doc_type, source_url, updated_at, allowed_groups.
- chunk_id is deterministic (same input gives same id), so re-ingestion updates rather than duplicates.
- Headers, footers and page numbers are stripped; tables are not shredded.
- Chunk size and overlap are config values, not magic numbers.
- Short context (doc title and section) is attached to chunks so "it" and "this policy" have a referent.

**Retrieval**
- Embedding model and dimension match the index. Query and documents use the same model (and the correct input_type if the provider has one).
- ACL filter is applied inside the retrieval call (Pinecone metadata filter, or before fusion for BM25), never after generation.
- BM25 tokenizer keeps IDs and error codes intact (for example ERR-4012, PENDING_REVIEW).
- top-k values are config values.
- RRF handles chunks that appear in only one list.

**Generation**
- The prompt says: answer only from the numbered sources, cite every factual sentence, say "I couldn't find this in the docs" when unsupported.
- Retrieved text is treated as data, not instructions (guard against prompt injection from documents).
- Citation ids are validated against the chunks actually provided.
- Model name, temperature and max_tokens are configurable.

**Engineering**
- No secrets in code; keys come from .env; .env.example is up to date.
- Type hints on all functions; pure functions have pytest tests.
- Each request logs: query, retrieved chunk ids with scores, latency.
- Errors from external APIs (rate limits, timeouts) are handled with retry and backoff.
- No silent failures: empty retrieval results produce an explicit "no answer" path.
