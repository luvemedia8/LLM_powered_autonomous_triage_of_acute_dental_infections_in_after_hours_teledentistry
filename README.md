# LLM-powered autonomous triage of acute dental infections in after-hours teledentistry

This repository contains ADAPT, a six-agent orchestration system for five-level after-hours dental emergency triage. The pipeline separates intake structuring, guideline-grounded triage, independent safety review, disagreement resolution, patient communication, and audit logging. The Safety Agent applies asymmetric authority: a credible safety concern escalates the decision, while de-escalation requires agreement.

## Installation

Python 3.11 is required.

```bash
python3.11 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Conda users can run `conda env create -f environment.yml`. The container image can be built with `docker build -t adapt-teledentistry .`.

## Data

Verified source locations are listed in `datasets.txt`. ADA, AAPD, AAE, and IADT materials remain subject to their publishers' terms. The 500 standardised scenarios and gold ADSI labels are described in the manuscript as awaiting public deposition and are therefore not included or fabricated here. The pipeline accepts JSON, JSONL, or CSV records after release. No patient records are used.

Each JSONL row must contain `case_id` and `narrative`; optional fields are `age_years`, `symptoms`, `duration_hours`, `anatomical_locations`, `medications`, `comorbidities`, and `vitals`. Run `adapt validate-data cases.jsonl` before evaluation.

## Configuration

`configs/main.yaml` records the reported setup: GPT-4o for triage, Claude Sonnet 4 for safety review, DeepSeek R1 for disagreement resolution, temperature 0.0, 4,096 maximum output tokens, Safety Agent escalation threshold 0.3, seeds 42, 123, and 256, and 10,000 stratified bootstrap iterations.

The paper reports commercial API inference rather than custom training or fine-tuning. GPU count, batch size, learning rate, epochs, precision, and storage are consequently not applicable. API credentials are read from `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and `DEEPSEEK_API_KEY`. Do not place credentials in configuration files or audit logs.

## Evaluation

The evaluation modules provide five-class accuracy, linearly weighted Cohen's kappa, macro one-vs-rest AUC, high-acuity undertriage, Level 5 critical miss rate, overtriage, inter-agent disagreement, expected calibration error, stratified bootstrap intervals, McNemar comparisons, Holm correction, Cohen's h, input perturbations, and selective deferral frontiers.

The reported main evaluation uses 500 scenarios divided into ten stratified groups of 50 and three runs. Expected manuscript values are 93.2% accuracy, weighted kappa 0.889, macro-AUC 0.966, 3.3% undertriage, 1.2% critical misses, 15.8% safety overrides, 8.2% escalation activation, and disagreement AUC 0.82. These values are reference targets, not embedded outputs. Exact verification requires the released scenario set and access to the dated model endpoints.

## Operational safety

ADAPT is research software and is not a medical device. It must not be used as the sole basis for patient care. Non-overridable airway and haemorrhage triggers are preserved in deterministic safeguards, but remote text triage cannot replace physical examination. Audit records contain hashes and model metadata; raw narratives are excluded from the ledger.

## Project layout

The `code/adapt_teledentistry` package contains clinical schemas, ADSI criteria, intake parsing, retrieval, model providers, specialised agents, pipeline orchestration, audit storage, baselines, metrics, statistical comparisons, perturbation analysis, deferral analysis, and the command interface. `configs` contains the reported experiment settings. `datasets.txt` is the single registry of external data and guideline locations.

## License

Software is released under the MIT License. External guidelines, model APIs, and future scenario deposits retain their own terms.
