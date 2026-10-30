# Ask-Ops: Hybrid Search RAG over Internal Docs

A support assistant for a fictional payments company (NimbusPay). It answers questions from runbooks, postmortems, error references and policies, with inline citations and permission-aware retrieval.

Built step by step as a learning project.

## Pipeline
```
Docs -> Loader -> Cleaner -> Chunker -> Embeddings -> Pinecone (dense)
                                   \-> BM25 index (sparse)

Query -> Dense top-N + BM25 top-N -> Reciprocal Rank Fusion
      -> Cohere Rerank -> Claude (cited answer) -> Verifier -> FastAPI
```

## Setup
```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # then add your API keys
```

## Working with Claude in VS Code
- `CLAUDE.md` holds the teaching rules (Claude explains and reviews; you write the code).
- Skills live in `.claude/skills/`: `rag-tutor`, `rag-review`, `rag-eval`, `milestone-check`, `explain-like-5`.
- Start a session and say: "Let's begin Milestone 0. Explain it, no code."

## Milestones
| # | Milestone | Status |
|---|---|---|
| 0 | Setup + eval set | todo |
| 1 | Load + clean + chunk | todo |
| 2 | Embed + Pinecone | todo |
| 3 | Dense-only RAG | todo |
| 4 | BM25 | todo |
| 5 | RRF fusion | todo |
| 6 | Cohere rerank | todo |
| 7 | Verification + "I don't know" | todo |
| 8 | FastAPI + ACL filtering | todo |
| 9 | Eval comparison report | todo |

## Results
See `eval/results.md`.
