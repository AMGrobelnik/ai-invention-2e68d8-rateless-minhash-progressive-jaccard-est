# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_sAQsTTaaqjOV` — Rateless MinHash: Progressive Jaccard Estimation via Fountain Codes
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 17:56:43 UTC

````
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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Collect and prepare datasets for evaluating near-duplicate detection and Jaccard similarity estimation, suitable for benchmarking
  rateless MinHash against baselines.
approach: >-
  Acquire datasets relevant to the hypothesis evaluation: (1) Near-duplicate text detection datasets (e.g., Quora Question
  Pairs, MS MARCO with duplicates, or synthetic near-duplicate sets); (2) LLM training data deduplication benchmarks (subsets
  of The Pile or C4 with known duplication); (3) Standard MinHash evaluation datasets (e.g., AOL search logs, document collections).
  Format all datasets into a common JSON schema with sets represented as token lists or hash sets. Create mini/preview variants
  for gradual scaling. Target total size under 300MB.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for dataset artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for a DATASET artifact.",
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
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_sAQsTTaaqjOV/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 17:56:43 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-03 17:56:49 UTC

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

### [4] SKILL-INPUT — aii-hf-datasets · 2026-07-03 17:57:09 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SYSTEM-USER prompt · 2026-07-03 18:04:52 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 2 problems — fix ALL of them at once:
  - at `dataset_search_plan`: {'phase_1_datasets_to_acquire': [{'dataset_name': 'Quora Question Pairs', 'source': 'HuggingFace: `quora` dataset (caelan/quora-question-pairs or similar)', 'backup_source': 'Kaggle API: `quora-question-pairs` competition data', 'description': 'Contains pairs of questions with binary label indicating if they are duplicates. Ideal for evaluating near-duplicate detection.', 'expected_format': 'CSV with columns: id, qid1, qid2, question1, question2, is_duplicate', 'preprocessing_steps': ["Load dataset via datasets.load_dataset('quora') or from CSV", 'Extract unique questions and assign IDs', 'Create duplicate pairs based on is_duplicate=1', 'Tokenize questions (simple word tokenization or n-gram shingles)', 'Output JSON with schema: {id, text, tokens, duplicate_pairs: [{id1, id2}]}'], 'estimated_size': '50MB after processing (subset of pairs)', 'target_samples': '5000-10000 question pairs', 'huggingface_search_query': 'quora question pairs duplicate detection'}, {'dataset_name': 'MS MARCO Passage Ranking', 'source': 'HuggingFace: `ms_marco` dataset (multiple versions available)', 'backup_source': 'Official Microsoft download: https://microsoft.github.io/MSMARCO-Passage-Ranking/', 'description': 'Passage retrieval dataset with queries and passages. Contains duplicate passages that can be identified for near-duplicate evaluation.', 'expected_format': 'JSON/TSV with queries, passages, and relevance labels', 'preprocessing_steps': ["Load via datasets.load_dataset('ms_marco', 'v1.1')", 'Extract passages and identify near-duplicates using existing qrels or by computing Jaccard on passages', 'Sample subsets to control size', 'Create passage sets with token overlap information', 'Output JSON with schema: {id, text, tokens, query_id, is_duplicate_passage}'], 'estimated_size': '80MB after processing (sampled)', 'target_samples': '10000 passages with known duplicates', 'huggingface_search_query': 'ms marco passage ranking'}, {'dataset_name': 'The Pile (Subset with Deduplication Info)', 'source': 'HuggingFace: `the_pile` by EleutherAI (sample subsets)', 'backup_source': 'Direct download from EleutherAI website or GitHub', 'description': 'Large-scale text dataset. Subsets can be sampled and synthetic near-duplicates can be introduced for evaluation.', 'expected_format': 'JSONL with text documents from various domains', 'preprocessing_steps': ["Load via datasets.load_dataset('the_pile', split='train', streaming=True)", 'Sample 5000-10000 documents from specific subsets (e.g., PubMed, GitHub, ArXiv)', 'Introduce synthetic near-duplicates by copying documents with small modifications (word substitutions, deletions)', 'Create ground truth duplicate clusters', 'Output JSON with schema: {id, text, tokens, cluster_id, is_synthetic_duplicate}'], 'estimated_size': '100MB after processing (sampled + synthetic duplicates)', 'target_samples': '5000 original + 2000 synthetic near-duplicates', 'huggingface_search_query': 'the pile eleutherai'}, {'dataset_name': 'C4 (Colossal Clean Crawled Corpus) Subset', 'source': 'HuggingFace: `c4` dataset (English subset)', 'backup_source': 'TensorFlow Datasets (TFDS): `c4`', 'description': 'Cleaned Common Crawl dataset. Can sample subsets and use built-in deduplication information if available.', 'expected_format': 'JSON with text field and metadata', 'preprocessing_steps': ["Load via datasets.load_dataset('c4', 'en', split='train', streaming=True)", 'Sample 5000-10000 documents', 'Identify near-duplicates using existing deduplication metadata or by clustering', 'Create evaluation subsets with known similarity distributions', 'Output JSON with schema: {id, text, tokens, url, timestamp, deduplication_cluster}'], 'estimated_size': '80MB after processing (sampled)', 'target_samples': '5000-8000 documents', 'huggingface_search_query': 'c4 colossal clean crawled corpus'}, {'dataset_name': 'AOL Search Logs', 'source': 'UCI ML Repository or direct academic source', 'backup_source': 'Research paper repositories, archive.org', 'description': 'Search query logs with potential duplicates (similar queries). Useful for evaluating MinHash on query-level deduplication.', 'expected_format': 'Text file with queries, user IDs, timestamps', 'preprocessing_steps': ['Search for AOL search log dataset (multiple sources available)', 'Parse query logs and extract unique queries', 'Identify near-duplicate queries (same user, similar wording)', 'Create query sets with known similarities', 'Output JSON with schema: {id, query, tokens, user_id, timestamp, session_id}'], 'estimated_size': '30MB after processing', 'target_samples': '10000 unique queries', 'search_query': 'AOL search logs dataset query duplicates'}, {'dataset_name': '20 Newsgroups (for Standard MinHash Evaluation)', 'source': 'sklearn.datasets.fetch_20newsgroups or HuggingFace', 'backup_source': 'UCI ML Repository: `twenty-newsgroups`', 'description': 'Classic document classification dataset. Can be used to evaluate Jaccard similarity estimation across newsgroups.', 'expected_format': 'Text documents with newsgroup labels', 'preprocessing_steps': ['Load via sklearn.datasets.fetch_20newsgroups() or HuggingFace', 'Extract documents and labels', 'Create document pairs within and across newsgroups (expect higher Jaccard within same group)', 'Tokenize and create shingles', 'Output JSON with schema: {id, text, tokens, newsgroup, document_pairs: [{id1, id2, same_group}]}'], 'estimated_size': '20MB after processing', 'target_samples': '5000 documents', 'huggingface_search_query': '20 newsgroups sklearn'}, {'dataset_name': 'Synthetic Near-Duplicate Sets (Fallback/Supplement)', 'source': 'Generate programmatically using Python', 'description': 'Create synthetic datasets with controlled Jaccard similarity distributions to test specific aspects of Rateless MinHash.', 'generation_steps': ['Generate base documents with known token sets', 'Create near-duplicates by controlling token overlap (target Jaccard: 0.1, 0.3, 0.5, 0.7, 0.9)', 'Generate documents with varying lengths (100-5000 tokens)', 'Create evaluation scenarios: streaming, batch, high/low similarity', 'Output JSON with schema: {id, text, tokens, target_jaccard, duplicate_group, similarity_level}'], 'estimated_size': '10MB (small but precise control)', 'target_samples': '2000 document groups with known Jaccard similarities', 'code_reference': "Use Python's random module, NLTK or simple word lists for text generation"}], 'phase_2_standardization_and_schema': {'output_format': {'description': 'The final data_out.json should be a JSON array where each element represents one document from any of the datasets. All documents from all datasets are merged into this single array. The metadata.source_dataset field indicates which original dataset each document came from.', 'example_output_structure': "See expected_outputs for file names. data_out.json format: [ {id: 'quora_001', text: '...', tokens: [...], metadata: {...}}, {id: 'ms_marco_001', ...}, ... ]"}, 'common_json_schema': {'description': 'All datasets must be converted to this common schema. The output data_out.json should be a JSON array where each element is an object with these fields.', 'schema': {'id': 'string or integer - unique document identifier (required)', 'text': 'string - raw text content (for reference/debugging) (required)', 'tokens': 'array of strings - tokenized text for MinHash computation (required)', 'metadata': {'source_dataset': 'string - name of original dataset (required)', 'duplicate_id': 'string or null - cluster ID for duplicates (if known, otherwise null)', 'similarity_level': 'string or null - high/medium/low (if known, otherwise null)', 'document_length': 'integer - number of tokens (required, computed from tokens array)', 'additional_fields': 'object - dataset-specific fields as needed (optional)'}}, 'example': {'id': 'quora_001', 'text': 'What is the capital of France?', 'tokens': ['what', 'is', 'the', 'capital', 'of', 'france'], 'metadata': {'source_dataset': 'quora_question_pairs', 'duplicate_id': 'dup_group_12', 'similarity_level': 'high', 'document_length': 6}}}, 'tokenization_approach': ['Default: Simple whitespace + punctuation tokenization (split on non-alphanumeric)', 'Alternative: Use nltk.word_tokenize for better quality (if nltk available)', 'For shingles: Create k-shingles (k=2,3,5) from tokens', 'Store both tokens and optional shingles in output'], 'mini_preview_variants': ['Preview variant: 3 samples with truncated text (100 chars max) - for quick inspection', 'Mini variant: 3-5 full samples - for development and testing', 'Full variant: Complete dataset (or sampled subset for large datasets)']}, 'phase_3_execution_steps': [{'step': 1, 'action': 'Search and verify dataset availability', 'commands': ["Use aii-hf-datasets skill to search: 'quora', 'ms marco', 'the pile', 'c4', '20 newsgroups'", 'Check dataset loadability and size via preview', 'Identify backup sources if HuggingFace datasets are unavailable'], 'verification': 'At least 5 datasets confirmed available'}, {'step': 2, 'action': 'Download and preview datasets', 'commands': ['For each dataset: run aii_hf_download_datasets.py to get preview/mini/full variants', 'Inspect preview files to understand schema', 'Document actual column names and format for preprocessing'], 'verification': 'Preview files created for all datasets'}, {'step': 3, 'action': 'Implement preprocessing scripts', 'commands': ['Create Python script to load each dataset', 'Implement tokenization (simple split or nltk)', 'Create duplicate pair extraction/synthesis logic', 'Convert to common JSON schema', 'Handle large datasets via streaming/sampling'], 'verification': 'Script runs successfully on mini variants'}, {'step': 4, 'action': 'Generate standardized output', 'commands': ['Process all datasets and save to data_out.json', 'Create mini and preview variants using aii-json skill', 'Validate JSON schema using aii-json validate', 'Check total file size < 300MB'], 'verification': 'data_out.json exists with valid schema, size < 300MB'}, {'step': 5, 'action': 'Validate and document', 'commands': ['Compute basic statistics: number of documents, duplicate pairs, Jaccard distribution', 'Create dataset_summary.json with metadata about each dataset', 'Document any issues or deviations from plan'], 'verification': 'Summary file created, statistics computed'}], 'phase_4_fallback_strategies': [{'scenario': 'HuggingFace dataset unavailable or too large', 'solution': 'Use direct download URL, sample aggressively, or use alternative source (Kaggle, UCI, etc.)'}, {'scenario': 'Insufficient near-duplicate ground truth', 'solution': 'Create synthetic near-duplicates by introducing controlled modifications to existing documents (word deletion, substitution, insertion)'}, {'scenario': 'Tokenization library unavailable', 'solution': "Use simple regex-based tokenization: re.findall(r'\\w+', text.lower())"}, {'scenario': 'Total size exceeds 300MB', 'solution': 'Sample more aggressively, reduce target_samples, or exclude largest dataset'}, {'scenario': 'Dataset has no obvious duplicate structure', 'solution': 'Use clustering on token overlap to create pseudo-duplicate pairs, or focus on Jaccard estimation rather than duplicate detection'}], 'tools_and_skills_to_use': ['aii-hf-datasets: Search, preview, download HuggingFace datasets', 'aii-json: Validate output schema, create mini/preview variants', 'aii-web-tools: Search for alternative dataset sources, verify URLs', 'Python standard library: json, re, random for preprocessing', 'sklearn: For 20 newsgroups dataset (if not using HF)', 'datasets (HuggingFace): Main dataset loading library'], 'expected_outputs': ['data_out.json: Main output file with all datasets in common schema', 'data_out_preview.json: 3 truncated samples for quick inspection', 'data_out_mini.json: 3-5 full samples for development', 'dataset_summary.json: Statistics and metadata about collected datasets', 'preprocessing_script.py: Reusable script for dataset conversion']} is not of type 'string'
  - at `ideal_dataset_criteria`: {'content_requirements': ['Text documents that can be represented as sets of tokens or shingles', 'Known near-duplicate pairs or clusters (ground truth labels)', 'Diverse Jaccard similarity distributions - some datasets with high similarity (near-duplicates), some with low similarity (dissimilar items)', 'Varying document lengths - from short texts (questions, sentences) to long documents', 'Both synthetic and real-world data to validate different aspects of the algorithm'], 'format_requirements': ['Must be convertible to JSON format with schema: {id, text/tokens, metadata}', 'For duplicate detection evaluation: include duplicate_id or cluster_id field', 'For Jaccard estimation evaluation: sets should be representable as token sets or k-shingles', 'Support creation of mini (3-5 samples) and preview (truncated) variants'], 'size_constraints': ['Total processed size under 300MB (all datasets combined)', 'Individual datasets: 10MB-100MB range ideal for meaningful evaluation', 'Must support sampling - can extract subsets from larger datasets like The Pile or C4'], 'technical_requirements': ['Accessible via HuggingFace Hub, direct download URL, or standard Python libraries (sklearn.datasets, etc.)', 'Well-documented format and schema', "Stable URLs or dataset IDs that won't change"]} is not of type 'string'
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
