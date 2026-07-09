# review_hypo — create_idea

> Phase: `hypo_loop` · round 1 · `review_hypo`
> Run: `run_sAQsTTaaqjOV` — Near Duplicate Finder
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (sdk_openhands_agent, openrouter/tencent/hy3-preview)

### [1] CONFIG · 2026-07-03 17:52:59 UTC

```
Model: openrouter/tencent/hy3-preview | Session: c8ed3829-6a96-48fb-ab19-904e4a806a05 | CWD: /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo | Tools: 3 | Permission: acceptEdits
```

### [2] SYSTEM PROMPT · 2026-07-03 17:53:02 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>
```

### [3] SYSTEM-USER prompt · 2026-07-03 17:53:02 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<hypothesis>
kind: hypothesis
title: 'Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes'
hypothesis: >-
  By viewing MinHash as a lossy compression channel and applying fountain code (rateless erasure code) principles, we can
  create a rateless MinHash sketch that generates a potentially infinite sequence of hash values, enabling progressive refinement
  of Jaccard similarity estimates. The optimal stopping point (sketch size) can be determined from rate-distortion theory,
  achieving optimal space-accuracy trade-offs without knowing the target similarity distribution beforehand.
motivation: >-
  MinHash and its variants require fixing the sketch size (number of hash functions) upfront, before knowing the desired estimation
  accuracy or the distribution of Jaccard similarities in the dataset. This leads to either wasted space (oversized sketches)
  or insufficient accuracy (undersized sketches). A rateless MinHash would solve this by generating hash values on-demand,
  allowing progressive refinement of estimates until a target accuracy is reached. This is particularly valuable for distributed
  deduplication, streaming data, and applications where the optimal sketch size is data-dependent.
assumptions:
- >-
  Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean
  squared error in similarity estimation
- >-
  Fountain code principles (rateless coding) can be applied to generate a sequence of dependent hash values that together
  provide progressive Jaccard estimation
- >-
  The hash value sequence can be designed such that the estimation error decays monotonically as more values are received
- >-
  Rate-distortion theory can provide a computable bound for the optimal stopping point given a target estimation error
investigation_approach: >-
  1. Formalize MinHash as a rate-distortion problem: define the rate (sketch bits) and distortion (estimation error) for Jaccard
  similarity estimation. 2. Design a rateless MinHash scheme inspired by LT/Raptor fountain codes: generate a potentially
  infinite sequence of coded hash values from the set elements. 3. Derive the rate-distortion function for Jaccard estimation
  and use it to determine optimal stopping rules. 4. Implement the rateless MinHash algorithm and compare against standard
  MinHash, b-bit MinHash, and SetSketch on near-duplicate detection tasks. 5. Evaluate on LLM training data deduplication
  benchmarks (e.g., The Pile, C4) measuring space efficiency, estimation accuracy, and runtime.
success_criteria: >-
  The rateless MinHash scheme should: (1) Achieve the same Jaccard estimation accuracy as standard MinHash with less space
  on average (by adapting sketch size to each pair's similarity); (2) Provide progressive estimates that improve monotonically
  as more hash values are processed; (3) Have a computable stopping rule based on rate-distortion theory that achieves near-optimal
  space-accuracy trade-off; (4) Outperform fixed-size MinHash variants on datasets with diverse Jaccard similarity distributions.
related_works:
- >-
  Standard MinHash (Broder et al.) - uses k independent random permutations to estimate Jaccard similarity; our approach generalizes
  this to a rateless setting where k is not fixed upfront.
- >-
  b-bit MinHash (Li & Konig) - reduces sketch size by storing only b bits per hash value; our approach achieves variable sketch
  size through progressive refinement rather than fixed-size compression.
- >-
  SetSketch (Ertl) - bridges MinHash and HyperLogLog with a configurable parameter; our approach differs by making the sketch
  size itself adaptive rather than fixed at creation time.
- >-
  Polar Code Nearest-Neighbor (Touitou & Halabi) - uses error-correcting codes for LSH clustering; our approach applies coding
  theory to the hash function design itself, not just to the clustering step.
- >-
  ProbMinHash (Ertl) - computes probability Jaccard similarity for weighted sets; our approach addresses a different problem
  (rateless/progressive estimation) for unweighted Jaccard similarity.
- >-
  Odd Sketch (Mitzenmacher et al.) - uses binary sketches with XOR properties for high similarities; our approach targets
  the general case with progressive refinement rather than a fixed binary sketch.
inspiration: >-
  The hypothesis combines three cross-domain inspirations: (1) Fountain codes / rateless erasure codes from coding theory
  - where encoded symbols can be generated indefinitely and decoding becomes possible after receiving enough symbols; (2)
  Rate-distortion theory from information theory - which provides the optimal trade-off between compression rate and estimation
  distortion; (3) Progressive refinement from numerical analysis - where estimates are improved incrementally. The key insight
  is that MinHash sketches are essentially 'encoded' representations of sets, and by using coding-theoretic principles we
  can make this encoding rateless (adaptive to the desired accuracy).
terms:
- term: MinHash
  definition: >-
    A locality-sensitive hashing technique that estimates Jaccard similarity between two sets by computing the probability
    that the minimum hash value under a random permutation is the same for both sets.
- term: Jaccard similarity
  definition: >-
    A similarity measure for sets defined as the ratio of the intersection size to the union size: J(A,B) = |A∩B| / |A∪B|.
    It ranges from 0 (disjoint sets) to 1 (identical sets).
- term: Fountain code / rateless code
  definition: >-
    An erasure code that can generate an unlimited number of encoded symbols from a source message. The receiver can recover
    the original message after receiving any sufficient subset of encoded symbols, making the code 'rateless' (no fixed rate).
- term: Rate-distortion theory
  definition: >-
    A framework in information theory that studies the optimal trade-off between the compression rate (bits per symbol) and
    the resulting distortion (loss) in lossy data compression.
- term: Locality-sensitive hashing (LSH)
  definition: >-
    A family of hash functions where similar items are more likely to hash to the same value than dissimilar items. MinHash
    is an LSH family for Jaccard similarity.
- term: Progressive estimation
  definition: >-
    An estimation procedure where the accuracy improves monotonically as more computational resources (time, space, or data)
    are invested, without requiring the total resource budget to be fixed upfront.
summary: >-
  We propose Rateless MinHash, a new sketching approach that applies fountain code principles to MinHash, enabling progressive
  Jaccard similarity estimation where hash values are generated on-demand and the sketch size adapts to the desired accuracy.
  Rate-distortion theory provides the optimal stopping rule.
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for judging whether the hypothesis is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>





<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE:
This is the first iteration — there is no previous hypothesis. Leave
``relation_type`` null and ``relation_rationale`` empty.

Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [4] HUMAN-USER prompt · 2026-07-03 17:53:02 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [5] THINKING · 2026-07-03 17:53:06 UTC

```
Let me analyze this hypothesis carefully. The user has provided a hypothesis about "Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes" and wants me to provide a thorough peer review as if I'm an experienced conference reviewer.

Let me break down what I need to do:

1. **Ground my review in evidence** - I should search for relevant context about MinHash, fountain codes, rate-distortion theory as applied to similarity estimation, etc.

2. **Write a comprehensive review** with:
   - Overall assessment
   - Strengths
   - Dimension scores (soundness, presentation, contribution - each 1-4)
   - Critiques (with category, severity, description, suggested action)
   - Overall score (1-10)
   - Confidence (1-5)
   - Relation type and rationale (null for first iteration)

Let me first understand the hypothesis:
- It's proposing a "Rateless MinHash" that applies fountain code principles to MinHash
- The idea is to generate hash values on-demand for progressive Jaccard similarity estimation
- Rate-distortion theory would provide optimal stopping rules

Key concerns I should investigate:
1. Is this technically sound? Can fountain code principles actually be applied to MinHash?
2. Is this novel? Are there existing works on progressive MinHash or adaptive sketch sizes?
3. Is the rate-distortion framing appropriate for Jaccard estimation?
4. What are the related works that might already do something similar?

Let me search for relevant papers and context to ground my review. I should look for:
- MinHash variants and improvements
- Fountain codes applied to sketching/hashing
- Rate-distortion theory applied to similarity estimation
- Progressive estimation techniques for Jaccard similarity

Let me start by searching for relevant work
```

### [6] ASSISTANT · 2026-07-03 17:53:06 UTC

```
I'll conduct a thorough review of this hypothesis. Let me first search for relevant context to ground my review in the actual state of the field.
```

### [7] TOOL CALL — invoke_skill · 2026-07-03 17:53:06 UTC

```
{
  "name": "aii-web-research-tools"
}
```

### [8] TOOL RESULT — invoke_skill · 2026-07-03 17:53:06 UTC

````
{"content": [{"cache_prompt": false, "type": "text", "text": "## Available Web Tools\n\nThree levels of web tools:\n\n1. **WebSearch** \u2014 broad discovery. Returns titles, URLs, snippets. Cheapest. Use first to scan the landscape.\n2. **WebFetch** \u2014 read a specific page. LLM summarizes it. HTML only. May miss specific details.\n3. **aii_web_tools__fetch_grep** \u2014 exact text extraction from HTML or PDF. Regex matching with context windows.\n   Use for precise details, methodology, or when WebFetch missed something.\n   Key params: pattern (required), max_matches (default 20), context_chars (default 200 per side).\n\n**Workflow:** WebSearch \u2192 WebFetch for gist \u2192 aii_web_tools__fetch_grep for exact details or PDFs.\n\n**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly \u2014 bypassing the server:\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-research-tools\"\nuv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r \"$SKILL_DIR/scripts/server_requirements.txt\"\n```\n\n---\nThis skill is located at `/ai-inventor/.claude/skills/aii-web-research-tools`. Any files it references (e.g. under `scripts/`, `references/`, `assets/`) are relative to that directory."}], "is_error": false, "skill_name": "aii-web-research-tools", "kind": "InvokeSkillObservation"}
````

### [9] THINKING · 2026-07-03 17:53:10 UTC

```
Let me start by searching for relevant literature to ground my review. I need to check:
1. Current state of MinHash variants and their limitations
2. Whether anyone has applied fountain codes or rateless coding to hashing/similarity estimation
3. Rate-distortion theory applied to similarity estimation
4. What level of contribution is needed for top-tier venues in this area

Let me start with web searches to understand the landscape
```

### [10] ASSISTANT · 2026-07-03 17:53:10 UTC

```
Let me search for relevant literature to ground my review properly.
```

### [11] TOOL CALL — terminal · 2026-07-03 17:53:10 UTC

```
{
  "command": "cd /ai-inventor/.claude/skills/aii-web-research-tools && python3 scripts/web_search.py \"MinHash rateless fountain codes progressive estimation\" 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [12] TOOL RESULT — terminal · 2026-07-03 17:53:12 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "python3: can't open file '/ai-inventor/.claude/skills/aii-web-research-tools/scripts/web_search.py': [Errno 2] No such file or directory"}], "is_error": false, "command": "cd /ai-inventor/.claude/skills/aii-web-research-tools && python3 scripts/web_search.py \"MinHash rateless fountain codes progressive estimation\" 10", "exit_code": 2, "timeout": false, "metadata": {"exit_code": 2, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 2.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [13] THINKING · 2026-07-03 17:53:24 UTC

```
Let me think about what I need to do here. I'm supposed to be a hypothesis reviewer, and I need to review this hypothesis about "Rateless MinHash". The user wants me to provide a thorough peer review.

The instructions say I should:
1. Ground my review in evidence by searching for relevant context
2. Write a review with critiques categorized by methodology, evidence, novelty, clarity, scope, or rigor
3. Rate severity as major or minor
4. Provide actionable suggestions

However, I'm having trouble with the web research tools. Let me try a different approach - maybe I should just use standard web search tools that are available to me.

Actually, looking at the available tools, I have:
- terminal
- file_editor
- task_tracker
- finish
- think
- invoke_skill

The invoke_skill tool can invoke "aii-web-research-tools" but it seems like that didn't work properly. Let me try using standard web search by calling invoke_skill differently, or I could just proceed with my review based on my existing knowledge.

Actually, I realize I should step back and think about this more carefully. The task is to review a hypothesis. Let me analyze the hypothesis:

**Hypothesis Title:** Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes

**Key Idea:** Apply fountain code (rateless erasure code) principles to MinHash to create a rateless MinHash sketch that generates a potentially infinite sequence of hash values, enabling progressive refinement of Jaccard similarity estimates.

**Key Technical Claims:**
1. MinHash can be viewed as a lossy compression channel
2. Fountain code principles can be applied to generate dependent hash values
3. Rate-distortion theory can provide optimal stopping rules

**Investigation Approach:**
1. Formalize MinHash as a rate-distortion problem
2. Design rateless MinHash scheme inspired by LT/Raptor codes
3. Derive rate-distortion function for Jaccard estimation
4. Implement and compare against standard MinHash, b-bit MinHash, SetSketch
5. Evaluate on LLM training data deduplication benchmarks

Let me think about the novelty and technical soundness:

**Novelty:** This is actually quite novel. I'm not aware of anyone applying fountain codes to MinHash directly. The idea of making MinHash "rateless" (able to generate hash values on demand) is interesting and could be valuable.

**Technical Soundness:** This is where I have concerns. Let me think about whether the technical approach makes sense:

1. **MinHash as a lossy compression channel:** This framing is a bit unusual. MinHash is typically viewed as a locality-sensitive hashing scheme, not as a compression channel. The connection to rate-distortion theory is not straightforward.

2. **Applying fountain codes to MinHash:** Fountain codes work by generating encoded symbols from source symbols. In MinHash, we're hashing set elements. The analogy would be:
   - Source message = set elements
   - Encoded symbols = hash values
   - But in MinHash, each hash function gives us one value (the minimum hash), not multiple symbols
   
   To apply fountain codes, we'd need to generate multiple "coded" hash values from the same set. But how? The hypothesis says "generate a potentially infinite sequence of coded hash values from the set elements." This is vague.

3. **Rate-distortion for Jaccard estimation:** The rate-distortion function R(D) gives the minimum rate needed to achieve distortion D. For Jaccard estimation:
   - Rate = bits used for the sketch
   - Distortion = MSE of Jaccard estimate
   
   But computing R(D) for Jaccard estimation is non-trivial. The hypothesis claims this is possible but doesn't explain how.

**Potential Issues:**

1. **Vagueness in the technical approach:** The hypothesis says "generate a potentially infinite sequence of coded hash values" but doesn't explain how this is done. What's the coding scheme? How are the coded hash values generated?

2. **Unclear connection between fountain codes and MinHash:** Fountain codes are for erasure channels - you generate encoded symbols and the receiver can decode after receiving enough symbols. But in MinHash, we're not trying to "decode" the original set - we're trying to estimate Jaccard similarity. The analogy is unclear.

3. **Rate-distortion derivation:** The hypothesis claims "derive the rate-distortion function for Jaccard estimation" but this is non-trivial. What's the source distribution? What's the distortion measure? How do you compute R(D)?

Let me try to search for related work using a different approach. Actually, let me just try using WebSearch directly since I should have access to it...

Wait, I see the issue. The available tools listed are:
- terminal
- file_editor  
- task_tracker
- finish
- think
- invoke_skill

But in the general instructions at the top, it mentions:
"- Web research is available through the aii-web-tools skill, in three levels (broad → specific):
1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs."

So I should have access to web tools. Let me try invoking the aii-web-tools skill.

Actually, I realize I should just proceed with writing the review based on my knowledge. The key issues I see are:

**Major Issues:**
1. The technical approach is vague - how exactly do you apply fountain codes to MinHash?
2. The connection between rate-distortion theory and Jaccard estimation is not well-established
3. The hypothesis makes strong claims without explaining the technical details

**Minor Issues:**
1. The related work section could be more comprehensive
2. The evaluation plan is reasonable but could be more specific

Let me write the review now. But first, let me try one more time to access web search...

Actually, you know what, let me just proceed with writing the review. I have enough knowledge to write a thorough review. The key is to be specific and actionable in my critiques.

Let me structure my review:

**Overall Assessment:** The hypothesis presents an interesting and novel idea (applying fountain codes to MinHash), but the technical approach is under-specified and may not be feasible. The connection to rate-distortion theory is unclear. Major revisions are needed before experiments can be run.

**Strengths:**
1. Novel combination of coding theory and LSH
2. Addresses a real problem (fixed sketch size in MinHash)
3. Clear motivation and potential impact

**Weaknesses:**
1. Technical approach is vague (how exactly to apply fountain codes?)
2. Unclear connection to rate-distortion theory
3. May not be technically feasible

**Specific Critiques:**

1. **Methodology (Major):** The hypothesis claims to "generate a potentially infinite sequence of coded hash values" but doesn't explain how. Fountain codes work by encoding source symbols into encoded symbols. What are the source symbols in MinHash? What's the encoding scheme? How do you generate coded hash values?

   Suggested Action: Provide a concrete algorithmic description of how fountain code principles are applied to MinHash. What's the equivalent of "source symbols"? How are "encoded symbols" (coded hash values) generated? What's the decoding process for estimating Jaccard similarity?

2. **Methodology (Major):** The connection to rate-distortion theory is unclear. The hypothesis claims "derive the rate-distortion function for Jaccard estimation" but doesn't explain how. What's the source distribution? What's the distortion measure? How do you compute R(D)?

   Suggested Action: Provide a concrete formulation of the rate-distortion problem for Jaccard estimation. Define the source distribution, the rate (bits per sketch), the distortion (MSE? Something else?), and explain how R(D) would be computed.

3. **Novelty (Minor):** The related work section is good but could be more comprehensive. Are there any works on progressive estimation for LSH? Any works applying coding theory to hashing?

   Suggested Action: Search for and cite works on progressive LSH estimation, coding-theoretic approaches to hashing, and any related work on adaptive sketch sizes.

4. **Clarity (Minor):** The hypothesis uses terms like "lossy compression channel" and "rate-distortion problem" without defining them in the context of MinHash. This makes it hard to evaluate the technical claims.

   Suggested Action: Provide clear definitions and formulations. Define exactly what is being compressed, what is the "channel", what is the rate, what is the distortion.

Let me now write the actual review in the required JSON format.

Actually, I realize I should try to access web search one more time. Let me try invoking the skill properly...

Actually, you know what, I just noticed something. The available tools section at the very top says:

"Web research is available through the aii-web-tools skill, in three levels (broad → specific):
1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs."

But these are not listed in the "available function calls" section. So maybe I don't have access to web search? Let me just proceed with writing the review based on my knowledge.

Hmm, but actually, I should have access to web search. Let me try a different approach - let me just use the terminal to do a web search using curl or something...

Actually, that's overcomplicating things. Let me just write the review now. I have enough knowledge to write a thorough and fair review.

Let me write the review in the required JSON format.
```

### [14] ASSISTANT · 2026-07-03 17:53:24 UTC

```
Let me first check the user uploads folder for any relevant reference materials, then search for related work to ground my review.
```

### [15] TOOL CALL — terminal · 2026-07-03 17:53:24 UTC

```
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads/ 2>/dev/null || echo \"No user uploads directory found\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [16] TOOL RESULT — terminal · 2026-07-03 17:53:26 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1954\ndrwxr-xr-x 2 root root       1 Jul  3 17:42 .\ndrwxr-xr-x 8 root root 2000355 Jul  3 17:43 .."}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads/ 2>/dev/null || echo \"No user uploads directory found\"", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [17] ASSISTANT · 2026-07-03 17:53:30 UTC

```
Let me search for relevant literature to properly evaluate this hypothesis. I'll use web search to find related work.
```

### [18] TOOL CALL — terminal · 2026-07-03 17:53:30 UTC

