# gen_plan_proof_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_sAQsTTaaqjOV` — Near Duplicate Finder
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_proof_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 18:43:43 UTC

````
<hypothesis>
kind: hypothesis
title: 'Rateless MinHash: Progressive Jaccard Estimation with Adaptive Stopping'
hypothesis: >-
  By generating MinHash values sequentially using a coded scheme inspired by fountain codes, we can create a MinHash variant
  that enables progressive Jaccard similarity estimation with adaptive stopping. The method trades statistical efficiency
  (1.01-1.93x higher MSE than independent hashes at equal bit budgets) for the ability to refine estimates on-demand without
  fixing sketch size upfront. The key theoretical challenge is analyzing the dependencies introduced by the coding process,
  which determine the variance penalty. The method is most useful in applications where the optimal sketch size is data-dependent
  and unknown beforehand, such as distributed deduplication with diverse similarity distributions.
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
_relation_rationale: >-
  Narrowing scope to dependency analysis and honest baseline comparison, not rate-distortion optimality.
_confidence_delta: decreased
_key_changes:
- >-
  Added honest acknowledgment of 1.01-1.93x statistical efficiency penalty from experiments
- >-
  Narrowed investigation approach: now includes comparing against simple adaptive baselines (sequential independent MinHash)
- >-
  Reframed contribution: from 'optimal rate-distortion' to 'analyzing dependency structure in progressive MinHash'
- >-
  Added theoretical analysis of dependencies as primary investigation goal (deriving E[π_i π_j] and covariance bounds)
- >-
  Clarified that the method's value depends on applications where progressive estimation justifies the efficiency penalty
- Added real-world evaluation on near-duplicate detection as success criterion
- >-
  Removed overstated claims about rate-distortion theory providing 'computable bound for optimal stopping' (function is unknown)
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: proof_iter2_dir1
type: proof
objective: >-
  Derive the theoretical dependency structure in Rateless MinHash: compute E[π_i π_j] and bound covariance terms
approach: >-
  Formally analyze the probability of matches at two positions in Rateless MinHash. Let π_i be the indicator that coded hash
  i matches. Start by deriving E[π_i] = J (the MinHash property). Then derive E[π_i π_j] = Pr[π_i = 1 ∧ π_j = 1] as a function
  of: (1) the true Jaccard similarity J, (2) the degree distribution μ(d), (3) the probability of index overlap between positions
  i and j. The key challenge is that the min operation over selected base hashes creates dependencies different from XOR in
  LT codes. Bound Cov[π_i, π_j] = E[π_i π_j] - J². Show how the expected total covariance sum depends on the degree distribution.
  Compare against independent samples case (Cov=0). Relate bounds to the observed 1.01-1.93x MSE penalty from previous experiments.
  Consider whether an optimal degree distribution exists that minimizes total covariance while maintaining rateless property.
  Formalize probability calculations and variance bounds in Lean 4.
depends_on:
- id: art_9jz-SfB9wrwJ
  label: theory_background
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
id: art_9jz-SfB9wrwJ
type: research
title: Rateless MinHash Theory Foundations Research
summary: >-
  This research provides the theoretical foundations for Rateless MinHash, a novel sketching approach addressing the fundamental
  limitation of fixed sketch size in existing MinHash variants. Key findings include: (1) All current MinHash variants (Standard,
  b-bit, SetSketch, Odd Sketch, ProbMinHash) require upfront sketch size selection [1, 4, 6, 7, 8]. (2) Fountain codes (LT
  codes, Raptor codes) provide a proven rateless encoding framework where infinite symbol sequences can be generated with
  decoding possible from any slightly larger set [9, 10]. (3) The rate-distortion function for Jaccard similarity estimation
  remains undiscovered, though lower bounds exist from information complexity [3, 11, 12]. (4) A mathematical framework for
  Rateless MinHash is proposed, featuring encoding via degree-distributed hash generation, progressive decoding with decreasing
  variance O(1/k), and optimal stopping rules based on sequential estimation theory. The expected contribution is a sketch
  achieving near-optimal rate-distortion performance while adapting to diverse similarity regimes without upfront parameter
  tuning.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for proof artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_plan/gen_plan_proof_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for a PROOF artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "informal_proof_draft": {
      "description": "Initial proof sketch in plain language - this is a first draft that may be refined or corrected during execution",
      "title": "Informal Proof Draft",
      "type": "string"
    },
    "explanation": {
      "description": "Why this proof matters and how it advances the research",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "informal_proof_draft",
    "explanation"
  ],
  "title": "ProofPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_2/gen_plan/gen_plan_proof_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 18:43:43 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-03 18:44:13 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SKILL-INPUT — aii-lean · 2026-07-03 18:44:21 UTC

The agent loaded the **aii-lean** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-lean
description: Compiles and verifies Lean 4 code using lean-interact. Use for checking proof validity, theorem proving, and formal verification. Supports search across Mathlib, tactic suggestions (exact?, apply?, simp?), and sorry-driven proof development.
---

**IMPORTANT - Path resolution:** Always use an absolute SKILL_DIR. The CWD may not be the project root (e.g. on worker pods).
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```
GNU `parallel` subshells do NOT inherit `source activate`. Use `export` and **single-quoted** command templates.

## Workflow: Sorry-Driven Proof Development

The standard mathematician workflow for formalizing proofs in Lean 4:

### Step 1: Formalize the Statement
Write the theorem signature — what you want to prove:
```lean
import Mathlib.Tactic

theorem my_theorem (x y : Int) (h : x < y) : x + 1 ≤ y := by
  sorry
```

### Step 2: Search Mathlib for Relevant Lemmas
Find existing theorems by type pattern via Loogle:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_mathlib_pattern_search.py "Int.lt_iff_add_one_le"
```

