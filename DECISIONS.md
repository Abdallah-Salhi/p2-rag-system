# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose the corpus of congressional research/report documents specifically related to energy and climate mainly due to the easily accessible documents and the fact that it would be the easiest sourcing. While I do care about energy and climate and what the US congress reports or what the documents contain, the primary motivation is to ensure the RAG system is working as expected and to determine which retrieval method works best. 

I predict that Hybrid will work the best based on the fact that it is usually at least as good as the weaker of the two methods (bm25 and dense). While it can inherit the mistakes both make I think it will generally do well. 

The method that will likely preform the worst in my opinion is the dense method. This is because exact names and numbers may cause confusion with similar reports like the same title in different years. 

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

We faced a fork on document chunk size: whether to stick with the baseline 300-word chunks or test 150-word and 600-word variants. We ultimately picked 300 words as our baseline. Comparing the variants against our 300-word baseline (which achieved MRR@10 of 0.983, Recall@10 of 0.953, and nDCG@10 of 0.926), the 150-word chunks performed worse across the board (MRR@10 0.967, Recall@10 0.889, nDCG@10 0.861), while the 600-word chunks yielded a higher MRR@10 of 1.000 but a lower Recall@10 of 0.911 and a lower nDCG@10 of 0.886. What we gave up by sticking with the 300-word baseline was the absolute top-rank MRR score achieved by the larger chunks; however, since none of the MRR@10 differences were statistically distinguishable, choosing 300 words avoided the nDCG degradation and recall loss seen in the variants.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

I initially asked to move and rename the parent directory to fix a uv run path error caused by a colon in Coding:Programming. I chose not to proceed after seeing the trade-offs: moving the top-level folder would shift all projects under it, break saved VS Code workspaces, invalidate shell shortcuts, disconnect the active AI session, and lose path-tied memory. The repo's git history and remotes were never at risk, but the widespread setup breaks were not worth it, so I opted for a local symlink instead.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

I don't completely trust our Dense MRR@10 score of 0.983 on our own corpus. The candidate pool for our gold set was built by taking the top results from bm25, dense, and hybrid, meaning dense was only judged against documents it or the other retrievers already surfaced. To truly trust it, we would need an independent random sample of documents evaluated for relevance rather than a closed candidate pool.

I did not formally test this number against an unjudged document audit during the run. Across dense's top 300 results (top 10 for 30 queries), 89 were judged relevant, 168 were evaluated and judged not relevant, and 43 documents (14%) were never shown or evaluated at all.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

One thing that isn't right is query h05 ("What could be a realistic alternative to the more polluting energy sources?"), where the relevant document if12411 (Fusion Energy) was ranked way down at 104 by dense because fusion doesn't have working grid-connected reactors yet. This shows a mismatch in our relevance labeling, an unproven technology might not fit a "realistic" alternative label. To fix it, I'd re-examine our qrels file and clean up whether research-stage energy sources should count as relevant answers.

To find out if this labeling discrepancy matters, I would remove `if12411` from the relevance labels (`qrels`) for `h05` and re-score the runs to measure the precise shift in MRR@10 and nDCG@10 on `hand` queries.