```
{
  "command": "python3 -c \"\nimport requests\nimport json\n\n# Search for MinHash variants and related work\nqueries = [\n    'MinHash progressive estimation adaptive sketch size',\n    'fountain codes hashing similarity estimation',\n    'rate-distortion theory MinHash Jaccard estimation',\n    'adaptive MinHash sketch size',\n    'rateless codes similarity search'\n]\n\nfor q in queries:\n    print(f'Query: {q}')\n    # Use arXiv API to search\n    url = f'http://export.arxiv.org/api/query?search_query=all:{q.replace(\\\" \\\", \\\"+\\\")}&start=0&max_results=5'\n    try:\n        r = requests.get(url, timeout=10)\n        print(f'  Status: {r.status_code}')\n    except Exception as e:\n        print(f'  Error: {e}')\n\" 2>&1 | head -100\n",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [19] TOOL RESULT — terminal · 2026-07-03 17:53:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "python3 -c \"\nimport requests\nimport json\n# Search for MinHash variants and related work\nqueries = [\n    'MinHash progressive estimation adaptive sketch size',\n    'fountain codes hashing similarity estimation',\n    'rate-distortion theory MinHash Jaccard estimation',\n    'adaptive MinHash sketch size',\n    'rateless codes similarity search'\n]\nfor q in queries:\n    print(f'Query: {q}')\n    # Use arXiv API to search\n    url = f'http://export.arxiv.org/api/query?search_query=all:{q.replace(\\\" \\\", \\\"+\\\")}&start=0&max_results=5'\n    try:\n        r = requests.get(url, timeout=10)\n        print(f'  Status: {r.status_code}')\n    except Exception as e:\n        print(f'  Error: {e}')\n\" 2>&1 | head -100\nQuery: MinHash progressive estimation adaptive sketch size\n  Status: 200\nQuery: fountain codes hashing similarity estimation\n  Status: 200\nQuery: rate-distortion theory MinHash Jaccard estimation\n  Status: 200\nQuery: adaptive MinHash sketch size\n  Status: 200\nQuery: rateless codes similarity search\n  Status: 200"}], "is_error": false, "command": "python3 -c \"\nimport requests\nimport json\n\n# Search for MinHash variants and related work\nqueries = [\n    'MinHash progressive estimation adaptive sketch size',\n    'fountain codes hashing similarity estimation',\n    'rate-distortion theory MinHash Jaccard estimation',\n    'adaptive MinHash sketch size',\n    'rateless codes similarity search'\n]\n\nfor q in queries:\n    print(f'Query: {q}')\n    # Use arXiv API to search\n    url = f'http://export.arxiv.org/api/query?search_query=all:{q.replace(\\\" \\\", \\\"+\\\")}&start=0&max_results=5'\n    try:\n        r = requests.get(url, timeout=10)\n        print(f'  Status: {r.status_code}')\n    except Exception as e:\n        print(f'  Error: {e}')\n\" 2>&1 | head -100", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [20] ASSISTANT · 2026-07-03 17:53:40 UTC

```
Let me search more thoroughly for relevant literature using available tools. I'll use web search to find related work.
```

### [21] TOOL CALL — terminal · 2026-07-03 17:53:40 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:MinHash+adaptive+sketch&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -40",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [22] TOOL RESULT — terminal · 2026-07-03 17:53:42 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:MinHash OR all:adaptive OR all:sketch&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>Unconstrained Face Sketch Synthesis via Perception-Adaptive Network and A New Benchmark</title>\n    <summary>Face sketch generation has attracted much attention in the field of visual computing. However, existing methods either are limited to constrained conditions or heavily rely on various preprocessing steps to deal with in-the-wild cases. In this paper, we argue that accurately perceiving facial region and facial components is crucial for unconstrained sketch synthesis. To this end, we propose a novel Perception-Adaptive Network (PANet), which can generate high-quality face sketches under unconstrained conditions in an end-to-end scheme. Specifically, our PANet is composed of i) a Fully Convolutional Encoder for hierarchical feature extraction, ii) a Face-Adaptive Perceiving Decoder for extracting potential facial region and handling face variations, and iii) a Component-Adaptive Perceiving Module for facial component aware feature representation learning. To facilitate further researches of unconstrained face sketch synthesis, we introduce a new benchmark termed WildSketch, which contains 800 pairs of face photo-sketch with large variations in pose, expression, ethnic origin, background, and illumination. Extensive experiments demonstrate that the proposed method is capable of achieving state-of-the-art performance under both constrained and unconstrained conditions. Our source codes and the WildSketch benchmark are resealed on the project page http://lingboliu.com/unconstrained_face_sketch.html.</summary>\n    <title>SketchAgent: Language-Driven Sequential Sketch Generation</title>\n    <summary>Sketching serves as a versatile tool for externalizing ideas, enabling rapid exploration and visual communication that spans various disciplines. While artificial systems have driven substantial advances in content creation and human-computer interaction, capturing the dynamic and abstract nature of human sketching remains challenging. In this work, we introduce SketchAgent, a language-driven, sequential sketch generation method that enables users to create, modify, and refine sketches through dynamic, conversational interactions. Our approach requires no training or fine-tuning. Instead, we leverage the sequential nature and rich prior knowledge of off-the-shelf multimodal large language models (LLMs). We present an intuitive sketching language, introduced to the model through in-context examples, enabling it to \"draw\" using string-based actions. These are processed into vector graphics and then rendered to create a sketch on a pixel canvas, which can be accessed again for further tasks. By drawing stroke by stroke, our agent captures the evolving, dynamic qualities intrinsic to sketching. We demonstrate that SketchAgent can generate sketches from diverse prompts, engage in dialogue-driven drawing, and collaborate meaningfully with human users.</summary>\n    <title>Engineering Sketch Generation for Computer-Aided Design</title>\n    <summary>Engineering sketches form the 2D basis of parametric Computer-Aided Design (CAD), the foremost modeling paradigm for manufactured objects. In this paper we tackle the problem of learning based engineering sketch generation as a first step towards synthesis and composition of parametric CAD models. We propose two generative models, CurveGen and TurtleGen, for engineering sketch generation. Both models generate curve primitives without the need for a sketch constraint solver and explicitly consider topology for downstream use with constraints and 3D CAD modeling operations. We find in our perceptual evaluation using human subjects that both CurveGen and TurtleGen produce more realistic engineering sketches when compared with the current state-of-the-art for engineering sketch generation.</summary>\n    <title>Real-Time Device Reach Forecasting Using HLL and MinHash Data Sketches</title>\n    <summary>Predicting the right number of TVs (Device Reach) in real-time based on a user-specified targeting attributes is imperative for running multi-million dollar ADs business. The traditional approach of SQL queries to join billions of records across multiple targeting dimensions is extremely slow. As a workaround, many applications will have an offline process to crunch these numbers and present the results after many hours. In our case, the solution was an offline process taking 24 hours to onboard a customer resulting in a potential loss of business. To solve this problem, we have built a new real-time prediction system using MinHash and HyperLogLog (HLL) data sketches to compute the device reach at runtime when a user makes a request. However, existing MinHash implementations do not solve the complex problem of multilevel aggregation and intersection. This work will show how we have solved this problem, in addition, we have improved MinHash algorithm to run 4 times faster using Single Instruction Multiple Data (SIMD) vectorized operations for high speed and accuracy with constant space to process billions of records. Finally, by experiments, we prove that the results are as accurate as traditional offline prediction system with an acceptable error rate of 5%.</summary>\n    <title>Unsupervised Sketch-to-Photo Synthesis</title>\n    <summary>Humans can envision a realistic photo given a free-hand sketch that is not only spatially imprecise and geometrically distorted but also without colors and visual details. We study unsupervised sketch-to-photo synthesis for the first time, learning from unpaired sketch-photo data where the target photo for a sketch is unknown during training. Existing works only deal with style change or spatial deformation alone, synthesizing photos from edge-aligned line drawings or transforming shapes within the same modality, e.g., color images. Our key insight is to decompose unsupervised sketch-to-photo synthesis into a two-stage translation task: First shape translation from sketches to grayscale photos and then content enrichment from grayscale to color photos. We also incorporate a self-supervised denoising objective and an attention module to handle abstraction and style variations that are inherent and specific to sketches. Our synthesis is sketch-faithful and photo-realistic to enable sketch-based image retrieval in practice. An exciting corollary product is a universal and promising sketch generator that captures human visual perception beyond the edge map of a photo.</summary>\n    <title>Conditional Human Sketch Synthesis with Explicit Abstraction Control</title>\n    <summary>This paper presents a novel free-hand sketch synthesis approach addressing explicit abstraction control in class-conditional and photo-to-sketch synthesis. Abstraction is a vital aspect of sketches, as it defines the fundamental distinction between a sketch and an image. Previous works relied on implicit control to achieve different levels of abstraction, leading to inaccurate control and synthesized sketches deviating from human sketches. To resolve this challenge, we propose two novel abstraction control mechanisms, state embeddings and the stroke token, integrated into a transformer-based latent diffusion model (LDM). These mechanisms explicitly provide the required amount of points or strokes to the model, enabling accurate point-level and stroke-level control in synthesized sketches while preserving recognizability. Outperforming state-of-the-art approaches, our method effectively generates diverse, non-rigid and human-like sketches. The proposed approach enables coherent sketch synthesis and excels in representing human habits with desired abstraction levels, highlighting the potential of sketch synthesis for real-world applications.</summary>\n    <title>HyperMinHash: MinHash in LogLog space</title>\n    <summary>In this extended abstract, we describe and analyze a lossy compression of MinHash from buckets of size $O(\\log n)$ to buckets of size $O(\\log\\log n)$ by encoding using floating-point notation. This new compressed sketch, which we call HyperMinHash, as we build off a HyperLogLog scaffold, can be used as a drop-in replacement of MinHash. Unlike comparable Jaccard index fingerprinting algorithms in sub-logarithmic space (such as b-bit MinHash), HyperMinHash retains MinHash's features of streaming updates, unions, and cardinality estimation. For a multiplicative approximation error $1+ \u03b5$ on a Jaccard index $ t $, given a random oracle, HyperMinHash needs $O\\left(\u03b5^{-2} \\left( \\log\\log n + \\log \\frac{1}{ t \u03b5} \\right)\\right)$ space. HyperMinHash allows estimating Jaccard indices of 0.01 for set cardinalities on the order of $10^{19}$ with relative error of around 10\\% using 64KiB of memory; MinHash can only estimate Jaccard indices for cardinalities of $10^{10}$ with the same memory consumption.</summary>\n    <title>One-shot Face Sketch Synthesis in the Wild via Generative Diffusion Prior and Instruction Tuning</title>\n    <summary>Face sketch synthesis is a technique aimed at converting face photos into sketches. Existing face sketch synthesis research mainly relies on training with numerous photo-sketch sample pairs from existing datasets. However, these large-scale discriminative learning methods will have to face problems such as data scarcity and high human labor costs. Once the training data becomes scarce, their generative performance significantly degrades. In this paper, we propose a one-shot face sketch synthesis method based on diffusion models. We optimize text instructions on a diffusion model using face photo-sketch image pairs. Then, the instructions derived through gradient-based optimization are used for inference. To simulate real-world scenarios more accurately and evaluate method effectiveness more comprehensively, we introduce a new benchmark named One-shot Face Sketch Dataset (OS-Sketch). The benchmark consists of 400 pairs of face photo-sketch images, including sketches with different styles and photos with different backgrounds, ages, sexes, expressions, illumination, etc. For a solid out-of-distribution evaluation, we select only one pair of images for training at each time, with the rest used for inference. Extensive experiments demonstrate that the proposed method can convert various photos into realistic and highly consistent sketches in a one-shot context. Compared to other methods, our approach offers greater convenience and broader applicability. The dataset will be available at: https://github.com/HanWu3125/OS-Sketch</summary>\n    <title>On Training Sketch Recognizers for New Domains</title>\n    <summary>Sketch recognition algorithms are engineered and evaluated using publicly available datasets contributed by the sketch recognition community over the years. While existing datasets contain sketches of a limited set of generic objects, each new domain inevitably requires collecting new data for training domain specific recognizers. This gives rise to two fundamental concerns: First, will the data collection protocol yield ecologically valid data? Second, will the amount of collected data suffice to train sufficiently accurate classifiers? In this paper, we draw attention to these two concerns. We show that the ecological validity of the data collection protocol and the ability to accommodate small datasets are significant factors impacting recognizer accuracy in realistic scenarios. More specifically, using sketch-based gaming as a use case, we show that deep learning methods, as well as more traditional methods, suffer significantly from dataset shift. Furthermore, we demonstrate that in realistic scenarios where data is scarce and expensive, standard measures taken for adapting deep learners to small datasets fall short of comparing favorably with alternatives. Although transfer learning, and extensive data augmentation help deep learners, they still perform significantly worse compared to standard setups (e.g., SVMs and GBMs with standard feature representations). We pose learning from small datasets as a key problem for the deep sketch recognition field, one which has been ignored in the bulk of the existing literature.</summary>\n    <title>Learning Dense Correspondences between Photos and Sketches</title>\n    <summary>Humans effortlessly grasp the connection between sketches and real-world objects, even when these sketches are far from realistic. Moreover, human sketch understanding goes beyond categorization -- critically, it also entails understanding how individual elements within a sketch correspond to parts of the physical world it represents. What are the computational ingredients needed to support this ability? Towards answering this question, we make two contributions: first, we introduce a new sketch-photo correspondence benchmark, $\\textit{PSC6k}$, containing 150K annotations of 6250 sketch-photo pairs across 125 object categories, augmenting the existing Sketchy dataset with fine-grained correspondence metadata. Second, we propose a self-supervised method for learning dense correspondences between sketch-photo pairs, building upon recent advances in correspondence learning for pairs of photos. Our model uses a spatial transformer network to estimate the warp flow between latent representations of a sketch and photo extracted by a contrastive learning-based ConvNet backbone. We found that this approach outperformed several strong baselines and produced predictions that were quantitatively consistent with other warp-based methods. However, our benchmark also revealed systematic differences between predictions of the suite of models we tested and those of humans. Taken together, our work suggests a promising path towards developing artificial systems that achieve more human-like understanding of visual images at different levels of abstraction. Project page: https://photo-sketch-correspondence.github.io</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:MinHash+adaptive+sketch&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -40", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [23] ASSISTANT · 2026-07-03 17:53:44 UTC

```
Let me search more specifically for MinHash variants and related work in sketching and coding theory.
```

### [24] TOOL CALL — terminal · 2026-07-03 17:53:44 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:SetSketch+OR+all:b-bit+MinHash+OR+all:HyperMinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [25] TOOL RESULT — terminal · 2026-07-03 17:53:46 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:SetSketch OR all:b-bit OR all:MinHash OR all:HyperMinHash&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>HyperMinHash: MinHash in LogLog space</title>\n    <summary>In this extended abstract, we describe and analyze a lossy compression of MinHash from buckets of size $O(\\log n)$ to buckets of size $O(\\log\\log n)$ by encoding using floating-point notation. This new compressed sketch, which we call HyperMinHash, as we build off a HyperLogLog scaffold, can be used as a drop-in replacement of MinHash. Unlike comparable Jaccard index fingerprinting algorithms in sub-logarithmic space (such as b-bit MinHash), HyperMinHash retains MinHash's features of streaming updates, unions, and cardinality estimation. For a multiplicative approximation error $1+ \u03b5$ on a Jaccard index $ t $, given a random oracle, HyperMinHash needs $O\\left(\u03b5^{-2} \\left( \\log\\log n + \\log \\frac{1}{ t \u03b5} \\right)\\right)$ space. HyperMinHash allows estimating Jaccard indices of 0.01 for set cardinalities on the order of $10^{19}$ with relative error of around 10\\% using 64KiB of memory; MinHash can only estimate Jaccard indices for cardinalities of $10^{10}$ with the same memory consumption.</summary>\n    <title>SetSketch: Filling the Gap between MinHash and HyperLogLog</title>\n    <summary>MinHash and HyperLogLog are sketching algorithms that have become indispensable for set summaries in big data applications. While HyperLogLog allows counting different elements with very little space, MinHash is suitable for the fast comparison of sets as it allows estimating the Jaccard similarity and other joint quantities. This work presents a new data structure called SetSketch that is able to continuously fill the gap between both use cases. Its commutative and idempotent insert operation and its mergeable state make it suitable for distributed environments. Fast, robust, and easy-to-implement estimators for cardinality and joint quantities, as well as the ability to use SetSketch for similarity search, enable versatile applications. The presented joint estimator can also be applied to other data structures such as MinHash, HyperLogLog, or HyperMinHash, where it even performs better than the corresponding state-of-the-art estimators in many cases.</summary>\n    <title>A Review for Weighted MinHash Algorithms</title>\n    <summary>Data similarity (or distance) computation is a fundamental research topic which underpins many high-level applications based on similarity measures in machine learning and data mining. However, in large-scale real-world scenarios, the exact similarity computation has become daunting due to \"3V\" nature (volume, velocity and variety) of big data. In such cases, the hashing techniques have been verified to efficiently conduct similarity estimation in terms of both theory and practice. Currently, MinHash is a popular technique for efficiently estimating the Jaccard similarity of binary sets and furthermore, weighted MinHash is generalized to estimate the generalized Jaccard similarity of weighted sets. This review focuses on categorizing and discussing the existing works of weighted MinHash algorithms. In this review, we mainly categorize the Weighted MinHash algorithms into quantization-based approaches, \"active index\"-based ones and others, and show the evolution and inherent connection of the weighted MinHash algorithms, from the integer weighted MinHash algorithms to real-valued weighted MinHash ones (particularly the Consistent Weighted Sampling scheme). Also, we have developed a python toolbox for the algorithms, and released it in our github. Based on the toolbox, we experimentally conduct a comprehensive comparative study of the standard MinHash algorithm and the weighted MinHash ones.</summary>\n    <title>In Defense of MinHash Over SimHash</title>\n    <summary>MinHash and SimHash are the two widely adopted Locality Sensitive Hashing (LSH) algorithms for large-scale data processing applications. Deciding which LSH to use for a particular problem at hand is an important question, which has no clear answer in the existing literature. In this study, we provide a theoretical answer (validated by experiments) that MinHash virtually always outperforms SimHash when the data are binary, as common in practice such as search.\n    <title>C-MinHash: Rigorously Reducing $K$ Permutations to Two</title>\n    <summary>Minwise hashing (MinHash) is an important and practical algorithm for generating random hashes to approximate the Jaccard (resemblance) similarity in massive binary (0/1) data. The basic theory of MinHash requires applying hundreds or even thousands of independent random permutations to each data vector in the dataset, in order to obtain reliable results for (e.g.,) building large-scale learning models or approximate near neighbor search in massive data. In this paper, we propose {\\bf Circulant MinHash (C-MinHash)} and provide the surprising theoretical results that we just need \\textbf{two} independent random permutations. For C-MinHash, we first conduct an initial permutation on the data vector, then we use a second permutation to generate hash values. Basically, the second permutation is re-used $K$ times via circulant shifting to produce $K$ hashes. Unlike classical MinHash, these $K$ hashes are obviously correlated, but we are able to provide rigorous proofs that we still obtain an unbiased estimate of the Jaccard similarity and the theoretical variance is uniformly smaller than that of the classical MinHash with $K$ independent permutations. The theoretical proofs of C-MinHash require some non-trivial efforts. Numerical experiments are conducted to justify the theory and demonstrate the effectiveness of C-MinHash.</summary>\n    <title>Real-Time Device Reach Forecasting Using HLL and MinHash Data Sketches</title>\n    <summary>Predicting the right number of TVs (Device Reach) in real-time based on a user-specified targeting attributes is imperative for running multi-million dollar ADs business. The traditional approach of SQL queries to join billions of records across multiple targeting dimensions is extremely slow. As a workaround, many applications will have an offline process to crunch these numbers and present the results after many hours. In our case, the solution was an offline process taking 24 hours to onboard a customer resulting in a potential loss of business. To solve this problem, we have built a new real-time prediction system using MinHash and HyperLogLog (HLL) data sketches to compute the device reach at runtime when a user makes a request. However, existing MinHash implementations do not solve the complex problem of multilevel aggregation and intersection. This work will show how we have solved this problem, in addition, we have improved MinHash algorithm to run 4 times faster using Single Instruction Multiple Data (SIMD) vectorized operations for high speed and accuracy with constant space to process billions of records. Finally, by experiments, we prove that the results are as accurate as traditional offline prediction system with an acceptable error rate of 5%.</summary>\n    <title>PrivMin: Differentially Private MinHash for Jaccard Similarity Computation</title>\n    <summary>In many industrial applications of big data, the Jaccard Similarity Computation has been widely used to measure the distance between two profiles or sets respectively owned by two users. Yet, one semi-honest user with unpredictable knowledge may also deduce the private or sensitive information (e.g., the existence of a single element in the original sets) of the other user via the shared similarity. In this paper, we aim at solving the privacy issues in Jaccard similarity computation with strict differential privacy guarantees. To achieve this, we first define the Conditional $\u03b5$-DPSO, a relaxed differential privacy definition regarding set operations, and prove that the MinHash-based Jaccard Similarity Computation (MH-JSC) satisfies this definition. Then for achieving strict differential privacy in MH-JSC, we propose the PrivMin algorithm, which consists of two private operations: 1) the Private MinHash Value Generation that works by introducing the Exponential noise to the generation of MinHash signature. 2) the Randomized MinHashing Steps Selection that works by adopting Randomized Response technique to privately select several steps within the MinHashing phase that are deployed with the Exponential mechanism. Experiments on real datasets demonstrate that the proposed PrivMin algorithm can successfully retain the utility of the computed similarity while preserving privacy.</summary>\n    <title>b-Bit Minwise Hashing</title>\n    <summary>  This paper establishes the theoretical framework of b-bit minwise hashing. The original minwise hashing method has become a standard technique for estimating set similarity (e.g., resemblance) with applications in information retrieval, data management, social networks and computational advertising.\n    <title>b-Bit Minwise Hashing for Large-Scale Linear SVM</title>\n    <summary>In this paper, we propose to (seamlessly) integrate b-bit minwise hashing with linear SVM to substantially improve the training (and testing) efficiency using much smaller memory, with essentially no loss of accuracy. Theoretically, we prove that the resemblance matrix, the minwise hashing matrix, and the b-bit minwise hashing matrix are all positive definite matrices (kernels). Interestingly, our proof for the positive definiteness of the b-bit minwise hashing kernel naturally suggests a simple strategy to integrate b-bit hashing with linear SVM. Our technique is particularly useful when the data can not fit in memory, which is an increasingly critical issue in large-scale machine learning. Our preliminary experimental results on a publicly available webspam dataset (350K samples and 16 million dimensions) verified the effectiveness of our algorithm. For example, the training time was reduced to merely a few seconds. In addition, our technique can be easily extended to many other linear and nonlinear machine learning applications such as logistic regression.</summary>\n    <title>Pb-Hash: Partitioned b-bit Hashing</title>\n    <summary>Many hashing algorithms including minwise hashing (MinHash), one permutation hashing (OPH), and consistent weighted sampling (CWS) generate integers of $B$ bits. With $k$ hashes for each data vector, the storage would be $B\\times k$ bits; and when used for large-scale learning, the model size would be $2^B\\times k$, which can be expensive. A standard strategy is to use only the lowest $b$ bits out of the $B$ bits and somewhat increase $k$, the number of hashes. In this study, we propose to re-use the hashes by partitioning the $B$ bits into $m$ chunks, e.g., $b\\times m =B$. Correspondingly, the model size becomes $m\\times 2^b \\times k$, which can be substantially smaller than the original $2^B\\times k$."}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:SetSketch+OR+all:b-bit+MinHash+OR+all:HyperMinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [26] THINKING · 2026-07-03 17:53:54 UTC

```
Let me gather more information about fountain codes and rate-distortion theory as applied to hashing/similarity estimation. I need to understand if this is a genuinely novel idea or if there's existing work I should be aware of.

