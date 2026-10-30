"""Evaluation runner (Milestone 0 sets up the questions; Milestone 3 onward runs it).

Plan (you write this, with rag-eval skill as coach):
- load eval/questions.jsonl
- for each question, run the chosen retrieval variant
- compute recall@k and MRR against expected_sources
- append a row to eval/results.md
"""