### Step 3: Try Tactics at Sorry Positions
Submit code with sorry and let the suggest tool try tactics:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_lean_suggest.py \
  --code "import Mathlib.Tactic
theorem ex : 1 + 1 = 2 := by sorry" \
  --tactics "exact?,simp?,omega,ring"
```

Returns goals at each sorry and which tactics close them.

### Step 4: Fill Sorrys Iteratively
Replace each sorry with the tactic that worked. Sorrys can be filled in any order — each is independent. For complex proofs, break into sub-lemmas with their own sorrys.

### Step 5: Verify Complete Proof
Compile the full proof — a clean compile with no sorrys means done:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
echo 'import Mathlib.Tactic
theorem ex (x y : Int) (h : x < y) : x + 1 ≤ y := by linarith' | $SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_run_lean.py -
```

`verified: true` = proof is complete and correct.

---

## Scripts

### Run / Verify (aii_run_lean.py)

Compile and verify Lean 4 code. Mathlib always enabled. Returns JSON with goal states at sorry positions.

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
echo 'theorem test : 1 + 1 = 2 := rfl' | $SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_run_lean.py -
```

**Parallel execution:**
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_run_lean.py" && \
parallel -j 30 -k --group --will-cite '$PY $S {}' ::: proof1.lean proof2.lean
```

**Output (verified):**
```json
{
  "success": true,
  "verified": true,
  "has_sorries": false,
  "sorry_goals": [],
  "errors": [],
  "warnings": [],
  "infos": []
}
```

**Output (sorry — shows goals):**
```json
{
  "success": true,
  "verified": false,
  "has_sorries": true,
  "sorry_goals": [
    {"sorry_index": 0, "goal": "⊢ 1 + 1 = 2", "proof_state": 0}
  ],
  "errors": [],
  "warnings": ["declaration uses 'sorry'"],
  "infos": []
}
```

**Parameters:**
- `file` (required) — Lean file to verify, or `-` for stdin
- Exit code 0 = verified, 1 = failed

---

### Suggest Tactics (aii_lean_suggest.py)

Try tactics at sorry positions. Extracts goals, runs each tactic, reports what works.

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_lean_suggest.py \
  --code "import Mathlib.Tactic
theorem ex : 1 + 1 = 2 := by sorry" \
  --tactics "exact?,simp?,omega,ring"
```

**Output:**
```json
{
  "success": true,
  "goals": [
    {"sorry_index": 0, "goal": "⊢ 1 + 1 = 2", "proof_state": 0}
  ],
  "suggestions": [
    {"sorry_index": 0, "tactic": "exact?", "success": true, "result": "Try this: exact rfl", "closes_goal": true},
    {"sorry_index": 0, "tactic": "simp?", "success": true, "result": "Try this: simp", "closes_goal": true},
    {"sorry_index": 0, "tactic": "omega", "success": true, "result": "", "closes_goal": true}
  ],
  "errors": []
}
```

**Parameters:**
- `--code, -c` (required) — Lean 4 code with sorry placeholders
- `--tactics, -t` (optional) — Comma-separated tactics (default: exact?,apply?,simp?,rw?,simp,aesop,omega,decide,ring,linarith,nlinarith,norm_num,field_simp,positivity)

**Useful tactics to try:**
- Discovery: `exact?`, `apply?`, `rw?`, `simp?`
- Automation: `simp`, `aesop`, `omega`, `decide`, `ring`, `linarith`, `nlinarith`, `norm_num`
- Field: `field_simp`, `polyrith`

---

### Pattern Search (aii_mathlib_pattern_search.py)

Search by type signature and patterns via Loogle API.

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_mathlib_pattern_search.py "List.map"
```

**Parallel execution:**
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-lean" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_mathlib_pattern_search.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 10' ::: 'List.map' 'Nat.Prime'
```

**Query patterns:**
- By constant: `Real.sin`
- By name substring: `"differ"`
- By subexpression: `_ * (_ ^ _)`
- Non-linear: `Real.sqrt ?a * Real.sqrt ?a`
- By conclusion: `|- tsum _ = _ * tsum _`
- Multiple filters: `Real.sin, "two", _ * _`

**Parameters:**
- `query` (required) — Type pattern query
- `--limit, -n` — Number of results (default: 10)
- `--timeout, -t` — Timeout in seconds (default: 30)

**Tip:** Pure type queries like `Nat → Nat` timeout — add a constant: `Nat.succ, Nat → Nat`

---

## Mathlib Tactics Reference

Mathlib is always enabled (Lean v4.14.0). Common tactics:

**Automation (close goals directly):**
- `ring` — Polynomial ring equations
- `linarith` — Linear arithmetic over ordered fields
- `nlinarith` — Nonlinear arithmetic
- `omega` — Integer/natural linear arithmetic (decision procedure)
- `decide` — Decidable propositions
- `norm_num` — Numeric normalization
- `simp` — Simplifier with extensible lemma set
- `aesop` — General proof search (best-first)

**Discovery (find what lemma/tactic to use):**
- `exact?` — Find a single lemma that closes the goal
- `apply?` — Find a lemma that applies (may leave subgoals)
- `rw?` — Find rewrite lemmas for subterms
- `simp?` — Run simplifier and report which lemmas fired

**Examples:**
```lean
import Mathlib.Tactic

-- ring closes polynomial identities
example (x y : Int) : (x + y)^2 = x^2 + 2*x*y + y^2 := by ring

-- linarith closes linear inequalities
example (x y : Int) (h1 : x < y) (h2 : y < x + 3) : y - x < 3 := by linarith

-- omega handles Nat/Int linear arithmetic
example (n : Nat) (h : n ≥ 2) : n * n ≥ 4 := by omega
```

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