Let me search for fountain codes in the context of sketching or hashing
```

### [27] ASSISTANT · 2026-07-03 17:53:54 UTC

```
Let me search for fountain codes applied to hashing and similarity estimation.
```

### [28] TOOL CALL — terminal · 2026-07-03 17:53:54 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:fountain+code+sketch+OR+all:rateless+code+hashing&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [29] TOOL RESULT — terminal · 2026-07-03 17:53:54 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:fountain OR all:code OR all:sketch OR all:rateless OR all:code OR all:hashing&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>JaCoText: A Pretrained Model for Java Code-Text Generation</title>\n    <summary>Pretrained transformer-based models have shown high performance in natural language generation task. However, a new wave of interest has surged: automatic programming language generation. This task consists of translating natural language instructions to a programming code. Despite the fact that well-known pretrained models on language generation have achieved good performance in learning programming languages, effort is still needed in automatic code generation. In this paper, we introduce JaCoText, a model based on Transformers neural network. It aims to generate java source code from natural language text. JaCoText leverages advantages of both natural language and code generation models. More specifically, we study some findings from the state of the art and use them to (1) initialize our model from powerful pretrained models, (2) explore additional pretraining on our java dataset, (3) carry out experiments combining the unimodal and bimodal data in the training, and (4) scale the input and output length during the fine-tuning of the model. Conducted experiments on CONCODE dataset show that JaCoText achieves new state-of-the-art results.</summary>\n    <title>Distributed Rateless Codes with UEP Property</title>\n    <summary>When multiple sources of data need to transmit their rateless coded symbols through a single relay to a common destination, a distributed rateless code instead of several separate conventional rateless codes can be employed to encode the input symbols to increase the transmission efficiency and flexibility.\n    <title>Deterministic Rateless Codes for BSC</title>\n    <summary>A rateless code encodes a finite length information word into an infinitely long codeword such that longer prefixes of the codeword can tolerate a larger fraction of errors. A rateless code achieves capacity for a family of channels if, for every channel in the family, reliable communication is obtained by a prefix of the code whose rate is arbitrarily close to the channel's capacity. As a result, a universal encoder can communicate over all channels in the family while simultaneously achieving optimal communication overhead. In this paper, we construct the first \\emph{deterministic} rateless code for the binary symmetric channel. Our code can be encoded and decoded in $O(\u03b2)$ time per bit and in almost logarithmic parallel time of $O(\u03b2\\log n)$, where $\u03b2$ is any (arbitrarily slow) super-constant function. Furthermore, the error probability of our code is almost exponentially small $\\exp(-\u03a9(n/\u03b2))$. Previous rateless codes are probabilistic (i.e., based on code ensembles), require polynomial time per bit for decoding, and have inferior asymptotic error probabilities. Our main technical contribution is a constructive proof for the existence of an infinite generating matrix that each of its prefixes induce a weight distribution that approximates the expected weight distribution of a random linear code.</summary>\n    <title>Fountain Codes with Varying Probability Distributions</title>\n    <summary>Fountain codes are rateless erasure-correcting codes, i.e., an essentially infinite stream of encoded packets can be generated from a finite set of data packets. Several fountain codes have been proposed recently to minimize overhead, many of which involve modifications of the Luby transform (LT) code. These fountain codes, like the LT code, have the implicit assumption that the probability distribution is fixed throughout the encoding process. In this paper, we will use the theory of posets to show that this assumption is unnecessary, and by dropping it, we can achieve overhead reduction by as much as 64% lower than LT codes. We also present the fundamental theory of probability distribution designs for fountain codes with non-constant probability distributions that minimize overhead.</summary>\n    <title>Intermediate Performance of Rateless Codes</title>\n    <summary>  Rateless/fountain codes are designed so that all input symbols can be recovered from a slightly larger number of coded symbols, with high probability using an iterative decoder. In this paper we investigate the number of input symbols that can be recovered by the same decoder, but when the number of coded symbols available is less than the total number of input symbols. Of course recovery of all inputs is not possible, and the fraction that can be recovered will depend on the output degree distribution of the code.\n    <title>Multiple Access Analog Fountain Codes</title>\n    <summary>In this paper, we propose a novel rateless multiple access scheme based on the recently proposed capacity-approaching analog fountain code (AFC). We show that the multiple access process will create an equivalent analog fountain code, referred to as the multiple access analog fountain code (MA-AFC), at the destination. Thus, the standard belief propagation (BP) decoder can be effectively used to jointly decode all the users. We further analyse the asymptotic performance of the BP decoder by using a density evolution approach and show that the average log-likelihood ratio (LLR) of each user's information symbol is proportional to its transmit signal to noise ratio (SNR), when all the users utilize the same AFC code. Simulation results show that the proposed scheme can approach the sum-rate capacity of the Gaussian multiple access channel in a wide range of signal to noise ratios.</summary>\n    <title>Capacity-Achieving Rateless Polar Codes</title>\n    <summary>A rateless coding scheme transmits incrementally more and more coded bits over an unknown channel until all the information bits are decoded reliably by the receiver. We propose a new rateless coding scheme based on polar codes, and we show that this scheme is capacity-achieving, i.e. its information rate is as good as the best code specifically designed for the unknown channel. Previous rateless coding schemes are designed for specific classes of channels such as AWGN channels, binary erasure channels, etc. but the proposed rateless coding scheme is capacity-achieving for broad classes of channels as long as they are ordered via degradation. Moreover, it inherits the conceptual and computational simplicity of polar codes.</summary>\n    <title>Primitive Rateless Codes</title>\n    <summary>In this paper, we propose primitive rateless (PR) codes. A PR code is characterized by the message length and a primitive polynomial over $\\mathbf{GF}(2)$, which can generate a potentially limitless number of coded symbols. We show that codewords of a PR code truncated at any arbitrary length can be represented as subsequences of a maximum-length sequence ($m$-sequence). We characterize the Hamming weight distribution of PR codes and their duals and show that for a properly chosen primitive polynomial, the Hamming weight distribution of the PR code can be well approximated by the truncated binomial distribution. We further find a lower bound on the minimum Hamming weight of PR codes and show that there always exists a PR code that can meet this bound for any desired codeword length. We provide a list of primitive polynomials for message lengths up to $40$ and show that the respective PR codes closely meet the Gilbert-Varshamov bound at various rates. Simulation results show that PR codes can achieve similar block error rates as their BCH counterparts at various signal-to-noise ratios (SNRs) and code rates. PR codes are rate-compatible and can generate as many coded symbols as required; thus, demonstrating a truly rateless performance.</summary>\n    <title>Zigzag Decodable Fountain Codes</title>\n    <summary>This paper proposes a fountain coding system which has lower space decoding complexity and lower decoding erasure rate than the Raptor coding systems. The main idea of the proposed fountain code is employing shift and exclusive OR to generate the output packets. This technique is known as the zigzag decodable code, which is efficiently decoded by the zigzag decoder. In other words, we propose a fountain code based on the zigzag decodable code in this paper. Moreover, we analyze the overhead for the received packets, decoding erasure rate, decoding complexity, and asymptotic overhead of the proposed fountain code. As the result, we show that the proposed fountain code outperforms the Raptor codes in terms of the overhead and decoding erasure rate. Simulation results show that the proposed fountain coding system outperforms Raptor coding system in terms of the overhead and the space decoding complexity.</summary>\n    <title>Rateless Coding for Gaussian Channels</title>\n    <summary>A rateless code-i.e., a rate-compatible family of codes-has the property that codewords of the higher rate codes are prefixes of those of the lower rate ones. A perfect family of such codes is one in which each of the codes in the family is capacity-achieving. We show by construction that perfect rateless codes with low-complexity decoding algorithms exist for additive white Gaussian noise channels. Our construction involves the use of layered encoding and successive decoding, together with repetition using time-varying layer weights. As an illustration of our framework, we design a practical three-rate code family. We further construct rich sets of near-perfect rateless codes within our architecture that require either significantly fewer layers or lower complexity than their perfect counterparts. Variations of the basic construction are also developed, including one for time-varying channels in which there is no a priori stochastic model.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:fountain+code+sketch+OR+all:rateless+code+hashing&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [30] ASSISTANT · 2026-07-03 17:54:00 UTC

```
Now let me search for rate-distortion theory applied to hashing or similarity estimation.
```

### [31] TOOL CALL — terminal · 2026-07-03 17:54:00 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:rate-distortion+similarity+estimation+OR+all:rate+distortion+MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [32] TOOL RESULT — terminal · 2026-07-03 17:54:00 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:rate-distortion OR all:similarity OR all:estimation OR all:rate OR all:distortion OR all:MinHash&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>Quantum rate distortion, reverse Shannon theorems, and source-channel separation</title>\n    <summary>We derive quantum counterparts of two key theorems of classical information theory, namely, the rate distortion theorem and the source-channel separation theorem. The rate-distortion theorem gives the ultimate limits on lossy data compression, and the source-channel separation theorem implies that a two-stage protocol consisting of compression and channel coding is optimal for transmitting a memoryless source over a memoryless channel. In spite of their importance in the classical domain, there has been surprisingly little work in these areas for quantum information theory. In the present paper, we prove that the quantum rate distortion function is given in terms of the regularized entanglement of purification. We also determine a single-letter expression for the entanglement-assisted quantum rate distortion function, and we prove that it serves as a lower bound on the unassisted quantum rate distortion function. This implies that the unassisted quantum rate distortion function is non-negative and generally not equal to the coherent information between the source and distorted output (in spite of Barnum's conjecture that the coherent information would be relevant here). Moreover, we prove several quantum source-channel separation theorems. The strongest of these are in the entanglement-assisted setting, in which we establish a necessary and sufficient codition for transmitting a memoryless source over a memoryless quantum channel up to a given distortion.</summary>\n    <title>Semantic Rate-Distortion for Bounded Multi-Agent Communication: Capacity-Derived Semantic Spaces and the Communication Cost of Alignment</title>\n    <summary>When two agents of different computational capacities interact with the same environment, they need not compress a common semantic alphabet differently; they can induce different semantic alphabets altogether. We show that the quotient POMDP $Q_{m,T}(M)$ - the unique coarsest abstraction consistent with an agent's capacity - serves as a capacity-derived semantic space for any bounded agent, and that communication between heterogeneous agents exhibits a sharp structural phase transition. Below a critical rate $R_{\\text{crit}}$ determined by the quotient mismatch, intent-preserving communication is structurally impossible. In the supported one-way memoryless regime, classical side-information coding then yields exponential decay above the induced benchmark. Classical coding theorems tell you the rate once the source alphabet is fixed; our contribution is to derive that alphabet from bounded interaction itself.\n    <title>The physical language of molecular codes: A rate-distortion approach to the evolution and emergence of biological codes</title>\n    <summary>The function of the organism hinges on the performance of its information-processing networks, which convey information via molecular recognition. Many paths within these networks utilize molecular codebooks, such as the genetic code, to translate information written in one class of molecules into another molecular \"language\" . The present paper examines the emergence and evolution of molecular codes in terms of rate-distortion theory and reviews recent results of this approach. We discuss how the biological problem of maximizing the fitness of an organism by optimizing its molecular coding machinery is equivalent to the communication engineering problem of designing an optimal information channel. The fitness of a molecular code takes into account the interplay between the quality of the channel and the cost of resources which the organism needs to invest in its construction and maintenance. We analyze the dynamics of a population of organisms that compete according to the fitness of their codes. The model suggests a generic mechanism for the emergence of molecular codes as a phase transition in an information channel. This mechanism is put into biological context and demonstrated in a simple example.</summary>\n    <title>Estimation of the Rate-Distortion Function</title>\n    <summary>  Motivated by questions in lossy data compression and by theoretical considerations, we examine the problem of estimating the rate-distortion function of an unknown (not necessarily discrete-valued) source from empirical data. Our focus is the behavior of the so-called \"plug-in\" estimator, which is simply the rate-distortion function of the empirical distribution of the observed data. Sufficient conditions are given for its consistency, and examples are provided to demonstrate that in certain cases it fails to converge to the true rate-distortion function. The analysis of its performance is complicated by the fact that the rate-distortion function is not continuous in the source distribution; the underlying mathematical problem is closely related to the classical problem of establishing the consistency of maximum likelihood estimators. General consistency results are given for the plug-in estimator applied to a broad class of sources, including all stationary and ergodic ones. A more general class of estimation problems is also considered, arising in the context of lossy data compression when the allowed class of coding distributions is restricted; analogous results are developed for the plug-in estimator in that case. Finally, consistency theorems are formulated for modified (e.g., penalized) versions of the plug-in, and for estimating the optimal reproduction distribution.</summary>\n    <title>The Quadratic Gaussian Rate-Distortion Function for Source Uncorrelated Distortions</title>\n    <summary>  We characterize the rate-distortion function for zero-mean stationary Gaussian sources under the MSE fidelity criterion and subject to the additional constraint that the distortion is uncorrelated to the input. The solution is given by two equations coupled through a single scalar parameter. This has a structure similar to the well known water-filling solution obtained without the uncorrelated distortion restriction. Our results fully characterize the unique statistics of the optimal distortion. We also show that, for all positive distortions, the minimum achievable rate subject to the uncorrelation constraint is strictly larger than that given by the un-constrained rate-distortion function. This gap increases with the distortion and tends to infinity and zero, respectively, as the distortion tends to zero and infinity.</summary>\n    <title>Rate-Distortion Bounds for an Epsilon-Insensitive Distortion Measure</title>\n    <summary>Direct evaluation of the rate-distortion function has rarely been achieved when it is strictly greater than its Shannon lower bound. In this paper, we consider the rate-distortion function for the distortion measure defined by an epsilon-insensitive loss function. We first present the Shannon lower bound applicable to any source distribution with finite differential entropy. Then, focusing on the Laplacian and Gaussian sources, we prove that the rate-distortion functions of these sources are strictly greater than their Shannon lower bounds and obtain analytically evaluable upper bounds for the rate-distortion functions. Small distortion limit and numerical evaluation of the bounds suggest that the Shannon lower bound provides a good approximation to the rate-distortion function for the epsilon-insensitive distortion measure.</summary>\n    <title>Neural Estimation of the Rate-Distortion Function With Applications to Operational Source Coding</title>\n    <summary>A fundamental question in designing lossy data compression schemes is how well one can do in comparison with the rate-distortion function, which describes the known theoretical limits of lossy compression. Motivated by the empirical success of deep neural network (DNN) compressors on large, real-world data, we investigate methods to estimate the rate-distortion function on such data, which would allow comparison of DNN compressors with optimality. While one could use the empirical distribution of the data and apply the Blahut-Arimoto algorithm, this approach presents several computational challenges and inaccuracies when the datasets are large and high-dimensional, such as the case of modern image datasets. Instead, we re-formulate the rate-distortion objective, and solve the resulting functional optimization problem using neural networks. We apply the resulting rate-distortion estimator, called NERD, on popular image datasets, and provide evidence that NERD can accurately estimate the rate-distortion function. Using our estimate, we show that the rate-distortion achievable by DNN compressors are within several bits of the rate-distortion function for real-world datasets. Additionally, NERD provides access to the rate-distortion achieving channel, as well as samples from its output marginal. Therefore, using recent results in reverse channel coding, we describe how NERD can be used to construct an operational one-shot lossy compression scheme with guarantees on the achievable rate and distortion. Experimental results demonstrate competitive performance with DNN compressors.</summary>\n    <title>Quantum Rate-Distortion Coding</title>\n    <summary>  I introduce rate-distortion theory for quantum coding, and derive a lower bound, involving the coherent information, on the rate at which qubits must be used to encode a quantum source with a given maximum level of distortion per source emission. The convexity of the \"information rate-distortion function\" which defines this bound is also derived.</summary>\n    <title>Minimax Rate-Distortion</title>\n    <summary>We show the existence of variable-rate rate-distortion codes that meet the disortion constraint almost surely and are minimax, i.e., strongly, universal with respect to an unknown source distribution and a distortion measure that is revealed only to the encoder and only at runtime. If we only require minimax universality with respect to the source distribution and not the distortion measure, then we provide an achievable $\\tilde{O}(1/\\sqrt{n})$ redundancy rate, which we show is optimal. This is in contrast to prior work on universal lossy compression, which provides $O(\\log n/n)$ redundancy guarantees for weakly universal codes under various regularity conditions. We show that either eliminating the regularity conditions or upgrading to strong universality while keeping these regularity conditions entails an inevitable increase in the redundancy to $\\tilde{O}(1/\\sqrt{n})$. Our construction involves random coding with non-i.i.d.\\ codewords and a zero-rate uncoded transmission scheme. The proof uses exact asymptotics from large deviations, acceptance-rejection sampling, and the VC dimension of distortion measures.</summary>\n    <title>RDD Function: A Tradeoff Between Rate and Distortion-in-Distortion</title>\n    <summary>In this paper, we propose a novel function named Rate Distortion-in-Distortion (RDD) function as an extension of the classical rate-distortion (RD) function, where the expected distortion constraint is replaced by a Gromov-type distortion. This distortion, integral to the Gromov-Wasserstein (GW) distance, effectively defines the similarity in spaces of possibly different dimensions even without a direct metric between them. While the RDD function qualifies as an informational RD function, encoding theorems substantiate its status as an operational RD function, thereby underscoring its potential applicability in real-world source coding. Due to the high computational complexity associated with Gromov-type distortion, in general, the RDD function cannot be evaluated analytically. Consequently, we develop an alternating mirror descent algorithm that significantly reduces computational complexity by employing decomposition, linearization, and relaxation techniques. Numerical results on classical sources and different grids demonstrate the effectiveness of the developed algorithm. By exploring the relationship between the RDD function and the RD function, we suggest that the RDD function may have potential applications in future scenarios.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:rate-distortion+similarity+estimation+OR+all:rate+distortion+MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [33] THINKING · 2026-07-03 17:54:17 UTC

```
Now I have gathered relevant literature context. Let me synthesize what I've found and write a thorough review.

Key findings from literature search:
1. **MinHash variants**: There are many MinHash variants including b-bit MinHash (Li & König), SetSketch (Ertl), HyperMinHash, C-MinHash, ProbMinHash. The field is quite mature.

2. **Fountain/rateless codes**: These are well-established in coding theory for erasure channels. They generate potentially infinite encoded symbols from a source message. The key property is that the receiver can decode after receiving enough symbols.

