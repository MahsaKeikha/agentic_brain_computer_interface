# Agentic Brain Computer Interface

**F67 | L3 Gold Standard | v1.0**

A governed multi-agent engineering and research workflow for BCI requirements, signal acquisition planning, decoder design, calibration, performance and safety review, and qualified human oversight.

This repository supports research and engineering. It does not authorize clinical use, stimulation, implants, treatment decisions, patient-specific control parameters, or autonomous control of consequential external systems.

## Core agents

- [`requirements_agent.py`](AGENTS/requirements_agent.py)
- [`signal_acquisition_agent.py`](AGENTS/signal_acquisition_agent.py)
- [`decoder_design_agent.py`](AGENTS/decoder_design_agent.py)
- [`calibration_agent.py`](AGENTS/calibration_agent.py)
- [`performance_safety_agent.py`](AGENTS/performance_safety_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Gold-standard governance

The orchestration layer executes all six specialists and then applies a fail-closed BCI control gate. Required reviews include signal provenance, acquisition quality, decoder validation, calibration, performance safety, false-activation risk, privacy, cybersecurity, and qualified human approval.

The gate also blocks poor signal quality, unvalidated decoders, invalid calibration, high or unbounded false-activation risk, unreviewed invasive interfaces, human-subject use without ethics approval, consequential autonomous control, external-device control authorization, stimulation authorization, implant authorization, clinical authorization, treatment decisions, and patient-specific control parameters.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and executes correctness-focused Ruff checks, pytest, the held-out governance suite, the example workflow, and the smoke run.

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
