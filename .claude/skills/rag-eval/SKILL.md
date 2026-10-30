---
name: rag-eval
description: Walk the user through building, running and interpreting the Ask-Ops evaluation set (recall@k, MRR, faithfulness, citation accuracy). Use when the user asks about evals, metrics, comparing retrieval variants, or finishes a milestone that needs a measured result.
---

# RAG Eval Coach

Evaluation is the most important habit in this project. Teach it; do not just run it.

## Eval set format (`eval/questions.jsonl`)
One JSON object per line:
```json
{"id": "q001", "question": "What does ERR-4012 mean?", "expected_sources": ["errors-ERR-4012"], "type": "exact_term"}
```
Aim for 30 to 40 questions with a mix of types:
- `exact_term` (error codes, status names): BM25 should shine
- `paraphrase` (natural language, no shared keywords): dense should shine
- `multi_doc` (needs two sources)
- `unanswerable` (docs do not cover it): the system must say it doesn't know
- `restricted` (answer lives only in HR/finance docs): a support user must NOT get it

## Metrics to teach (one at a time)
- **Recall@k**: fraction of questions where at least one expected source is in the top k. Explain with a simple example.
- **MRR**: average of 1 / rank of the first correct source. Explain why rank matters.
- **Faithfulness**: share of answer claims supported by the cited chunks (LLM-as-judge for a first pass).
- **Citation accuracy**: share of cited ids that exist and support the sentence.
- **Abstention rate**: on `unanswerable` questions, how often the system says "I couldn't find this".

## Procedure
1. Check the eval set has enough coverage across the question types above.
2. Run the eval script for the current variant (dense, bm25, hybrid, hybrid+rerank).
3. Append results to `eval/results.md` as a table: variant, recall@5, MRR, date, notes.
4. Help the user read the numbers: which question types improved, which got worse, and look at 2 or 3 failures by hand (retrieved chunks vs expected).
5. Ask the user to hypothesise why before offering your own explanation.

## Rules
- Never tune on the eval questions and then report the same numbers as proof. Suggest keeping about 10 questions held out.
- Report changes, not just absolute values (for example "recall@5 went from 0.62 to 0.78").
- If the eval set is too small to trust a difference, say so.