3. **Rate-distortion theory**: This is a well-established framework, but I didn't find direct applications to MinHash or Jaccard similarity estimation. This could be a novel contribution.

4. **Adaptive sketching**: I didn't find work that specifically addresses "rateless" or "progressive" MinHash where the sketch size is not fixed upfront.

Now let me think about the hypothesis critically:

**Strengths:**
1. Novel cross-domain combination: Applying fountain codes to MinHash is creative
2. Practical motivation: The problem of not knowing optimal sketch size upfront is real
3. Strong theoretical foundation: Rate-distortion theory could provide principled stopping rules
4. Clear applications: LLM deduplication, streaming data, distributed systems

**Potential issues:**
1. **Fundamental technical challenge**: How exactly do you apply fountain codes to MinHash? MinHash works by applying random permutations to sets and taking minimum values. Fountain codes work by XORing source symbols together. The connection is not obvious. The hypothesis needs to explain this more clearly.

2. **Progressive estimation challenge**: Standard MinHash uses k independent permutations. Each additional hash provides an independent estimate. The problem is that to get a "progressive" estimate, you need the estimates to be correlated in a specific way (monotonically improving). But independent estimates don't naturally give monotonic improvement - you could get a worse estimate with more samples due to variance.

3. **Rate-distortion formulation**: The hypothesis states "Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean squared error." This needs more justification. Rate-distortion theory typically deals with continuous-valued sources and MSE distortion. Jaccard estimation is a discrete problem with a specific estimator (the fraction of matching minima). The RD function for this specific estimation problem is not obvious.

4. **Comparison to baselines**: The hypothesis mentions comparing to SetSketch, b-bit MinHash, etc. But SetSketch already provides a configurable parameter that bridges MinHash and HyperLogLog. How is rateless MinHash fundamentally different from just using a larger SetSketch and reading fewer bytes?

5. **Monotonic improvement**: The assumption that "estimation error decays monotonically as more values are received" is strong. Standard MinHash doesn't guarantee this - adding more hash functions reduces variance but any particular estimate could be worse.

6. **The "lossy compression channel" framing**: Viewing MinHash as a lossy compression channel is interesting but needs more development. What exactly is the "source"? The set? The Jaccard similarities? The compression is the sketch. But fountain codes are typically applied to the source directly, not to an already-compressed representation.

Let me think about whether this is a "fatal flaw" that would waste compute:

The biggest technical challenge is the lack of a clear mechanism for how fountain codes map to MinHash. Without this, the whole hypothesis is vague. The author needs to:
1. Clearly define how fountain code encoding maps to generating hash values from sets
2. Show that the decoding (estimation) process actually benefits from the rateless property
3. Prove or provide intuition for why this gives better space-accuracy trade-offs

This is a major issue that could waste compute if not addressed.

Let me also think about related work more carefully. The hypothesis cites:
- Standard MinHash (Broder et al.)
- b-bit MinHash (Li & Konig)
- SetSketch (Ertl)
- Polar Code Nearest-Neighbor (Touitou & Halabi)
- ProbMinHash (Ertl)
- Odd Sketch (Mitzenmacher et al.)

But I should check if there's work on progressive or adaptive MinHash that's missing. Let me search for that.

Actually, thinking more carefully, the concept of "progressive" estimation is related to the idea of "one-pass" or "streaming" algorithms where you can get estimates at any point. But standard MinHash already has this property - you can compute the Jaccard estimate after any number of hash functions. The issue is that the estimate doesn't necessarily improve monotonically.

Wait, I think I understand the vision better now. The idea might be:
1. Instead of using k independent permutations, use a rateless code to generate an infinite sequence of "coded" hash values
2. These coded values are designed so that receiving the first n values gives an estimate with error that decreases (on average) with n
3. The rate-distortion theory tells you when to stop (when the error is below a threshold)

The key innovation would be in how the coded hash values are generated. They can't just be independent permutations - they need to have some structure from the fountain code.

Actually, I think there might be a fundamental confusion here. Fountain codes are used for erasure channels - you want to transmit k source symbols over a channel where some symbols are lost. The receiver can decode after receiving any k(1+ε) symbols. The "rateless" property is that you can keep sending symbols indefinitely and the receiver can start decoding at any point.

For MinHash, the "source symbols" would be... what exactly? The set elements? The hash values under different permutations? 

I think the hypothesis needs significant clarification on this point. Let me write the review accordingly.

For the review, I should:
1. Praise the novel cross-domain combination
2. Flag the lack of clear technical mechanism as a major issue
3. Question whether the rate-distortion formulation is straightforward
4. Ask for more concrete technical details before experiments
5. Suggest related work that might be missing

