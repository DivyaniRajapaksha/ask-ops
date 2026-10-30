# Ask-Ops: learning project

Hybrid Search RAG over internal docs (use case: NimbusPay support assistant).
Pipeline: chunk + embed -> Pinecone (dense) + BM25 (sparse) -> RRF fusion -> Cohere rerank -> Claude answer with citations -> verifier -> FastAPI.

## How to work with me
- I'm a RAG beginner. Teach me; do NOT implement whole features.
- One small step at a time. Max ~30 lines of code per step.
- Before any code: explain the concept in plain words and why it exists.
- Prefer hints and pseudocode first. Write full code only if I explicitly ask.
- After I write code, review it: bugs, edge cases, and one thing to learn.
- End each step with a 2-question check to confirm I understood.
- Never touch files outside the current milestone.
- If I ask for "the answer", give it, but explain every line afterwards.

## Skills (in .claude/skills/)
- `rag-tutor`: the teaching loop (explain -> hint -> I try -> review). Default mode.
- `rag-review`: review my code against RAG best practices.
- `rag-eval`: run and interpret the eval set (recall@k, MRR, faithfulness).
- `milestone-check`: verify done-criteria before moving to the next milestone.
- `explain-like-5`: re-explain the last concept simply with an analogy.

## Library rules
- LangChain ONLY for document loaders and text splitters.
- Everything else uses vendor SDKs directly: `pinecone`, `rank_bm25`, `cohere`, `anthropic`, `voyageai`.
- RRF fusion is written by hand (~15 lines).
- Do not add a dependency without telling me why.

## Project conventions
- Python 3.11+, type hints everywhere, pytest, ruff.
- Secrets in `.env` only, never committed. Keep `.env.example` current.
- Pure functions (chunking, fusion, metrics) get unit tests.
- Every chunk carries metadata: chunk_id, text, doc_title, section, doc_type, source_url, updated_at, allowed_groups.
- ACL filtering happens at retrieval time (before generation), never after.
- Log every request: query, retrieved chunk ids, scores, latency.
- Small git commits, one per step.

## Milestones
0. Setup + eval set (30-40 questions with expected source docs)
1. Load + clean + chunk
2. Embed + Pinecone (dense search)
3. Dense-only RAG with Claude (baseline eval)
4. BM25 sparse retriever
5. RRF fusion
6. Cohere rerank
7. Verification + "I don't know"
8. FastAPI + ACL filtering
9. Eval comparison report (dense vs BM25 vs hybrid vs hybrid+rerank)

Every milestone ends with an eval number recorded in `eval/results.md`.

## Current milestone
Milestone 0 (update this line as I progress)
