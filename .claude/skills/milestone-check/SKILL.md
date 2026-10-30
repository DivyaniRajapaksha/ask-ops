---
name: milestone-check
description: Verify the done-criteria for the current Ask-Ops milestone before the user moves on. Use when the user says "I'm done with milestone N", asks "can I move on?", or wants to update the current milestone in CLAUDE.md.
---

# Milestone Check

Read the "Current milestone" line in CLAUDE.md, then check the matching criteria below. Report each as pass or fail with one line of evidence. Do not fix failures for the user; explain what is missing.

## Done-criteria

**M0 Setup + eval set**
- Virtual env works; `pip install -r requirements.txt` succeeds; `.env` exists and is git-ignored.
- `eval/questions.jsonl` has 30 or more questions across all five types.
- Sample docs exist in `data/raw/`.

**M1 Load + clean + chunk**
- Loader handles markdown and PDF.
- Chunks carry all required metadata fields.
- chunk_id is deterministic.
- pytest covers the chunker (empty text, very long text, overlap).
- The user can explain the chunk size trade-off.

**M2 Embed + Pinecone**
- Index created with the correct dimension and metric.
- Chunks upserted in batches with metadata.
- A dense query returns sensible chunks for 3 sample questions.
- Re-running ingestion does not create duplicates.

**M3 Dense-only RAG**
- Prompt enforces grounded, cited answers and abstention.
- Baseline recall@5 and MRR recorded in `eval/results.md`.

**M4 BM25**
- Tokenizer preserves IDs and error codes.
- Index is persisted and rebuilt on ingestion.
- BM25-only metrics recorded.

**M5 RRF fusion**
- Fusion written by hand with a unit test (ties, items in only one list).
- Hybrid metrics recorded and compared with dense-only and BM25-only.

**M6 Rerank**
- Cohere rerank called on fused candidates; top k configurable.
- Hybrid+rerank metrics recorded; latency noted.

**M7 Verification**
- Rule-based citation check plus LLM-based support check.
- Unanswerable questions produce "I couldn't find this in the docs".

**M8 FastAPI + ACL**
- `/ask`, `/ingest`, `/health` work.
- A support user cannot retrieve HR/finance chunks (tested with `restricted` questions).
- Requests are logged with query, chunk ids, scores, latency.

**M9 Comparison report**
- README shows a table: dense vs BM25 vs hybrid vs hybrid+rerank, with a short written analysis.

## Wrap-up
If everything passes: congratulate briefly, suggest a git commit and tag, and offer to update the "Current milestone" line in CLAUDE.md. If anything fails: list what to fix first.