Let me also check if there's existing work on "progressive" or "adaptive" MinHash that the hypothesis might have missed. Let me search more specifically.
```

### [34] ASSISTANT · 2026-07-03 17:54:17 UTC

```
Let me search for more specific related work on progressive estimation and adaptive sketching.
```

### [35] TOOL CALL — terminal · 2026-07-03 17:54:17 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=ti:progressive+AND+ti:sketch+OR+ti:adaptive+AND+ti:MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [36] TOOL RESULT — terminal · 2026-07-03 17:54:17 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=ti:progressive AND ti:sketch OR ti:adaptive AND ti:MinHash&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>Stroke of Surprise: Progressive Semantic Illusions in Vector Sketching</title>\n    <summary>Visual illusions traditionally rely on spatial manipulations such as multi-view consistency. In this work, we introduce Progressive Semantic Illusions, a novel vector sketching task where a single sketch undergoes a dramatic semantic transformation through the sequential addition of strokes. We present Stroke of Surprise, a generative framework that optimizes vector strokes to satisfy distinct semantic interpretations at different drawing stages. The core challenge lies in the \"dual-constraint\": initial prefix strokes must form a coherent object (e.g., a duck) while simultaneously serving as the structural foundation for a second concept (e.g., a sheep) upon adding delta strokes. To address this, we propose a sequence-aware joint optimization framework driven by a dual-branch Score Distillation Sampling (SDS) mechanism. Unlike sequential approaches that freeze the initial state, our method dynamically adjusts prefix strokes to discover a \"common structural subspace\" valid for both targets. Furthermore, we introduce a novel Overlay Loss that enforces spatial complementarity, ensuring structural integration rather than occlusion. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines in recognizability and illusion strength, successfully expanding visual anagrams from the spatial to the temporal dimension. Project page: https://stroke-of-surprise.github.io/</summary>\n    <title>CoProSketch: Controllable and Progressive Sketch Generation with Diffusion Model</title>\n    <summary>Sketches serve as fundamental blueprints in artistic creation because sketch editing is easier and more intuitive than pixel-level RGB image editing for painting artists, yet sketch generation remains unexplored despite advancements in generative models. We propose a novel framework CoProSketch, providing prominent controllability and details for sketch generation with diffusion models. A straightforward method is fine-tuning a pretrained image generation diffusion model with binarized sketch images. However, we find that the diffusion models fail to generate clear binary images, which makes the produced sketches chaotic. We thus propose to represent the sketches by unsigned distance field (UDF), which is continuous and can be easily decoded to sketches through a lightweight network. With CoProSketch, users generate a rough sketch from a bounding box and a text prompt. The rough sketch can be manually edited and fed back into the model for iterative refinement and will be decoded to a detailed sketch as the final result. Additionally, we curate the first large-scale text-sketch paired dataset as the training data. Experiments demonstrate superior semantic consistency and controllability over baselines, offering a practical solution for integrating user feedback into generative workflows.</summary>\n    <title>sketch-plot: Progressive Editing for Text-to-Image Academic Figures</title>\n    <summary>Text to image (T2I) models such as gpt-image-2 can now generate publication grade academic figures from a short prompt, but the output is a flat raster: a user who wants to change one arrow, one label, or one icon has to regenerate the whole image, which also disturbs the parts they wanted to keep. We present sketch-plot, an interactive system that closes this controllability gap with a three layer progressive editing pipeline: a generated PNG, an addressable puzzle of editable pieces, and a per piece SVG. The user stops at the layer that gives them enough control for the change at hand, so the cost of decomposition and vectorisation is paid only on the pieces that need it. Realising this pipeline is not trivial. General segmentation models lack the semantic discriminability to decompose a research figure cleanly, and end to end image vectorisation produces incomplete shapes and loses semantic structure. We therefore route both stages through a human in the loop interface that lets the user accept, refine, or reject decomposition and vectorisation decisions on a piece by piece basis. We validate the design with an expert user study, in which participants found sketch-plot effective for making targeted edits to AI generated academic figures and preferred it over regenerating the whole image. A demonstration video is available at https://paper-plot.dev/sketch.</summary>\n    <title>From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution</title>\n    <summary>Diffusion Transformers achieve impressive generative quality but remain computationally expensive due to iterative sampling. Recently, dynamic resolution sampling has emerged as a promising acceleration technique by reducing the resolution of early sampling steps. However, existing methods rely on heuristic re-noising at every resolution transition, injecting noise that breaks cross-stage consistency and forces the model to relearn global structure. In addition, these methods indiscriminately upsample the entire latent space at once without checking which regions have actually converged, causing accumulated errors, and visible artifacts. Therefore, we propose \\textbf{Fresco}, a dynamic resolution framework that unifies re-noise and global structure across stages with progressive upsampling, preserving both the efficiency of low-resolution drafting and the fidelity of high-resolution refinement, with all stages aligned toward the same final target. Fresco achieves near-lossless acceleration across diverse domains and models, including 10$\\times$ speedup on FLUX, and 5$\\times$ on HunyuanVideo, while remaining orthogonal to distillation, quantization and feature caching, reaching 22$\\times$ speedup when combined with distilled models. Our code is in supplementary material and will be released on Github.</summary>\n    <title>Interactive Tumor Progression Modeling via Sketch-Based Image Editing</title>\n    <summary>Accurately visualizing and editing tumor progression in medical imaging is crucial for diagnosis, treatment planning, and clinical communication. To address the challenges of subjectivity and limited precision in existing methods, we propose SkEditTumor, a sketch-based diffusion model for controllable tumor progression editing. By leveraging sketches as structural priors, our method enables precise modifications of tumor regions while maintaining structural integrity and visual realism. We evaluate SkEditTumor on four public datasets - BraTS, LiTS, KiTS, and MSD-Pancreas - covering diverse organs and imaging modalities. Experimental results demonstrate that our method outperforms state-of-the-art baselines, achieving superior image fidelity and segmentation accuracy. Our contributions include a novel integration of sketches with diffusion models for medical image editing, fine-grained control over tumor progression visualization, and extensive validation across multiple datasets, setting a new benchmark in the field.</summary>\n    <title>Synthesis and Edition of Ultrasound Images via Sketch Guided Progressive Growing GANs</title>\n    <summary>Ultrasound (US) is widely accepted in clinic for anatomical structure inspection. However, lacking in resources to practice US scan, novices often struggle to learn the operation skills. Also, in the deep learning era, automated US image analysis is limited by the lack of annotated samples. Efficiently synthesizing realistic, editable and high resolution US images can solve the problems. The task is challenging and previous methods can only partially complete it. In this paper, we devise a new framework for US image synthesis. Particularly, we firstly adopt a sketch generative adversarial networks (Sgan) to introduce background sketch upon object mask in a conditioned generative adversarial network. With enriched sketch cues, Sgan can generate realistic US images with editable and fine-grained structure details. Although effective, Sgan is hard to generate high resolution US images. To achieve this, we further implant the Sgan into a progressive growing scheme (PGSgan). By smoothly growing both generator and discriminator, PGSgan can gradually synthesize US images from low to high resolution. By synthesizing ovary and follicle US images, our extensive perceptual evaluation, user study and segmentation results prove the promising efficacy and efficiency of the proposed PGSgan.</summary>\n    <title>Sketch guided and progressive growing GAN for realistic and editable ultrasound image synthesis</title>\n    <summary>Ultrasound (US) imaging is widely used for anatomical structure inspection in clinical diagnosis. The training of new sonographers and deep learning based algorithms for US image analysis usually requires a large amount of data. However, obtaining and labeling large-scale US imaging data are not easy tasks, especially for diseases with low incidence. Realistic US image synthesis can alleviate this problem to a great extent. In this paper, we propose a generative adversarial network (GAN) based image synthesis framework. Our main contributions include: 1) we present the first work that can synthesize realistic B-mode US images with high-resolution and customized texture editing features; 2) to enhance structural details of generated images, we propose to introduce auxiliary sketch guidance into a conditional GAN. We superpose the edge sketch onto the object mask and use the composite mask as the network input; 3) to generate high-resolution US images, we adopt a progressive training strategy to gradually generate high-resolution images from low-resolution images. In addition, a feature loss is proposed to minimize the difference of high-level features between the generated and real images, which further improves the quality of generated images; 4) the proposed US image synthesis method is quite universal and can also be generalized to the US images of other anatomical structures besides the three ones tested in our study (lung, hip joint, and ovary); 5) extensive experiments on three large US image datasets are conducted to validate our method. Ablation studies, customized texture editing, user studies, and segmentation tests demonstrate promising results of our method in synthesizing realistic US images.</summary>\n    <title>Progressive Domain-Independent Feature Decomposition Network for Zero-Shot Sketch-Based Image Retrieval</title>\n    <summary>Zero-shot sketch-based image retrieval (ZS-SBIR) is a specific cross-modal retrieval task for searching natural images given free-hand sketches under the zero-shot scenario. Most existing methods solve this problem by simultaneously projecting visual features and semantic supervision into a low-dimensional common space for efficient retrieval. However, such low-dimensional projection destroys the completeness of semantic knowledge in original semantic space, so that it is unable to transfer useful knowledge well when learning semantic from different modalities. Moreover, the domain information and semantic information are entangled in visual features, which is not conducive for cross-modal matching since it will hinder the reduction of domain gap between sketch and image. In this paper, we propose a Progressive Domain-independent Feature Decomposition (PDFD) network for ZS-SBIR. Specifically, with the supervision of original semantic knowledge, PDFD decomposes visual features into domain features and semantic ones, and then the semantic features are projected into common space as retrieval features for ZS-SBIR. The progressive projection strategy maintains strong semantic supervision. Besides, to guarantee the retrieval features to capture clean and complete semantic information, the cross-reconstruction loss is introduced to encourage that any combinations of retrieval features and domain features can reconstruct the visual features. Extensive experiments demonstrate the superiority of our PDFD over state-of-the-art competitors.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=ti:progressive+AND+ti:sketch+OR+ti:adaptive+AND+ti:MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [37] ASSISTANT · 2026-07-03 17:54:23 UTC

```
Let me search for the related works mentioned in the hypothesis - particularly the Polar Code Nearest-Neighbor and ProbMinHash papers.
```

### [38] TOOL CALL — terminal · 2026-07-03 17:54:23 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:Polar+Code+Nearest-Neighbor+OR+all:ProbMinHash+OR+all:Odd+Sketch+MinHash&start=0&max_results=10\" | grep -E \"<title>|<id>|<summary>\" | head -80",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [39] TOOL RESULT — terminal · 2026-07-03 17:54:23 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<id>https://arxiv.org/api/HeltTaSbR+zuOWksoCZp2KS3NDE</id>\n  <title>arXiv Query: search_query=all:Polar OR all:Code OR all:Nearest-Neighbor OR all:ProbMinHash OR all:Odd OR all:Sketch OR all:MinHash&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <id>http://arxiv.org/abs/2109.03142v1</id>\n    <title>Polarization measurements of the Crab Pulsar with POLAR</title>\n    <summary>POLAR is a dedicated Gamma-Ray Burst polarimeter making use of Compton-scattering which took data from the second Chinese spacelab, the Tiangong-2 from September 2016 to April 2017. It has a wide Field of View of $\\sim6$ steradians and an effective area of $\\sim400\\ cm^2$ at 300 keV. These features make it one of the most sensitive instruments in its energy range (15-500 keV), and therefore capable of almost continuously monitoring persistent sources such as pulsars. Significant folded pulsation from both PSR B0531+21 (the Crab Pulsar) and PSR B1509-58 has been observed. Observations of the Crab Pulsar with POLAR have previously been used for phase-resolved spectroscopy of the Crab Pulsar to calibrate the instrumental responses of POLAR. In this work, we investigate a polarimetric joint-fitting method for observations of the Crab Pulsar with POLAR. Unlike a GRB observation with POLAR, the observations of the Crab Pulsar are complicated by multiple observational datasets during which the polarization plane rotates as well. So before fitting, we have to correct the modulation curves under different datasets, by taking into account the rotations of the Crab Pulsar's relative position in the detctor's local coordinate, and the changes of detector response in different datasets. Despite these difficulties and the low signal to background for such sources constraining, polarization measurements were possible with the POLAR data. We will present the methodology briefly, which could be applied to any wide FoV polarimeter, and polarization results of the Crab pulsar with POLAR. Finally, the inferred ability of pulsar detection with POLAR-2 (the successor of POLAR) will also be discussed.</summary>\n    <id>http://arxiv.org/abs/1910.07977v1</id>\n    <title>POLAR measurements of the Crab pulsar</title>\n    <summary>POLAR is a Compton polarimeter sensitive in the 50 to 500 keV energy range. The Crab pulsar is a scientific target for POLAR on board the Chinese space laboratory Tiangong-2 (TG-2). With its large Field of View (FoV), POLAR detected significant pulsed signals from the Crab pulsar which is visible by POLAR in about half of observation time. In this work, we present the preliminary results including the pulse profile, timing and polarization measuring method. First, we show the highly significant pulse profile observed by POLAR which is compared to the results of other detectors including Fermi/LAT and INTEGRAL. And the pulse profile as a function of theta incident angle and as a function of channel number, which indicate that POLAR has a good detection performance, have been showed. Second, we find that the timing of the Crab pulses are accurately measured, which provides a unique verification and calibration to the POLAR timing system. Finally, the potential polarization measurement of the Crab pulsar is also discussed.</summary>\n    <id>http://arxiv.org/abs/1911.07940v1</id>\n    <title>Neighborhood Watch: Representation Learning with Local-Margin Triplet Loss and Sampling Strategy for K-Nearest-Neighbor Image Classification</title>\n    <summary>Deep representation learning using triplet network for classification suffers from a lack of theoretical foundation and difficulty in tuning both the network and classifiers for performance. To address the problem, local-margin triplet loss along with local positive and negative mining strategy is proposed with theory on how the strategy integrate nearest-neighbor hyper-parameter with triplet learning to increase subsequent classification performance. Results in experiments with 2 public datasets, MNIST and Cifar-10, and 2 small medical image datasets demonstrate that proposed strategy outperforms end-to-end softmax and typical triplet loss in settings without data augmentation while maintaining utility of transferable feature for related tasks. The method serves as a good performance baseline where end-to-end methods encounter difficulties such as small sample data with limited allowable data augmentation.</summary>\n    <id>http://arxiv.org/abs/1605.06792v3</id>\n    <title>Active Nearest-Neighbor Learning in Metric Spaces</title>\n    <summary>We propose a pool-based non-parametric active learning algorithm for general metric spaces, called MArgin Regularized Metric Active Nearest Neighbor (MARMANN), which outputs a nearest-neighbor classifier. We give prediction error guarantees that depend on the noisy-margin properties of the input sample, and are competitive with those obtained by previously proposed passive learners. We prove that the label complexity of MARMANN is significantly lower than that of any passive learner with similar error guarantees. MARMANN is based on a generalized sample compression scheme, and a new label-efficient active model-selection procedure.</summary>\n    <id>http://arxiv.org/abs/1902.04008v1</id>\n    <title>Magnon excitations in $Cs_2CuAl_4O_8$ - a bond alternating S=1/2 spin chain with next nearest neighbor coupling</title>\n    <summary>A recent density functional theory (DFT) based analysis, complemented with Quantum Monte Carlo calculations revealed a highly spin-frustrating nature of the one-dimensional spin-$\\frac{1}{2}$ compound $Cs_2CuAl_4O_8$ that comprises of unique bond alternations and relatively strong next nearest neighbor interactions. This article gives a brief account on possible magnon excitations that can appear in the ground state of such systems. We find that the spin waves obtained on top of coplanar helical reference states show multiple magnon modes (both acoustic and optical). However, those magnon modes turn out to be stable only in the absence of bond alternations.</summary>\n    <id>http://arxiv.org/abs/2511.16576v1</id>\n    <title>PolyMinHash: Efficient Area-Based MinHashing of Polygons for Approximate Nearest Neighbor Search</title>\n    <summary>Similarity searches are a critical task in data mining. As data sets grow larger, exact nearest neighbor searches quickly become unfeasible, leading to the adoption of approximate nearest neighbor (ANN) searches. ANN has been studied for text data, images, and trajectories. However, there has been little effort to develop ANN systems for polygons in spatial database systems and geographic information systems. We present PolyMinHash, a system for approximate polygon similarity search that adapts MinHashing into a novel 2D polygon-hashing scheme to generate short, similarity-preserving signatures of input polygons. Minhash is generated by counting the number of randomly sampled points needed before the sampled point lands within the polygon's interior area, yielding hash values that preserve area-based Jaccard similarity. We present the tradeoff between search accuracy and runtime of our PolyMinHash system. Our hashing mechanism reduces the number of candidates to be processed in the query refinement phase by up to 98% compared to the number of candidates processed by the brute-force algorithm.</summary>\n    <id>http://arxiv.org/abs/1410.8433v2</id>\n    <title>Binary Polarization Kernels from Code Decompositions</title>\n    <summary>In this paper, code decompositions (a.k.a. code nestings) are used to design binary polarization kernels. The proposed kernels are in general non-linear. They provide a better polarization exponent than the previously known kernels of the same dimensions. In particular, non-linear kernels of dimensions 14, 15, and 16 are constructed and are shown to have optimal asymptotic error-correction performance. The optimality is proved by showing that the exponents of these kernels achieve a new upper bound that is developed in this paper.</summary>\n    <id>http://arxiv.org/abs/1903.02899v2</id>\n    <title>A General Construction and Encoder Implementation of Polar Codes</title>\n    <summary>Similar to existing codes, puncturing and shortening are two general ways to obtain an arbitrary code length and code rate for polar codes. When some of the coded bits are punctured or shortened, it is equivalent to a situation in which the underlying channels of the polar codes are different. Therefore, the quality of bit channels with puncturing or shortening differ from the original qualities, which can greatly affect the construction of polar codes. In this paper, a general construction of polar codes is studied in two aspects: 1) the theoretical foundation of the construction; and 2) the hardware implementation of polar codes encoders. In contrast to the original identical and independent binary-input, memoryless, symmetric (BMS) channels, these underlying BMS channels can be different. For binary erasure channel (BEC) channels, recursive equations can be employed assuming independent BMS channels. For all other channel types, the proposed general construction of polar codes is based on the existing Tal-Vardy's procedure. The symmetric property and the degradation relationship are shown to be preserved under the general setting, rendering the possibility of a modification of Tal-Vardy's procedure. Simulation results clearly show improved error performance with re-ordering using the proposed new procedures. In terms of hardware, a novel pruned folded encoder architecture is proposed which saves the computation for the beginning frozen bits. Implementation results show the pruned encoder achieve 28% throughput improvement.</summary>\n    <id>http://arxiv.org/abs/2411.17673v1</id>\n    <title>SketchAgent: Language-Driven Sequential Sketch Generation</title>\n    <summary>Sketching serves as a versatile tool for externalizing ideas, enabling rapid exploration and visual communication that spans various disciplines. While artificial systems have driven substantial advances in content creation and human-computer interaction, capturing the dynamic and abstract nature of human sketching remains challenging. In this work, we introduce SketchAgent, a language-driven, sequential sketch generation method that enables users to create, modify, and refine sketches through dynamic, conversational interactions. Our approach requires no training or fine-tuning. Instead, we leverage the sequential nature and rich prior knowledge of off-the-shelf multimodal large language models (LLMs). We present an intuitive sketching language, introduced to the model through in-context examples, enabling it to \"draw\" using string-based actions. These are processed into vector graphics and then rendered to create a sketch on a pixel canvas, which can be accessed again for further tasks. By drawing stroke by stroke, our agent captures the evolving, dynamic qualities intrinsic to sketching. We demonstrate that SketchAgent can generate sketches from diverse prompts, engage in dialogue-driven drawing, and collaborate meaningfully with human users.</summary>\n    <id>http://arxiv.org/abs/2306.09274v1</id>\n    <title>Conditional Human Sketch Synthesis with Explicit Abstraction Control</title>\n    <summary>This paper presents a novel free-hand sketch synthesis approach addressing explicit abstraction control in class-conditional and photo-to-sketch synthesis. Abstraction is a vital aspect of sketches, as it defines the fundamental distinction between a sketch and an image. Previous works relied on implicit control to achieve different levels of abstraction, leading to inaccurate control and synthesized sketches deviating from human sketches. To resolve this challenge, we propose two novel abstraction control mechanisms, state embeddings and the stroke token, integrated into a transformer-based latent diffusion model (LDM). These mechanisms explicitly provide the required amount of points or strokes to the model, enabling accurate point-level and stroke-level control in synthesized sketches while preserving recognizability. Outperforming state-of-the-art approaches, our method effectively generates diverse, non-rigid and human-like sketches. The proposed approach enables coherent sketch synthesis and excels in representing human habits with desired abstraction levels, highlighting the potential of sketch synthesis for real-world applications.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:Polar+Code+Nearest-Neighbor+OR+all:ProbMinHash+OR+all:Odd+Sketch+MinHash&start=0&max_results=10\" | grep -E \"<title>|<id>|<summary>\" | head -80", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [40] ASSISTANT · 2026-07-03 17:54:27 UTC

```
Let me now search for the specific papers mentioned in the related work section, particularly the Polar Code Nearest-Neighbor paper by Touitou & Halabi.
```

### [41] TOOL CALL — terminal · 2026-07-03 17:54:27 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=au:Touitou+OR+au:Halabi+AND+ti:polar+AND+ti:LSH&start=0&max_results=5\" | grep -E \"<title>|<summary>|<id>\" | head -40",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [42] TOOL RESULT — terminal · 2026-07-03 17:54:29 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<id>https://arxiv.org/api/3dM+AH68elQ36FBETX19EbZEDHk</id>\n  <title>arXiv Query: search_query=au:Touitou OR au:Halabi AND ti:polar AND ti:LSH&amp;id_list=&amp;start=0&amp;max_results=5</title>\n    <id>http://arxiv.org/abs/2306.05744v1</id>\n    <title>Improved and Deterministic Online Service with Deadlines or Delay</title>\n    <summary>We consider the problem of online service with delay on a general metric space, first presented by Azar, Ganesh, Ge and Panigrahi (STOC 2017). The best known randomized algorithm for this problem, by Azar and Touitou (FOCS 2019), is $O(\\log^2 n)$-competitive, where $n$ is the number of points in the metric space. This is also the best known result for the special case of online service with deadlines, which is of independent interest.\n    <id>http://arxiv.org/abs/2004.07946v1</id>\n    <title>Beyond Tree Embeddings -- a Deterministic Framework for Network Design with Deadlines or Delay</title>\n    <summary>We consider network design problems with deadline or delay. All previous results for these models are based on randomized embedding of the graph into a tree (HST) and then solving the problem on this tree. We show that this is not necessary. In particular, we design a deterministic framework for these problems which is not based on embedding. This enables us to provide deterministic $\\text{poly-log}(n)$-competitive algorithms for Steiner tree, generalized Steiner tree, node weighted Steiner tree, (non-uniform) facility location and directed Steiner tree with deadlines or with delay (where $n$ is the number of nodes). Our deterministic algorithms also give improved guarantees over some previous randomized results. In addition, we show a lower bound of $\\text{poly-log}(n)$ for some of these problems, which implies that our framework is optimal up to the power of the poly-log. Our algorithms and techniques differ significantly from those in all previous considerations of these problems.</summary>\n    <id>http://arxiv.org/abs/2112.11831v1</id>\n    <title>Online Graph Algorithms with Predictions</title>\n    <summary>Online algorithms with predictions is a popular and elegant framework for bypassing pessimistic lower bounds in competitive analysis. In this model, online algorithms are supplied with future predictions, and the goal is for the competitive ratio to smoothly interpolate between the best offline and online bounds as a function of the prediction error. In this paper, we study online graph problems with predictions. Our contributions are the following:\n    <id>http://arxiv.org/abs/1904.07131v1</id>\n    <title>General Framework for Metric Optimization Problems with Delay or with Deadlines</title>\n    <summary>In this paper, we present a framework used to construct and analyze algorithms for online optimization problems with deadlines or with delay over a metric space. Using this framework, we present algorithms for several different problems. We present an $O(D^{2})$-competitive deterministic algorithm for online multilevel aggregation with delay on a tree of depth $D$, an exponential improvement over the $O(D^{4}2^{D})$-competitive algorithm of Bienkowski et al. (ESA '16), where the only previously-known improvement was for the special case of deadlines by Buchbinder et al. (SODA '17). We also present an $O(\\log^{2}n)$-competitive randomized algorithm for online service with delay over any general metric space of $n$ points, improving upon the $O(\\log^{4}n)$-competitive algorithm by Azar et al. (STOC '17). In addition, we present the problem of online facility location with deadlines. In this problem, requests arrive over time in a metric space, and need to be served until their deadlines by facilities that are opened momentarily for some cost. We also consider the problem of facility location with delay, in which the deadlines are replaced with arbitrary delay functions. For those problems, we present $O(\\log^{2}n)$-competitive algorithms, with $n$ the number of points in the metric space. The algorithmic framework we present includes techniques for the design of algorithms as well as techniques for their analysis.</summary>\n    <id>http://arxiv.org/abs/1712.10273v3</id>\n    <title>Improved Online Algorithm for Weighted Flow Time</title>\n    <summary>We discuss one of the most fundamental scheduling problem of processing jobs on a single machine to minimize the weighted flow time (weighted response time). Our main result is a $O(\\log P)$-competitive algorithm, where $P$ is the maximum-to-minimum processing time ratio, improving upon the $O(\\log^{2}P)$-competitive algorithm of Chekuri, Khanna and Zhu (STOC 2001). We also design a $O(\\log D)$-competitive algorithm, where $D$ is the maximum-to-minimum density ratio of jobs. Finally, we show how to combine these results with the result of Bansal and Dhamdhere (SODA 2003) to achieve a $O(\\log(\\min(P,D,W)))$-competitive algorithm (where $W$ is the maximum-to-minimum weight ratio), without knowing $P,D,W$ in advance. As shown by Bansal and Chan (SODA 2009), no constant-competitive algorithm is achievable for this problem.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=au:Touitou+OR+au:Halabi+AND+ti:polar+AND+ti:LSH&start=0&max_results=5\" | grep -E \"<title>|<summary>|<id>\" | head -40", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [43] ASSISTANT · 2026-07-03 17:54:33 UTC

```
Let me search more specifically for the Polar Codes for LSH paper and also understand the current state of MinHash variants better. Let me also look for recent papers on coding theory applied to LSH.
```

### [44] TOOL CALL — terminal · 2026-07-03 17:54:33 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:polar+codes+locality+sensitive+hashing&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [45] TOOL RESULT — terminal · 2026-07-03 17:54:35 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:polar OR all:codes OR all:locality OR all:sensitive OR all:hashing&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>LV Barcoding: locality sensitive hashing-based tool for rapid species identification in DNA barcoding</title>\n    <summary>DNA barcoding has emerged as a cost-effective approach for species identification. However, the scarcity of tools used for searching the booming reference database becomes an obstacle, currently with BLAST as the only practical choice. Here, we propose a program - LV Barcoding - based on both the random hyperplane projection-based locality sensitive hashing method and the composition vector-based VIP Barcoding for fast species identification. The performance of LV Barcoding is assessed on the data release of BOLD. LV Barcoding has higher accuracy than BLAST, and is able to match a single query against ~114,000 reference barcodes within 10 seconds on a desktop computer. This program is available at http://msl.sls.cuhk.edu.hk/vipbarcoding/.</summary>\n    <title>Polarization measurements of the Crab Pulsar with POLAR</title>\n    <summary>POLAR is a dedicated Gamma-Ray Burst polarimeter making use of Compton-scattering which took data from the second Chinese spacelab, the Tiangong-2 from September 2016 to April 2017. It has a wide Field of View of $\\sim6$ steradians and an effective area of $\\sim400\\ cm^2$ at 300 keV. These features make it one of the most sensitive instruments in its energy range (15-500 keV), and therefore capable of almost continuously monitoring persistent sources such as pulsars. Significant folded pulsation from both PSR B0531+21 (the Crab Pulsar) and PSR B1509-58 has been observed. Observations of the Crab Pulsar with POLAR have previously been used for phase-resolved spectroscopy of the Crab Pulsar to calibrate the instrumental responses of POLAR. In this work, we investigate a polarimetric joint-fitting method for observations of the Crab Pulsar with POLAR. Unlike a GRB observation with POLAR, the observations of the Crab Pulsar are complicated by multiple observational datasets during which the polarization plane rotates as well. So before fitting, we have to correct the modulation curves under different datasets, by taking into account the rotations of the Crab Pulsar's relative position in the detctor's local coordinate, and the changes of detector response in different datasets. Despite these difficulties and the low signal to background for such sources constraining, polarization measurements were possible with the POLAR data. We will present the methodology briefly, which could be applied to any wide FoV polarimeter, and polarization results of the Crab pulsar with POLAR. Finally, the inferred ability of pulsar detection with POLAR-2 (the successor of POLAR) will also be discussed.</summary>\n    <title>A General Construction and Encoder Implementation of Polar Codes</title>\n    <summary>Similar to existing codes, puncturing and shortening are two general ways to obtain an arbitrary code length and code rate for polar codes. When some of the coded bits are punctured or shortened, it is equivalent to a situation in which the underlying channels of the polar codes are different. Therefore, the quality of bit channels with puncturing or shortening differ from the original qualities, which can greatly affect the construction of polar codes. In this paper, a general construction of polar codes is studied in two aspects: 1) the theoretical foundation of the construction; and 2) the hardware implementation of polar codes encoders. In contrast to the original identical and independent binary-input, memoryless, symmetric (BMS) channels, these underlying BMS channels can be different. For binary erasure channel (BEC) channels, recursive equations can be employed assuming independent BMS channels. For all other channel types, the proposed general construction of polar codes is based on the existing Tal-Vardy's procedure. The symmetric property and the degradation relationship are shown to be preserved under the general setting, rendering the possibility of a modification of Tal-Vardy's procedure. Simulation results clearly show improved error performance with re-ordering using the proposed new procedures. In terms of hardware, a novel pruned folded encoder architecture is proposed which saves the computation for the beginning frozen bits. Implementation results show the pruned encoder achieve 28% throughput improvement.</summary>\n    <title>POLAR measurements of the Crab pulsar</title>\n    <summary>POLAR is a Compton polarimeter sensitive in the 50 to 500 keV energy range. The Crab pulsar is a scientific target for POLAR on board the Chinese space laboratory Tiangong-2 (TG-2). With its large Field of View (FoV), POLAR detected significant pulsed signals from the Crab pulsar which is visible by POLAR in about half of observation time. In this work, we present the preliminary results including the pulse profile, timing and polarization measuring method. First, we show the highly significant pulse profile observed by POLAR which is compared to the results of other detectors including Fermi/LAT and INTEGRAL. And the pulse profile as a function of theta incident angle and as a function of channel number, which indicate that POLAR has a good detection performance, have been showed. Second, we find that the timing of the Crab pulses are accurately measured, which provides a unique verification and calibration to the POLAR timing system. Finally, the potential polarization measurement of the Crab pulsar is also discussed.</summary>\n    <title>Inexact Simplification of Symbolic Regression Expressions with Locality-sensitive Hashing</title>\n    <summary>Symbolic regression (SR) searches for parametric models that accurately fit a dataset, prioritizing simplicity and interpretability. Despite this secondary objective, studies point out that the models are often overly complex due to redundant operations, introns, and bloat that arise during the iterative process, and can hinder the search with repeated exploration of bloated segments. Applying a fast heuristic algebraic simplification may not fully simplify the expression and exact methods can be infeasible depending on size or complexity of the expressions. We propose a novel agnostic simplification and bloat control for SR employing an efficient memoization with locality-sensitive hashing (LHS). The idea is that expressions and their sub-expressions traversed during the iterative simplification process are stored in a dictionary using LHS, enabling efficient retrieval of similar structures. We iterate through the expression, replacing subtrees with others of same hash if they result in a smaller expression. Empirical results shows that applying this simplification during evolution performs equal or better than without simplification in minimization of error, significantly reducing the number of nonlinear functions. This technique can learn simplification rules that work in general or for a specific problem, and improves convergence while reducing model complexity.</summary>\n    <title>Optimal Puncturing of Polar Codes With a Fixed Information Set</title>\n    <summary>For a given polar code construction, the existing literature on puncturing for polar codes focuses in finding the optimal puncturing pattern, and then re-selecting the information set. This paper devotes itself to find the optimal puncturing pattern when the information set is fixed. Puncturing the coded bits corresponding to the worst quality bit channels, called the worst quality puncturing (WQP), is proposed, which is analyzed to minimize the bit channel quality loss at the punctured positions. Simulation results show that WQP outperforms the best existing puncturing schemes when the information set is fixed.</summary>\n    <title>All the codeword symbols in polar codes have the same SER under the SC decoder</title>\n    <summary>We consider polar codes constructed from the $2\\times 2$ kernel $\\begin{bmatrix}\n    <title>Balanced Locally Repairable Codes</title>\n    <summary>We introduce a family of balanced locally repairable codes (BLRCs) $[n, k, d]$ for arbitrary values of $n$, $k$ and $d$. Similar to other locally repairable codes (LRCs), the presented codes are suitable for applications that require a low repair locality. The novelty that we introduce in our construction is that we relax the strict requirement the repair locality to be a fixed small number $l$, and we allow the repair locality to be either $l$ or $l+1$. This gives us the flexibility to construct BLRCs for arbitrary values of $n$ and $k$ which partially solves the open problem of finding a general construction of LRCs. Additionally, the relaxed locality criteria gives us an opportunity to search for BLRCs that have a low repair locality even when double failures occur. We use metrics such as a storage overhead, an average repair bandwidth, a Mean Time To Data Loss (MTTDL) and an update complexity to compare the performance of BLRCs with existing LRCs.</summary>\n    <title>Optimal Densification for Fast and Accurate Minwise Hashing</title>\n    <summary>Minwise hashing is a fundamental and one of the most successful hashing algorithm in the literature. Recent advances based on the idea of densification~\\cite{Proc:OneHashLSH_ICML14,Proc:Shrivastava_UAI14} have shown that it is possible to compute $k$ minwise hashes, of a vector with $d$ nonzeros, in mere $(d + k)$ computations, a significant improvement over the classical $O(dk)$. These advances have led to an algorithmic improvement in the query complexity of traditional indexing algorithms based on minwise hashing. Unfortunately, the variance of the current densification techniques is unnecessarily high, which leads to significantly poor accuracy compared to vanilla minwise hashing, especially when the data is sparse. In this paper, we provide a novel densification scheme which relies on carefully tailored 2-universal hashes. We show that the proposed scheme is variance-optimal, and without losing the runtime efficiency, it is significantly more accurate than existing densification techniques. As a result, we obtain a significantly efficient hashing scheme which has the same variance and collision probability as minwise hashing. Experimental evaluations on real sparse and high-dimensional datasets validate our claims. We believe that given the significant advantages, our method will replace minwise hashing implementations in practice.</summary>\n    <title>Locality in Index Coding for Large Min-Rank</title>\n    <summary>An index code is said to be locally decodable if each receiver can decode its demand using its side information and by querying only a subset of the transmitted codeword symbols instead of observing the entire codeword. Local decodability can be a beneficial feature in some communication scenarios, such as when the receivers can afford to listen to only a part of the transmissions because of limited availability of power. The locality of an index code is the ratio of the maximum number of codeword symbols queried by a receiver to the message length. In this paper we analyze the optimum locality of linear codes for the family of index coding problems whose min-rank is one less than the number of receivers in the network. We first derive the optimal trade-off between the index coding rate and locality with vector linear coding when the side information graph is a directed cycle. We then provide the optimal trade-off achieved by scalar linear coding for a larger family of problems, viz., problems where the min-rank is only one less than the number of receivers. While the arguments used for achievability are based on known coding techniques, the converse arguments rely on new results on the structure of locally decodable index codes.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:polar+codes+locality+sensitive+hashing&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [46] THINKING · 2026-07-03 17:54:53 UTC

```
Let me now review what I've found and think about the hypothesis more carefully. I need to provide a thorough review of this research hypothesis about "Rateless MinHash".

Key aspects of the hypothesis:
1. It proposes applying fountain code (rateless erasure code) principles to MinHash
2. The goal is to create a rateless MinHash sketch that generates infinite hash values for progressive Jaccard estimation
3. Rate-distortion theory is proposed to determine optimal stopping point

Let me think about the technical feasibility and novelty:

**Novelty concerns:**
- The idea of combining fountain codes with MinHash is interesting but I need to verify if this has been done before
- The hypothesis mentions related work but I should verify the novelty claims
- Rate-distortion theory applied to Jaccard estimation - is this novel?

**Technical concerns:**
1. The fundamental issue: MinHash works by computing minimum hash values under random permutations. How do you make this "rateless"?
   - Fountain codes work by encoding data symbols into an infinite stream of coded symbols
   - MinHash already uses independent hash functions - each hash is already "independent"
   - The key question: what's the "source message" in MinHash that we're encoding with fountain codes?

2. The hypothesis says "generate a potentially infinite sequence of coded hash values from the set elements"
   - But MinHash already generates independent hashes - you can just generate more if needed
   - The novelty claim seems to be about making the hashes "dependent" in a way that allows progressive refinement
   - But this contradicts how MinHash works - independent hashes are what give the unbiased estimate

3. Rate-distortion theory application:
   - The rate-distortion function for Jaccard estimation would depend on the true Jaccard similarity
   - But the true Jaccard similarity is what we're trying to estimate!
   - This seems circular - how do you determine the stopping point without knowing the similarity?

Let me think about what the actual contribution could be:
- Maybe the idea is to use fountain codes to encode the entire set in a way that allows progressive Jaccard estimation?
- But current MinHash already allows progressive estimation - you can always compute more hash functions

Actually, I think I understand the confusion in the hypothesis. Let me think more carefully:

Standard MinHash: Fix k, compute k independent min-hash values, use them to estimate Jaccard.

The problem: You need to fix k upfront without knowing the desired accuracy.

The proposed solution: Make MinHash "rateless" so you can generate hash values on-demand until you reach desired accuracy.

But this is ALREADY possible with standard MinHash! You can just compute more hash functions until the estimate converges.

So what's the actual novel contribution? The hypothesis says:
"generate a potentially infinite sequence of coded hash values from the set elements"

Ah, I think the idea might be:
- Instead of computing independent min-hash values (which requires storing all k values)
- Use fountain code principles to generate a SEQUENCE where earlier values are more "important" and later values provide progressive refinement
- This could be more efficient than just computing independent hashes

But there's still a fundamental issue: MinHash estimates Jaccard by counting matches in the k hash values. If the hash values are dependent (due to fountain coding), then the statistical properties change...

Actually, I think I now see a potential contribution:
- Standard MinHash: k independent hashes, each requiring storage
- Rateless MinHash: Generate hashes in a sequence where you can stop early if similarity is high (fewer hashes needed to confirm high similarity)
- The fountain code structure ensures that the estimate improves monotonically

But this requires careful statistical analysis to ensure unbiasedness and to derive the variance of the estimate.

Let me think about the rate-distortion part:
- Rate = number of hash values (sketch size)
- Distortion = estimation error (MSE)
- The rate-distortion function R(D) tells you the minimum rate needed to achieve distortion D
- For Jaccard estimation, this would depend on the true Jaccard similarity J
- But you don't know J - you're trying to estimate it!

This seems like a fundamental circularity problem...

Unless the idea is:
1. Start with a small sketch
2. Get a preliminary Jaccard estimate
3. Use rate-distortion theory to determine how many MORE hashes are needed to achieve target accuracy
4. Generate more hashes (progressive refinement)

But this is essentially what people already do in practice - compute more hashes until the estimate stabilizes!

I think the hypothesis has some fundamental technical issues that need to be addressed. Let me structure my review accordingly.

Key critiques:
1. **Major methodological issue**: The connection between fountain codes and MinHash is not clearly established. How exactly do fountain codes apply to MinHash? What is the "source message"? How are the coded symbols generated?

2. **Major technical issue**: The rate-distortion theory application seems circular. The rate-distortion function depends on the true Jaccard similarity, which is unknown.

3. **Novelty concerns**: Progressive estimation with MinHash is already possible by computing more hash functions. The novelty over standard MinHash + early stopping needs to be clearly articulated.

4. **Missing details**: The actual algorithm is not described. How exactly are the "coded hash values" generated? What's the decoding process?

Let me now write the review. I should be specific and actionable in my critiques
```

### [47] ASSISTANT · 2026-07-03 17:54:53 UTC

```
Let me now search for one more critical piece - understanding whether there's existing work on progressive or adaptive MinHash, and also look at the fundamental connection between fountain codes and hashing more carefully.
```

### [48] TOOL CALL — terminal · 2026-07-03 17:54:53 UTC

```
{
  "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:One+Permutation+Hashing+OR+all:consistent+weighted+sampling+MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [49] TOOL RESULT — terminal · 2026-07-03 17:54:55 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "<title>arXiv Query: search_query=all:One OR all:Permutation OR all:Hashing OR all:consistent OR all:weighted OR all:sampling OR all:MinHash&amp;id_list=&amp;start=0&amp;max_results=10</title>\n    <title>Differentially Private One Permutation Hashing and Bin-wise Consistent Weighted Sampling</title>\n    <summary>Minwise hashing (MinHash) is a standard algorithm widely used in the industry, for large-scale search and learning applications with the binary (0/1) Jaccard similarity. One common use of MinHash is for processing massive n-gram text representations so that practitioners do not have to materialize the original data (which would be prohibitive). Another popular use of MinHash is for building hash tables to enable sub-linear time approximate near neighbor (ANN) search. MinHash has also been used as a tool for building large-scale machine learning systems. The standard implementation of MinHash requires applying $K$ random permutations. In comparison, the method of one permutation hashing (OPH), is an efficient alternative of MinHash which splits the data vectors into $K$ bins and generates hash values within each bin. OPH is substantially more efficient and also more convenient to use.\n    <title>A Review for Weighted MinHash Algorithms</title>\n    <summary>Data similarity (or distance) computation is a fundamental research topic which underpins many high-level applications based on similarity measures in machine learning and data mining. However, in large-scale real-world scenarios, the exact similarity computation has become daunting due to \"3V\" nature (volume, velocity and variety) of big data. In such cases, the hashing techniques have been verified to efficiently conduct similarity estimation in terms of both theory and practice. Currently, MinHash is a popular technique for efficiently estimating the Jaccard similarity of binary sets and furthermore, weighted MinHash is generalized to estimate the generalized Jaccard similarity of weighted sets. This review focuses on categorizing and discussing the existing works of weighted MinHash algorithms. In this review, we mainly categorize the Weighted MinHash algorithms into quantization-based approaches, \"active index\"-based ones and others, and show the evolution and inherent connection of the weighted MinHash algorithms, from the integer weighted MinHash algorithms to real-valued weighted MinHash ones (particularly the Consistent Weighted Sampling scheme). Also, we have developed a python toolbox for the algorithms, and released it in our github. Based on the toolbox, we experimentally conduct a comprehensive comparative study of the standard MinHash algorithm and the weighted MinHash ones.</summary>\n    <title>C-MinHash: Rigorously Reducing $K$ Permutations to Two</title>\n    <summary>Minwise hashing (MinHash) is an important and practical algorithm for generating random hashes to approximate the Jaccard (resemblance) similarity in massive binary (0/1) data. The basic theory of MinHash requires applying hundreds or even thousands of independent random permutations to each data vector in the dataset, in order to obtain reliable results for (e.g.,) building large-scale learning models or approximate near neighbor search in massive data. In this paper, we propose {\\bf Circulant MinHash (C-MinHash)} and provide the surprising theoretical results that we just need \\textbf{two} independent random permutations. For C-MinHash, we first conduct an initial permutation on the data vector, then we use a second permutation to generate hash values. Basically, the second permutation is re-used $K$ times via circulant shifting to produce $K$ hashes. Unlike classical MinHash, these $K$ hashes are obviously correlated, but we are able to provide rigorous proofs that we still obtain an unbiased estimate of the Jaccard similarity and the theoretical variance is uniformly smaller than that of the classical MinHash with $K$ independent permutations. The theoretical proofs of C-MinHash require some non-trivial efforts. Numerical experiments are conducted to justify the theory and demonstrate the effectiveness of C-MinHash.</summary>\n    <title>C-MinHash: Practically Reducing Two Permutations to Just One</title>\n    <summary>Traditional minwise hashing (MinHash) requires applying $K$ independent permutations to estimate the Jaccard similarity in massive binary (0/1) data, where $K$ can be (e.g.,) 1024 or even larger, depending on applications. The recent work on C-MinHash (Li and Li, 2021) has shown, with rigorous proofs, that only two permutations are needed. An initial permutation is applied to break whatever structures which might exist in the data, and a second permutation is re-used $K$ times to produce $K$ hashes, via a circulant shifting fashion. (Li and Li, 2021) has proved that, perhaps surprisingly, even though the $K$ hashes are correlated, the estimation variance is strictly smaller than the variance of the traditional MinHash.\n    <title>C-OPH: Improving the Accuracy of One Permutation Hashing (OPH) with Circulant Permutations</title>\n    <summary>Minwise hashing (MinHash) is a classical method for efficiently estimating the Jaccrad similarity in massive binary (0/1) data. To generate $K$ hash values for each data vector, the standard theory of MinHash requires $K$ independent permutations. Interestingly, the recent work on \"circulant MinHash\" (C-MinHash) has shown that merely two permutations are needed. The first permutation breaks the structure of the data and the second permutation is re-used $K$ time in a circulant manner. Surprisingly, the estimation accuracy of C-MinHash is proved to be strictly smaller than that of the original MinHash. The more recent work further demonstrates that practically only one permutation is needed. Note that C-MinHash is different from the well-known work on \"One Permutation Hashing (OPH)\" published in NIPS'12. OPH and its variants using different \"densification\" schemes are popular alternatives to the standard MinHash. The densification step is necessary in order to deal with empty bins which exist in One Permutation Hashing.\n    <title>Optimal Densification for Fast and Accurate Minwise Hashing</title>\n    <summary>Minwise hashing is a fundamental and one of the most successful hashing algorithm in the literature. Recent advances based on the idea of densification~\\cite{Proc:OneHashLSH_ICML14,Proc:Shrivastava_UAI14} have shown that it is possible to compute $k$ minwise hashes, of a vector with $d$ nonzeros, in mere $(d + k)$ computations, a significant improvement over the classical $O(dk)$. These advances have led to an algorithmic improvement in the query complexity of traditional indexing algorithms based on minwise hashing. Unfortunately, the variance of the current densification techniques is unnecessarily high, which leads to significantly poor accuracy compared to vanilla minwise hashing, especially when the data is sparse. In this paper, we provide a novel densification scheme which relies on carefully tailored 2-universal hashes. We show that the proposed scheme is variance-optimal, and without losing the runtime efficiency, it is significantly more accurate than existing densification techniques. As a result, we obtain a significantly efficient hashing scheme which has the same variance and collision probability as minwise hashing. Experimental evaluations on real sparse and high-dimensional datasets validate our claims. We believe that given the significant advantages, our method will replace minwise hashing implementations in practice.</summary>\n    <title>Parameterizing Kterm Hashing</title>\n    <summary>Kterm Hashing provides an innovative approach to novelty detection on massive data streams. Previous research focused on maximizing the efficiency of Kterm Hashing and succeeded in scaling First Story Detection to Twitter-size data stream without sacrificing detection accuracy. In this paper, we focus on improving the effectiveness of Kterm Hashing. Traditionally, all kterms are considered as equally important when calculating a document's degree of novelty with respect to the past. We believe that certain kterms are more important than others and hypothesize that uniform kterm weights are sub-optimal for determining novelty in data streams. To validate our hypothesis, we parameterize Kterm Hashing by assigning weights to kterms based on their characteristics. Our experiments apply Kterm Hashing in a First Story Detection setting and reveal that parameterized Kterm Hashing can surpass state-of-the-art detection accuracy and significantly outperform the uniformly weighted approach.</summary>\n    <title>Communication-Efficient (Weighted) Reservoir Sampling from Fully Distributed Data Streams</title>\n    <summary>We consider communication-efficient weighted and unweighted (uniform) random sampling from distributed data streams presented as a sequence of mini-batches of items. This is a natural model for distributed streaming computation, and our goal is to showcase its usefulness. We present and analyze fully distributed, communication-efficient algorithms for both versions of the problem. An experimental evaluation of weighted reservoir sampling on up to 256 nodes (5120 processors) shows good speedups, while theoretical analysis promises further scaling to much larger machines.</summary>\n    <title>One Permutation Hashing for Efficient Search and Learning</title>\n    <summary>Recently, the method of b-bit minwise hashing has been applied to large-scale linear learning and sublinear time near-neighbor search. The major drawback of minwise hashing is the expensive preprocessing cost, as the method requires applying (e.g.,) k=200 to 500 permutations on the data. The testing time can also be expensive if a new data point (e.g., a new document or image) has not been processed, which might be a significant issue in user-facing applications.\n    <title>Right-jumps and pattern avoiding permutations</title>\n    <summary>We study the iteration of the process \"a particle jumps to the right\" in permutations. We prove that the set of permutations obtained in this model after a given number of iterations from the identity is a class of pattern avoiding permutations. We characterize the elements of the basis of this class and we enumerate these \"forbidden minimal patterns\" by giving their bivariate exponential generating function: we achieve this via a catalytic variable, the number of left-to-right maxima. We show that this generating function is a D-finite function satisfying a nice differential equation of order~2. We give some congruence properties for the coefficients of this generating function, and we show that their asymptotics involves a rather unusual algebraic exponent (the golden ratio $(1+\\sqrt 5)/2$) and some unusual closed-form constants. We end by proving a limit law: a forbidden pattern of length $n$ has typically $(\\ln n) /\\sqrt{5}$ left-to-right maxima, with Gaussian fluctuations.</summary>"}], "is_error": false, "command": "curl -s \"https://export.arxiv.org/api/query?search_query=all:One+Permutation+Hashing+OR+all:consistent+weighted+sampling+MinHash&start=0&max_results=10\" | grep -E \"<title>|<summary>\" | head -50", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [50] ASSISTANT · 2026-07-03 17:55:20 UTC

```
Now I have enough context to write a thorough review. Let me analyze the hypothesis against the literature I've found and evaluate its merits. Let me create the review output file.
```

### [51] TOOL CALL — file_editor · 2026-07-03 17:55:20 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"overall_assessment\": \"The hypothesis proposes an intriguing cross-domain connection between fountain codes (rateless erasure codes) and MinHash sketching for Jaccard similarity estimation. The core idea\u2014creating a rateless MinHash that generates hash values on-demand for progressive estimation\u2014addresses a real problem (fixed sketch size requiring upfront decisions). However, the hypothesis has several fundamental methodological issues that must be resolved before experiments can yield meaningful results. Most critically, the connection between fountain codes and MinHash is not clearly established\u2014fountain codes operate on finite alphabets with symbol-level erasures, while MinHash operates on continuous/minimum hash values with estimation error as distortion, not symbol loss. The rate-distortion formulation for Jaccard estimation also lacks a clear mathematical framework. The hypothesis is novel in its cross-domain inspiration but requires substantial theoretical grounding before experimental validation.\",\n  \n  \"strengths\": [\n    \"Addresses a genuine practical problem: fixed sketch size in MinHash requires knowing accuracy requirements upfront, leading to inefficiency.\",\n    \"Cross-domain thinking is creative: applying fountain/rateless code principles to sketching is a novel angle not explored in the literature.\",\n    \"Progressive estimation with adaptive stopping is valuable for streaming, distributed deduplication, and LLM training data scenarios.\",\n    \"Related work section is reasonably comprehensive, citing standard MinHash, b-bit MinHash, SetSketch, and recent variants like HyperMinHash.\",\n    \"The motivation is clear and well-articulated\u2014the problem of not knowing optimal sketch size beforehand is real.\"\n  ],\n  \n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The proposed methodology has fundamental issues: (1) The connection between fountain codes and MinHash is not mathematically established\u2014fountain codes generate redundant symbols for erasure recovery, while MinHash estimates similarities via minimum hash values; these are fundamentally different operations. (2) Rate-distortion theory application to Jaccard estimation lacks a clear source distribution and distortion measure formulation. (3) The assumption that hash values can be generated as a sequence where error decays monotonically needs proof\u2014correlated hash values from fountain coding may not provide independent estimates.\",\n      \"improvements\": [\n        \"Clarify the mathematical connection: How exactly does fountain coding apply to generating MinHash values? Fountain codes encode finite symbols; MinHash uses minimum over permutations. Propose a concrete encoding scheme (e.g., treat set elements as source symbols, encode using LT/Raptor, then define how to extract Jaccard estimates from received symbols).\",\n        \"Formulate the rate-distortion problem precisely: Define the source (pair of sets?), the rate (bits in sketch), the distortion measure (MSE on Jaccard estimate?), and derive or bound the rate-distortion function. Currently this is asserted but not developed.\",\n        \"Address the independence assumption: Standard MinHash uses independent permutations to get independent estimates. Fountain-coded hashes will be dependent by construction. Provide theoretical analysis of how this dependence affects estimation variance and bias.\",\n        \"Expected score impact: These are major issues\u2014fixing them could raise soundness from 2 to 3 or 4.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The hypothesis is clearly written with good motivation and a reasonable related work section. The connection to fountain codes and rate-distortion theory is described at a high level but lacks concrete technical details that would allow an expert to evaluate feasibility. The investigation approach is outlined but is quite abstract.\",\n      \"improvements\": [\n        \"Provide a concrete algorithmic sketch: Give a pseudo-code or mathematical description of how the rateless MinHash would work. How are set elements encoded? How are hash values generated sequentially? How is Jaccard estimated from a prefix of the sequence?\",\n        \"Define notation precisely: What is the 'sequence of hash values'? Are these minimum values under different permutations? Or something else? How does fountain coding enter the picture?\",\n        \"Add a feasibility analysis: What is the computational complexity of generating and decoding these rateless sketches? How does it compare to standard MinHash?\",\n        \"Expected score impact: Minor to moderate improvement\u2014better presentation alone won't fix fundamental soundness issues, but it would make the work more reviewable (3\u21923.5).\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"If the approach works, the contribution would be significant: a truly adaptive MinHash that doesn't require fixing sketch size upfront would be valuable for many applications (deduplication, streaming, distributed systems). The cross-domain connection to coding theory could open new research directions. However, the contribution is currently speculative\u2014the hypothesis has not demonstrated that the fountain code approach actually provides benefits over simpler adaptive approaches (e.g., just generating more standard MinHash values on-demand).\",\n      \"improvements\": [\n        \"Compare against simpler baselines: Why use fountain codes specifically? Could one achieve progressive estimation simply by generating standard MinHash values incrementally (since they're independent)? The hypothesis should justify why fountain coding is necessary or beneficial vs. simpler approaches.\",\n        \"Quantify the expected benefit: Provide theoretical or preliminary empirical evidence that rateless MinHash achieves better space-accuracy trade-offs. E.g., derive the expected sketch size for a target accuracy and compare to fixed-size MinHash bounds.\",\n        \"Address practical concerns: Can the rateless MinHash support set operations (union, intersection) like standard MinHash? This is important for many applications. Fountain codes may not preserve these properties.\",\n        \"Expected score impact: Addressing these could raise contribution score from 3 to 4 if the approach is shown to be both novel and practically beneficial.\"\n      ]\n    }\n  ],\n  \n  \"critiques\": [\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The connection between fountain codes and MinHash is not mathematically established. Fountain codes (LT, Raptor) are designed for erasure recovery: given k source symbols, they generate an infinite sequence of coded symbols such that any k'(1+\u03b5) symbols can recover the original k symbols. MinHash, conversely, estimates Jaccard similarity by computing minimum hash values under random permutations. The hypothesis asserts these can be connected but doesn't explain how. Key unanswered questions: (1) What are the 'source symbols' for the fountain code? (2) How does one recover Jaccard similarity from fountain-coded symbols? (3) What is the equivalent of 'erasure' in the MinHash context?\",\n      \"suggested_action\": \"Provide a concrete technical proposal for how fountain coding would be applied. One possible approach: Treat each set element as a source symbol. Use fountain coding to generate a stream of coded symbols. Define the MinHash estimate from the first k coded symbols as the minimum over some function of these symbols. Analyze the statistical properties of this estimate. Alternatively, reconsider whether fountain codes are the right analogy\u2014perhaps the real insight is 'progressive refining estimates' which could be achieved more directly.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"Rate-distortion theory application is not formulated. The hypothesis states 'Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean squared error' but doesn't develop this framework. Rate-distortion theory requires: (1) A source distribution P(A,B) over pairs of sets, (2) An encoding function mapping sets to sketches, (3) A decoding function mapping sketches to Jaccard estimates, (4) A distortion measure D(J_true, J_estimated). None of these are defined. Furthermore, the rate-distortion function R(D) characterizes the fundamental limit\u2014but the hypothesis aims to design a practical algorithm, not just bound performance.\",\n      \"suggested_action\": \"Formulate the rate-distortion problem explicitly: Define the source distribution, the encoding/decoding functions, and the distortion measure. Derive (or cite) the rate-distortion function for Jaccard estimation. Alternatively, if the goal is practical algorithm design rather than fundamental limits, reframe the contribution as 'designing an adaptive MinHash with near-optimal space-accuracy trade-off' and use the rate-distortion function as an evaluation benchmark.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"major\",\n      \"description\": \"The hypothesis may be incremental over existing work on adaptive sketching. The related work cites SetSketch, b-bit MinHash, HyperMinHash\u2014all of which address space-accuracy trade-offs for MinHash. The key differentiation claimed is 'adaptive sketch size' vs 'fixed at creation time.' However, one could achieve adaptive estimation simply by computing additional standard MinHash values on-demand (since each MinHash value provides an independent estimate). The hypothesis should clarify what fountain codes add beyond 'generate more hashes as needed.' If the answer is 'nothing,' then the contribution is incremental. If fountain codes provide coding gain (better estimates per bit), this should be demonstrated.\",\n      \"suggested_action\": \"Compare against the naive adaptive baseline: Generate k standard MinHash values, estimate Jaccard, compute confidence interval, generate more if needed. Why is this insufficient? What do fountain codes provide that independence doesn't? Possible answers: (1) Fountain-coded hashes may have lower variance through careful dependence design, (2) The rate-distortion framework provides optimal stopping rules, (3) The approach enables progressive estimation in distributed settings where communication is expensive. Articulate and demonstrate the advantage.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The assumption that 'estimation error decays monotonically as more hash values are received' needs proof. For standard MinHash with independent permutations, the estimation variance decays as 1/k where k is the number of hashes\u2014this is monotonic in expectation but not necessarily monotonic for any particular pair of sets. For fountain-coded hashes, the dependence structure may cause non-monotonic behavior: early symbols may provide little information, then later symbols may dramatically improve estimates. The hypothesis should analyze the learning curve theoretically.\",\n      \"suggested_action\": \"Provide theoretical analysis of the estimation error as a function of the number of hash values. For standard MinHash, Var[J_hat] = J(1-J)/k. What is Var[J_hat] for the proposed rateless MinHash? Does it decay monotonically? At what rate? If the rate is slower than 1/k, the approach may be worse than standard MinHash despite being adaptive.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The investigation approach is ambitious but may be too broad. Formalizing MinHash as rate-distortion, designing a fountain-code-inspired scheme, deriving optimal stopping rules, and implementing/evaluating on LLM deduplication benchmarks is a lot for one paper. The hypothesis could benefit from a more focused contribution: either (1) the theoretical rate-distortion formulation, or (2) the rateless MinHash algorithm design, or (3) the application to LLM deduplication. Trying to do all three may result in superficial treatment of each.\",\n      \"suggested_action\": \"Consider narrowing the scope: Focus on the core theoretical contribution (rateless MinHash design and analysis) with evaluation on standard datasets. Or focus on the application (LLM deduplication) with the rateless MinHash as a practical tool. A narrowed scope would allow deeper treatment and higher confidence in results.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The hypothesis uses terminology from coding theory ('rateless,' 'fountain codes,' 'rate-distortion') without precisely defining how these map to the MinHash context. For example, 'rateless' in fountain codes means 'can generate arbitrary many encoded symbols'\u2014in the MinHash context, this could mean 'can generate arbitrary many hash values,' but then standard MinHash is already 'rateless' in this sense (just generate more permutations). The specific value of fountain codes is unclear.\",\n      \"suggested_action\": \"Define terminology precisely in the context of the problem. Explain: (1) What makes the proposed MinHash 'rateless' beyond just generating more hashes? (2) How exactly are fountain code principles applied? (3) What is the 'rate' and 'distortion' in the rate-distortion formulation? A reader familiar with either coding theory or MinHash (but not both) should be able to understand the connection.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The hypothesis would be stronger with preliminary evidence or a concrete example. Even a small-scale simulation showing that fountain-coded MinHash provides progressive estimates with favorable space-accuracy trade-offs would substantially increase confidence. Currently, the hypothesis is purely conceptual without any proof-of-concept.\",\n      \"suggested_action\": \"Add a proof-of-concept experiment: Implement a simple version of rateless MinHash (even if not fully optimized) and compare against standard MinHash on a small dataset. Show that (1) estimates improve with more hash values, (2) the space-accuracy trade-off is favorable. This could be included as a preliminary result or a cited technical report.\"\n    }\n  ],\n  \n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": null,\n  \"relation_rationale\": \"\"\n}",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [52] TOOL RESULT — file_editor · 2026-07-03 17:55:20 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json", "prev_exist": false, "old_content": null, "new_content": "{\n  \"overall_assessment\": \"The hypothesis proposes an intriguing cross-domain connection between fountain codes (rateless erasure codes) and MinHash sketching for Jaccard similarity estimation. The core idea\u2014creating a rateless MinHash that generates hash values on-demand for progressive estimation\u2014addresses a real problem (fixed sketch size requiring upfront decisions). However, the hypothesis has several fundamental methodological issues that must be resolved before experiments can yield meaningful results. Most critically, the connection between fountain codes and MinHash is not clearly established\u2014fountain codes operate on finite alphabets with symbol-level erasures, while MinHash operates on continuous/minimum hash values with estimation error as distortion, not symbol loss. The rate-distortion formulation for Jaccard estimation also lacks a clear mathematical framework. The hypothesis is novel in its cross-domain inspiration but requires substantial theoretical grounding before experimental validation.\",\n  \n  \"strengths\": [\n    \"Addresses a genuine practical problem: fixed sketch size in MinHash requires knowing accuracy requirements upfront, leading to inefficiency.\",\n    \"Cross-domain thinking is creative: applying fountain/rateless code principles to sketching is a novel angle not explored in the literature.\",\n    \"Progressive estimation with adaptive stopping is valuable for streaming, distributed deduplication, and LLM training data scenarios.\",\n    \"Related work section is reasonably comprehensive, citing standard MinHash, b-bit MinHash, SetSketch, and recent variants like HyperMinHash.\",\n    \"The motivation is clear and well-articulated\u2014the problem of not knowing optimal sketch size beforehand is real.\"\n  ],\n  \n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The proposed methodology has fundamental issues: (1) The connection between fountain codes and MinHash is not mathematically established\u2014fountain codes generate redundant symbols for erasure recovery, while MinHash estimates similarities via minimum hash values; these are fundamentally different operations. (2) Rate-distortion theory application to Jaccard estimation lacks a clear source distribution and distortion measure formulation. (3) The assumption that hash values can be generated as a sequence where error decays monotonically needs proof\u2014correlated hash values from fountain coding may not provide independent estimates.\",\n      \"improvements\": [\n        \"Clarify the mathematical connection: How exactly does fountain coding apply to generating MinHash values? Fountain codes encode finite symbols; MinHash uses minimum over permutations. Propose a concrete encoding scheme (e.g., treat set elements as source symbols, encode using LT/Raptor, then define how to extract Jaccard estimates from received symbols).\",\n        \"Formulate the rate-distortion problem precisely: Define the source (pair of sets?), the rate (bits in sketch), the distortion measure (MSE on Jaccard estimate?), and derive or bound the rate-distortion function. Currently this is asserted but not developed.\",\n        \"Address the independence assumption: Standard MinHash uses independent permutations to get independent estimates. Fountain-coded hashes will be dependent by construction. Provide theoretical analysis of how this dependence affects estimation variance and bias.\",\n        \"Expected score impact: These are major issues\u2014fixing them could raise soundness from 2 to 3 or 4.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The hypothesis is clearly written with good motivation and a reasonable related work section. The connection to fountain codes and rate-distortion theory is described at a high level but lacks concrete technical details that would allow an expert to evaluate feasibility. The investigation approach is outlined but is quite abstract.\",\n      \"improvements\": [\n        \"Provide a concrete algorithmic sketch: Give a pseudo-code or mathematical description of how the rateless MinHash would work. How are set elements encoded? How are hash values generated sequentially? How is Jaccard estimated from a prefix of the sequence?\",\n        \"Define notation precisely: What is the 'sequence of hash values'? Are these minimum values under different permutations? Or something else? How does fountain coding enter the picture?\",\n        \"Add a feasibility analysis: What is the computational complexity of generating and decoding these rateless sketches? How does it compare to standard MinHash?\",\n        \"Expected score impact: Minor to moderate improvement\u2014better presentation alone won't fix fundamental soundness issues, but it would make the work more reviewable (3\u21923.5).\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"If the approach works, the contribution would be significant: a truly adaptive MinHash that doesn't require fixing sketch size upfront would be valuable for many applications (deduplication, streaming, distributed systems). The cross-domain connection to coding theory could open new research directions. However, the contribution is currently speculative\u2014the hypothesis has not demonstrated that the fountain code approach actually provides benefits over simpler adaptive approaches (e.g., just generating more standard MinHash values on-demand).\",\n      \"improvements\": [\n        \"Compare against simpler baselines: Why use fountain codes specifically? Could one achieve progressive estimation simply by generating standard MinHash values incrementally (since they're independent)? The hypothesis should justify why fountain coding is necessary or beneficial vs. simpler approaches.\",\n        \"Quantify the expected benefit: Provide theoretical or preliminary empirical evidence that rateless MinHash achieves better space-accuracy trade-offs. E.g., derive the expected sketch size for a target accuracy and compare to fixed-size MinHash bounds.\",\n        \"Address practical concerns: Can the rateless MinHash support set operations (union, intersection) like standard MinHash? This is important for many applications. Fountain codes may not preserve these properties.\",\n        \"Expected score impact: Addressing these could raise contribution score from 3 to 4 if the approach is shown to be both novel and practically beneficial.\"\n      ]\n    }\n  ],\n  \n  \"critiques\": [\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The connection between fountain codes and MinHash is not mathematically established. Fountain codes (LT, Raptor) are designed for erasure recovery: given k source symbols, they generate an infinite sequence of coded symbols such that any k'(1+\u03b5) symbols can recover the original k symbols. MinHash, conversely, estimates Jaccard similarity by computing minimum hash values under random permutations. The hypothesis asserts these can be connected but doesn't explain how. Key unanswered questions: (1) What are the 'source symbols' for the fountain code? (2) How does one recover Jaccard similarity from fountain-coded symbols? (3) What is the equivalent of 'erasure' in the MinHash context?\",\n      \"suggested_action\": \"Provide a concrete technical proposal for how fountain coding would be applied. One possible approach: Treat each set element as a source symbol. Use fountain coding to generate a stream of coded symbols. Define the MinHash estimate from the first k coded symbols as the minimum over some function of these symbols. Analyze the statistical properties of this estimate. Alternatively, reconsider whether fountain codes are the right analogy\u2014perhaps the real insight is 'progressive refining estimates' which could be achieved more directly.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"Rate-distortion theory application is not formulated. The hypothesis states 'Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean squared error' but doesn't develop this framework. Rate-distortion theory requires: (1) A source distribution P(A,B) over pairs of sets, (2) An encoding function mapping sets to sketches, (3) A decoding function mapping sketches to Jaccard estimates, (4) A distortion measure D(J_true, J_estimated). None of these are defined. Furthermore, the rate-distortion function R(D) characterizes the fundamental limit\u2014but the hypothesis aims to design a practical algorithm, not just bound performance.\",\n      \"suggested_action\": \"Formulate the rate-distortion problem explicitly: Define the source distribution, the encoding/decoding functions, and the distortion measure. Derive (or cite) the rate-distortion function for Jaccard estimation. Alternatively, if the goal is practical algorithm design rather than fundamental limits, reframe the contribution as 'designing an adaptive MinHash with near-optimal space-accuracy trade-off' and use the rate-distortion function as an evaluation benchmark.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"major\",\n      \"description\": \"The hypothesis may be incremental over existing work on adaptive sketching. The related work cites SetSketch, b-bit MinHash, HyperMinHash\u2014all of which address space-accuracy trade-offs for MinHash. The key differentiation claimed is 'adaptive sketch size' vs 'fixed at creation time.' However, one could achieve adaptive estimation simply by computing additional standard MinHash values on-demand (since each MinHash value provides an independent estimate). The hypothesis should clarify what fountain codes add beyond 'generate more hashes as needed.' If the answer is 'nothing,' then the contribution is incremental. If fountain codes provide coding gain (better estimates per bit), this should be demonstrated.\",\n      \"suggested_action\": \"Compare against the naive adaptive baseline: Generate k standard MinHash values, estimate Jaccard, compute confidence interval, generate more if needed. Why is this insufficient? What do fountain codes provide that independence doesn't? Possible answers: (1) Fountain-coded hashes may have lower variance through careful dependence design, (2) The rate-distortion framework provides optimal stopping rules, (3) The approach enables progressive estimation in distributed settings where communication is expensive. Articulate and demonstrate the advantage.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The assumption that 'estimation error decays monotonically as more hash values are received' needs proof. For standard MinHash with independent permutations, the estimation variance decays as 1/k where k is the number of hashes\u2014this is monotonic in expectation but not necessarily monotonic for any particular pair of sets. For fountain-coded hashes, the dependence structure may cause non-monotonic behavior: early symbols may provide little information, then later symbols may dramatically improve estimates. The hypothesis should analyze the learning curve theoretically.\",\n      \"suggested_action\": \"Provide theoretical analysis of the estimation error as a function of the number of hash values. For standard MinHash, Var[J_hat] = J(1-J)/k. What is Var[J_hat] for the proposed rateless MinHash? Does it decay monotonically? At what rate? If the rate is slower than 1/k, the approach may be worse than standard MinHash despite being adaptive.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The investigation approach is ambitious but may be too broad. Formalizing MinHash as rate-distortion, designing a fountain-code-inspired scheme, deriving optimal stopping rules, and implementing/evaluating on LLM deduplication benchmarks is a lot for one paper. The hypothesis could benefit from a more focused contribution: either (1) the theoretical rate-distortion formulation, or (2) the rateless MinHash algorithm design, or (3) the application to LLM deduplication. Trying to do all three may result in superficial treatment of each.\",\n      \"suggested_action\": \"Consider narrowing the scope: Focus on the core theoretical contribution (rateless MinHash design and analysis) with evaluation on standard datasets. Or focus on the application (LLM deduplication) with the rateless MinHash as a practical tool. A narrowed scope would allow deeper treatment and higher confidence in results.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The hypothesis uses terminology from coding theory ('rateless,' 'fountain codes,' 'rate-distortion') without precisely defining how these map to the MinHash context. For example, 'rateless' in fountain codes means 'can generate arbitrary many encoded symbols'\u2014in the MinHash context, this could mean 'can generate arbitrary many hash values,' but then standard MinHash is already 'rateless' in this sense (just generate more permutations). The specific value of fountain codes is unclear.\",\n      \"suggested_action\": \"Define terminology precisely in the context of the problem. Explain: (1) What makes the proposed MinHash 'rateless' beyond just generating more hashes? (2) How exactly are fountain code principles applied? (3) What is the 'rate' and 'distortion' in the rate-distortion formulation? A reader familiar with either coding theory or MinHash (but not both) should be able to understand the connection.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"minor\",\n      \"description\": \"The hypothesis would be stronger with preliminary evidence or a concrete example. Even a small-scale simulation showing that fountain-coded MinHash provides progressive estimates with favorable space-accuracy trade-offs would substantially increase confidence. Currently, the hypothesis is purely conceptual without any proof-of-concept.\",\n      \"suggested_action\": \"Add a proof-of-concept experiment: Implement a simple version of rateless MinHash (even if not fully optimized) and compare against standard MinHash on a small dataset. Show that (1) estimates improve with more hash values, (2) the space-accuracy trade-off is favorable. This could be included as a preliminary result or a cited technical report.\"\n    }\n  ],\n  \n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": null,\n  \"relation_rationale\": \"\"\n}", "kind": "FileEditorObservation"}
```

### [53] THINKING · 2026-07-03 17:55:28 UTC

```
The user has asked me to provide a thorough peer review of the research hypothesis. I've done my research by searching for related work on MinHash, fountain codes, rate-distortion theory, and related topics. I've created a structured review output file.

Let me now verify the output file was created correctly and review its contents to ensure it meets the requirements.

Looking at my review, I need to make sure I've:
1. Grounded the review in evidence (I searched for related work on MinHash variants, fountain codes, rate-distortion theory)
2. Written a review with clear critiques categorized by methodology, evidence, novelty, clarity, scope, or rigor
3. Rated severity as major or minor
4. Provided concrete actionable suggestions
5. Focused on the most impactful issues
6. Provided the output in the required JSON schema format

Let me review the JSON file I created to ensure it's valid and complete. The file path is:
`/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json`

I should verify the JSON is valid and properly structured. Let me also think about whether I've missed any critical issues.

Key issues I identified:
1. **Major methodological issue**: The connection between fountain codes and MinHash is not mathematically established. Fountain codes work on finite alphabets with erasures; MinHash works on continuous values with estimation error. How exactly does one apply fountain coding to generate MinHash values?

2. **Major methodological issue**: Rate-distortion formulation is not developed. What is the source distribution? What is the distortion measure? How is R(D) derived or bounded?

3. **Major novelty issue**: The hypothesis may be incremental. 

Standard MinHash already allows progressive estimation by generating additional independent hash values. The key question is: why use fountain codes? The contribution needs to articulate a clear advantage over simply computing more standard MinHash values on-demand.

4. **Major rigor issue**: The monotonic error decay assumption requires proof, especially given the dependent nature of fountain-coded hashes versus independent permutations in standard MinHash.

I should verify the JSON file and ensure it's complete. Let me also consider if my review is fair and grounded. I searched for related work and found:
- MinHash variants: b-bit MinHash, SetSketch, HyperMinHash, C-MinHash, One Permutation Hashing
- Fountain codes: LT codes, Raptor codes, rateless coding theory
- Rate-distortion: Theory and applications, but not specifically applied to Jaccard estimation

I didn't find any existing work connecting fountain codes to MinHash, which suggests the hypothesis is novel in that regard. However, the connection is not clearly established, which is my main critique.

I believe my review is thorough and fair. The score of 5 (Borderline Accept) reflects that the hypothesis is technically solid in motivation but has major methodological issues that need resolution. The confidence of 4 reflects that I'm familiar with MinHash and sketching algorithms, and I searched for related work, but I'm not an expert in fountain codes.

Let me verify the JSON file is valid
```

### [54] ASSISTANT · 2026-07-03 17:55:28 UTC

```
Let me verify the JSON file I created is valid and properly formatted.
```

### [55] TOOL CALL — terminal · 2026-07-03 17:55:28 UTC

```
{
  "command": "python3 -c \"import json; f=open('/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json'); d=json.load(f); print('Valid JSON'); print('Score:', d['score']); print('Confidence:', d['confidence']); print('Num critiques:', len(d['critiques'])); print('Num strengths:', len(d['strengths']))\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [56] TOOL RESULT — terminal · 2026-07-03 17:55:30 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Valid JSON\nScore: 5\nConfidence: 4\nNum critiques: 7\nNum strengths: 5"}], "is_error": false, "command": "python3 -c \"import json; f=open('/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json'); d=json.load(f); print('Valid JSON'); print('Score:', d['score']); print('Confidence:', d['confidence']); print('Num critiques:', len(d['critiques'])); print('Num strengths:', len(d['strengths']))\"", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "bd2a8b13bd93", "working_dir": "/ai-inventor/.claude/skills/aii-web-research-tools", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/.oh_sessions/c8ed38296a9648fbab19904e4a806a05/observations", "kind": "TerminalObservation"}
```

### [57] THINKING · 2026-07-03 17:55:38 UTC

```
Let me review what I've done and check if my review is comprehensive and fair. The user asked me to review a hypothesis about "Rateless MinHash" which combines fountain codes with MinHash for progressive Jaccard similarity estimation.

Let me think about whether my review adequately covers the key issues:

1. **Main concern**: The hypothesis proposes using fountain codes (rateless erasure codes) for MinHash, but the connection is not mathematically established. Fountain codes work on finite alphabets with symbol erasures, while MinHash works with minimum hash values. This is a fundamental methodological issue.

2. **Rate-distortion formulation**: The hypothesis mentions using rate-distortion theory but doesn't formulate the problem precisely. This is another major issue.

3. **Novelty concerns**: The hypothesis needs to justify why fountain codes are necessary vs. simply generating more MinHash values on-demand.

4. **Monotonic error decay**: The assumption that error decays monotonically needs proof.

5. **Scope**: The investigation approach is quite broad and might be too ambitious.

Looking at my review:
- I gave an overall score of 5 (Borderline Accept)
- Confidence of 4 (Confident but not absolutely certain)
- Soundness: 2 (fair/poor) - I think this is appropriate given the major methodological issues
- Presentation: 3 (good) - The hypothesis is clearly written but lacks technical details
- Contribution: 3 (good) - If it works, it would be significant, but currently speculative

The critiques I provided are:
1. Major: Connection between fountain codes and MinHash not established
2. Major: Rate-distortion theory not formulated
3. Major: Novelty concerns vs. existing adaptive approaches
4. Major: Monotonic error decay needs proof
5. Minor: Scope too broad
6. Minor: Terminology not precisely defined
7. Minor: Lack of preliminary evidence

I think the review is thorough and fair. The score of 5 (Borderline Accept) reflects that:
- The idea is creative and addresses a real problem
- But there are major methodological issues that need to be resolved
- With revisions, this could become a solid contribution

Let me also verify that I've done proper literature review. 

I searched for:
- MinHash variants (SetSketch, b-bit MinHash, HyperMinHash, C-MinHash, One Permutation Hashing)
- Fountain codes and rateless codes
- Rate-distortion theory applied to similarity estimation
- Polar codes for LSH (mentioned in related work)

I found relevant prior work and contextualized the hypothesis against it. The related work section in the hypothesis itself is decent, citing standard works. My review pushes back on the technical connection.

One thing I might have missed: I should check if there's existing work on "progressive" or "adaptive" MinHash that the hypothesis should compare against. Let me think... The hypothesis mentions that existing approaches require fixing sketch size upfront. But actually, one could just generate MinHash values incrementally - this is a simple baseline that the hypothesis should address.

I believe my review adequately captures this concern in the "novelty" critique.

Overall, I believe the review is thorough, fair, and actionable. The score of 5 is appropriate for a hypothesis with creative ideas but major technical gaps that need to be addressed before experimentation
```

### [58] ASSISTANT · 2026-07-03 17:55:38 UTC

```
Let me verify the content of the review file to ensure it's complete and properly formatted.
```

### [59] TOOL CALL — file_editor · 2026-07-03 17:55:38 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [60] TOOL RESULT — file_editor · 2026-07-03 17:55:38 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json:\n     1\t{\n     2\t  \"overall_assessment\": \"The hypothesis proposes an intriguing cross-domain connection between fountain codes (rateless erasure codes) and MinHash sketching for Jaccard similarity estimation. The core idea\u2014creating a rateless MinHash that generates hash values on-demand for progressive estimation\u2014addresses a real problem (fixed sketch size requiring upfront decisions). However, the hypothesis has several fundamental methodological issues that must be resolved before experiments can yield meaningful results. Most critically, the connection between fountain codes and MinHash is not clearly established\u2014fountain codes operate on finite alphabets with symbol-level erasures, while MinHash operates on continuous/minimum hash values with estimation error as distortion, not symbol loss. The rate-distortion formulation for Jaccard estimation also lacks a clear mathematical framework. The hypothesis is novel in its cross-domain inspiration but requires substantial theoretical grounding before experimental validation.\",\n     3\t  \n     4\t  \"strengths\": [\n     5\t    \"Addresses a genuine practical problem: fixed sketch size in MinHash requires knowing accuracy requirements upfront, leading to inefficiency.\",\n     6\t    \"Cross-domain thinking is creative: applying fountain/rateless code principles to sketching is a novel angle not explored in the literature.\",\n     7\t    \"Progressive estimation with adaptive stopping is valuable for streaming, distributed deduplication, and LLM training data scenarios.\",\n     8\t    \"Related work section is reasonably comprehensive, citing standard MinHash, b-bit MinHash, SetSketch, and recent variants like HyperMinHash.\",\n     9\t    \"The motivation is clear and well-articulated\u2014the problem of not knowing optimal sketch size beforehand is real.\"\n    10\t  ],\n    11\t  \n    12\t  \"dimension_scores\": [\n    13\t    {\n    14\t      \"dimension\": \"soundness\",\n    15\t      \"score\": 2,\n    16\t      \"justification\": \"The proposed methodology has fundamental issues: (1) The connection between fountain codes and MinHash is not mathematically established\u2014fountain codes generate redundant symbols for erasure recovery, while MinHash estimates similarities via minimum hash values; these are fundamentally different operations. (2) Rate-distortion theory application to Jaccard estimation lacks a clear source distribution and distortion measure formulation. (3) The assumption that hash values can be generated as a sequence where error decays monotonically needs proof\u2014correlated hash values from fountain coding may not provide independent estimates.\",\n    17\t      \"improvements\": [\n    18\t        \"Clarify the mathematical connection: How exactly does fountain coding apply to generating MinHash values? Fountain codes encode finite symbols; MinHash uses minimum over permutations. Propose a concrete encoding scheme (e.g., treat set elements as source symbols, encode using LT/Raptor, then define how to extract Jaccard estimates from received symbols).\",\n    19\t        \"Formulate the rate-distortion problem precisely: Define the source (pair of sets?), the rate (bits in sketch), the distortion measure (MSE on Jaccard estimate?), and derive or bound the rate-distortion function. Currently this is asserted but not developed.\",\n    20\t        \"Address the independence assumption: Standard MinHash uses independent permutations to get independent estimates. Fountain-coded hashes will be dependent by construction. Provide theoretical analysis of how this dependence affects estimation variance and bias.\",\n    21\t        \"Expected score impact: These are major issues\u2014fixing them could raise soundness from 2 to 3 or 4.\"\n    22\t      ]\n    23\t    },\n    24\t    {\n    25\t      \"dimension\": \"presentation\",\n    26\t      \"score\": 3,\n    27\t      \"justification\": \"The hypothesis is clearly written with good motivation and a reasonable related work section. The connection to fountain codes and rate-distortion theory is described at a high level but lacks concrete technical details that would allow an expert to evaluate feasibility. The investigation approach is outlined but is quite abstract.\",\n    28\t      \"improvements\": [\n    29\t        \"Provide a concrete algorithmic sketch: Give a pseudo-code or mathematical description of how the rateless MinHash would work. How are set elements encoded? How are hash values generated sequentially? How is Jaccard estimated from a prefix of the sequence?\",\n    30\t        \"Define notation precisely: What is the 'sequence of hash values'? Are these minimum values under different permutations? Or something else? How does fountain coding enter the picture?\",\n    31\t        \"Add a feasibility analysis: What is the computational complexity of generating and decoding these rateless sketches? How does it compare to standard MinHash?\",\n    32\t        \"Expected score impact: Minor to moderate improvement\u2014better presentation alone won't fix fundamental soundness issues, but it would make the work more reviewable (3\u21923.5).\"\n    33\t      ]\n    34\t    },\n    35\t    {\n    36\t      \"dimension\": \"contribution\",\n    37\t      \"score\": 3,\n    38\t      \"justification\": \"If the approach works, the contribution would be significant: a truly adaptive MinHash that doesn't require fixing sketch size upfront would be valuable for many applications (deduplication, streaming, distributed systems). The cross-domain connection to coding theory could open new research directions. However, the contribution is currently speculative\u2014the hypothesis has not demonstrated that the fountain code approach actually provides benefits over simpler adaptive approaches (e.g., just generating more standard MinHash values on-demand).\",\n    39\t      \"improvements\": [\n    40\t        \"Compare against simpler baselines: Why use fountain codes specifically? Could one achieve progressive estimation simply by generating standard MinHash values incrementally (since they're independent)? The hypothesis should justify why fountain coding is necessary or beneficial vs. simpler approaches.\",\n    41\t        \"Quantify the expected benefit: Provide theoretical or preliminary empirical evidence that rateless MinHash achieves better space-accuracy trade-offs. E.g., derive the expected sketch size for a target accuracy and compare to fixed-size MinHash bounds.\",\n    42\t        \"Address practical concerns: Can the rateless MinHash support set operations (union, intersection) like standard MinHash? This is important for many applications. Fountain codes may not preserve these properties.\",\n    43\t        \"Expected score impact: Addressing these could raise contribution score from 3 to 4 if the approach is shown to be both novel and practically beneficial.\"\n    44\t      ]\n    45\t    }\n    46\t  ],\n    47\t  \n    48\t  \"critiques\": [\n    49\t    {\n    50\t      \"category\": \"methodology\",\n    51\t      \"severity\": \"major\",\n    52\t      \"description\": \"The connection between fountain codes and MinHash is not mathematically established. Fountain codes (LT, Raptor) are designed for erasure recovery: given k source symbols, they generate an infinite sequence of coded symbols such that any k'(1+\u03b5) symbols can recover the original k symbols. MinHash, conversely, estimates Jaccard similarity by computing minimum hash values under random permutations. The hypothesis asserts these can be connected but doesn't explain how. Key unanswered questions: (1) What are the 'source symbols' for the fountain code? (2) How does one recover Jaccard similarity from fountain-coded symbols? (3) What is the equivalent of 'erasure' in the MinHash context?\",\n    53\t      \"suggested_action\": \"Provide a concrete technical proposal for how fountain coding would be applied. One possible approach: Treat each set element as a source symbol. Use fountain coding to generate a stream of coded symbols. Define the MinHash estimate from the first k coded symbols as the minimum over some function of these symbols. Analyze the statistical properties of this estimate. Alternatively, reconsider whether fountain codes are the right analogy\u2014perhaps the real insight is 'progressive refining estimates' which could be achieved more directly.\"\n    54\t    },\n    55\t    {\n    56\t      \"category\": \"methodology\",\n    57\t      \"severity\": \"major\",\n    58\t      \"description\": \"Rate-distortion theory application is not formulated. The hypothesis states 'Jaccard similarity estimation can be framed as a rate-distortion problem where rate = sketch size and distortion = mean squared error' but doesn't develop this framework. Rate-distortion theory requires: (1) A source distribution P(A,B) over pairs of sets, (2) An encoding function mapping sets to sketches, (3) A decoding function mapping sketches to Jaccard estimates, (4) A distortion measure D(J_true, J_estimated). None of these are defined. Furthermore, the rate-distortion function R(D) characterizes the fundamental limit\u2014but the hypothesis aims to design a practical algorithm, not just bound performance.\",\n    59\t      \"suggested_action\": \"Formulate the rate-distortion problem explicitly: Define the source distribution, the encoding/decoding functions, and the distortion measure. Derive (or cite) the rate-distortion function for Jaccard estimation. Alternatively, if the goal is practical algorithm design rather than fundamental limits, reframe the contribution as 'designing an adaptive MinHash with near-optimal space-accuracy trade-off' and use the rate-distortion function as an evaluation benchmark.\"\n    60\t    },\n    61\t    {\n    62\t      \"category\": \"novelty\",\n    63\t      \"severity\": \"major\",\n    64\t      \"description\": \"The hypothesis may be incremental over existing work on adaptive sketching. The related work cites SetSketch, b-bit MinHash, HyperMinHash\u2014all of which address space-accuracy trade-offs for MinHash. The key differentiation claimed is 'adaptive sketch size' vs 'fixed at creation time.' However, one could achieve adaptive estimation simply by computing additional standard MinHash values on-demand (since each MinHash value provides an independent estimate). The hypothesis should clarify what fountain codes add beyond 'generate more hashes as needed.' If the answer is 'nothing,' then the contribution is incremental. If fountain codes provide coding gain (better estimates per bit), this should be demonstrated.\",\n    65\t      \"suggested_action\": \"Compare against the naive adaptive baseline: Generate k standard MinHash values, estimate Jaccard, compute confidence interval, generate more if needed. Why is this insufficient? What do fountain codes provide that independence doesn't? Possible answers: (1) Fountain-coded hashes may have lower variance through careful dependence design, (2) The rate-distortion framework provides optimal stopping rules, (3) The approach enables progressive estimation in distributed settings where communication is expensive. Articulate and demonstrate the advantage.\"\n    66\t    },\n    67\t    {\n    68\t      \"category\": \"rigor\",\n    69\t      \"severity\": \"major\",\n    70\t      \"description\": \"The assumption that 'estimation error decays monotonically as more hash values are received' needs proof. For standard MinHash with independent permutations, the estimation variance decays as 1/k where k is the number of hashes\u2014this is monotonic in expectation but not necessarily monotonic for any particular pair of sets. For fountain-coded hashes, the dependence structure may cause non-monotonic behavior: early symbols may provide little information, then later symbols may dramatically improve estimates. The hypothesis should analyze the learning curve theoretically.\",\n    71\t      \"suggested_action\": \"Provide theoretical analysis of the estimation error as a function of the number of hash values. For standard MinHash, Var[J_hat] = J(1-J)/k. What is Var[J_hat] for the proposed rateless MinHash? Does it decay monotonically? At what rate? If the rate is slower than 1/k, the approach may be worse than standard MinHash despite being adaptive.\"\n    72\t    },\n    73\t    {\n    74\t      \"category\": \"scope\",\n    75\t      \"severity\": \"minor\",\n    76\t      \"description\": \"The investigation approach is ambitious but may be too broad. Formalizing MinHash as rate-distortion, designing a fountain-code-inspired scheme, deriving optimal stopping rules, and implementing/evaluating on LLM deduplication benchmarks is a lot for one paper. The hypothesis could benefit from a more focused contribution: either (1) the theoretical rate-distortion formulation, or (2) the rateless MinHash algorithm design, or (3) the application to LLM deduplication. Trying to do all three may result in superficial treatment of each.\",\n    77\t      \"suggested_action\": \"Consider narrowing the scope: Focus on the core theoretical contribution (rateless MinHash design and analysis) with evaluation on standard datasets. Or focus on the application (LLM deduplication) with the rateless MinHash as a practical tool. A narrowed scope would allow deeper treatment and higher confidence in results.\"\n    78\t    },\n    79\t    {\n    80\t      \"category\": \"clarity\",\n    81\t      \"severity\": \"minor\",\n    82\t      \"description\": \"The hypothesis uses terminology from coding theory ('rateless,' 'fountain codes,' 'rate-distortion') without precisely defining how these map to the MinHash context. For example, 'rateless' in fountain codes means 'can generate arbitrary many encoded symbols'\u2014in the MinHash context, this could mean 'can generate arbitrary many hash values,' but then standard MinHash is already 'rateless' in this sense (just generate more permutations). The specific value of fountain codes is unclear.\",\n    83\t      \"suggested_action\": \"Define terminology precisely in the context of the problem. Explain: (1) What makes the proposed MinHash 'rateless' beyond just generating more hashes? (2) How exactly are fountain code principles applied? (3) What is the 'rate' and 'distortion' in the rate-distortion formulation? A reader familiar with either coding theory or MinHash (but not both) should be able to understand the connection.\"\n    84\t    },\n    85\t    {\n    86\t      \"category\": \"evidence\",\n    87\t      \"severity\": \"minor\",\n    88\t      \"description\": \"The hypothesis would be stronger with preliminary evidence or a concrete example. Even a small-scale simulation showing that fountain-coded MinHash provides progressive estimates with favorable space-accuracy trade-offs would substantially increase confidence. Currently, the hypothesis is purely conceptual without any proof-of-concept.\",\n    89\t      \"suggested_action\": \"Add a proof-of-concept experiment: Implement a simple version of rateless MinHash (even if not fully optimized) and compare against standard MinHash on a small dataset. Show that (1) estimates improve with more hash values, (2) the space-accuracy trade-off is favorable. This could be included as a preliminary result or a cited technical report.\"\n    90\t    }\n    91\t  ],\n    92\t  \n    93\t  \"score\": 5,\n    94\t  \"confidence\": 4,\n    95\t  \"relation_type\": null,\n    96\t  \"relation_rationale\": \"\"\n    97\t}\n"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [61] ASSISTANT · 2026-07-03 17:55:47 UTC

```
The review file has been created. Let me now provide a summary of my review and signal completion.

## Summary

I've completed a thorough peer review of the "Rateless MinHash" hypothesis. Here are the key findings:

**Overall Assessment**: The hypothesis proposes a creative cross-domain connection between fountain codes and MinHash sketching. While the problem addressed (fixed sketch size in MinHash) is genuine, the hypothesis has fundamental methodological issues that must be resolved before experiments can yield meaningful results.

**Key Strengths**:
1. Addresses a real practical problem with MinHash
2. Creative cross-domain thinking
3. Progressive estimation is valuable for many applications
4. Reasonable related work coverage

**Major Issues** (Score Impact: High):
1. **Methodology**: The connection between fountain codes and MinHash is not mathematically established. Fountain codes operate on finite alphabets with erasure recovery; MinHash estimates Jaccard via minimum hash values. How these connect is unclear.

2. **Methodology**: Rate-distortion theory application lacks formulation. The source distribution, encoding/decoding functions, and distortion measure are not defined.

3. **Novelty**: The hypothesis may be incremental—one could achieve adaptive estimation simply by generating standard MinHash values incrementally. The unique advantage of fountain codes is not demonstrated.

4. **Rigor**: The assumption that estimation error decays monotonically needs proof, especially given the dependence structure of fountain-coded hashes.

**Score**: 5 (Borderline Accept - technically solid where reasons to accept outweigh reasons to reject, but major methodological issues need resolution)

**Confidence**: 4 (Confident but not absolutely certain)

The review file has been saved to the required location. The hypothesis author now has detailed, actionable feedback to improve the work before experimental validation.
```

### [62] TOOL CALL — finish · 2026-07-03 17:55:47 UTC

```
{
  "message": "I have completed a thorough peer review of the \"Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes\" hypothesis. \n\nThe review has been saved to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json`\n\n**Key Review Findings**:\n\n**Overall Score**: 5/10 (Borderline Accept)\n\n**Major Issues Identified**:\n1. **Methodology - Fountain Code Connection Unclear**: The hypothesis asserts a connection between fountain codes and MinHash but doesn't explain the mathematical mapping. Fountain codes recover erased symbols; MinHash estimates similarities. How these connect needs explicit formulation.\n\n2. **Methodology - Rate-Distortion Not Formulated**: The rate-distortion framework for Jaccard estimation is asserted but not developed. Source distribution, encoding/decoding functions, and distortion measures are undefined.\n\n3. **Novelty - Incremental Over Simple Adaptive Baselines**: One could achieve progressive estimation simply by generating standard MinHash values on-demand. The hypothesis doesn't demonstrate what fountain codes add beyond this naive approach.\n\n4. **Rigor - Monotonic Error Decay Unproven**: The assumption that estimation error decays monotonically with more hash values needs theoretical analysis, especially given dependence in fountain-coded hashes.\n\n**Minor Issues**:\n- Scope may be too broad (theoretical formulation + algorithm design + LLM application)\n- Terminology from coding theory not precisely mapped to MinHash context\n- No proof-of-concept evidence provided\n\n**Strengths**:\n- Addresses a genuine problem (fixed sketch size in MinHash)\n- Creative cross-domain thinking\n- Clear motivation and reasonable related work\n\nThe review provides detailed, actionable suggestions for each issue to help the author improve the hypothesis before experimental validation."
}
```

### [63] TOOL RESULT — finish · 2026-07-03 17:55:47 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "I have completed a thorough peer review of the \"Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes\" hypothesis. \n\nThe review has been saved to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/iter_1/review_hypo/.sdk_openhands_agent_struct_out.json`\n\n**Key Review Findings**:\n\n**Overall Score**: 5/10 (Borderline Accept)\n\n**Major Issues Identified**:\n1. **Methodology - Fountain Code Connection Unclear**: The hypothesis asserts a connection between fountain codes and MinHash but doesn't explain the mathematical mapping. Fountain codes recover erased symbols; MinHash estimates similarities. How these connect needs explicit formulation.\n\n2. **Methodology - Rate-Distortion Not Formulated**: The rate-distortion framework for Jaccard estimation is asserted but not developed. Source distribution, encoding/decoding functions, and distortion measures are undefined.\n\n3. **Novelty - Incremental Over Simple Adaptive Baselines**: One could achieve progressive estimation simply by generating standard MinHash values on-demand. The hypothesis doesn't demonstrate what fountain codes add beyond this naive approach.\n\n4. **Rigor - Monotonic Error Decay Unproven**: The assumption that estimation error decays monotonically with more hash values needs theoretical analysis, especially given dependence in fountain-coded hashes.\n\n**Minor Issues**:\n- Scope may be too broad (theoretical formulation + algorithm design + LLM application)\n- Terminology from coding theory not precisely mapped to MinHash context\n- No proof-of-concept evidence provided\n\n**Strengths**:\n- Addresses a genuine problem (fixed sketch size in MinHash)\n- Creative cross-domain thinking\n- Clear motivation and reasonable related work\n\nThe review provides detailed, actionable suggestions for each issue to help the author improve the hypothesis before experimental validation."}], "is_error": false, "kind": "FinishObservation"}
```

### [64] HOOK — PostToolUse · 2026-07-03 17:55:47 UTC

```
<system-reminder>You have 112.2 minutes remaining to finish all your tasks.</system-reminder>
```
