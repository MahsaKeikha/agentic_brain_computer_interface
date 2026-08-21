# Agentic Brain Computer Interface

F67 in the Agentic AI Library.

A standalone multi-agent engineering and research workflow for BCI requirements, signal acquisition planning, decoding pipeline design, calibration planning, performance evaluation, safety review, and human oversight.

This repository does not authorize clinical use or autonomous control of consequential systems.

## Core agents

- [`requirements_agent.py`](AGENTS/requirements_agent.py)
- [`signal_acquisition_agent.py`](AGENTS/signal_acquisition_agent.py)
- [`decoder_design_agent.py`](AGENTS/decoder_design_agent.py)
- [`calibration_agent.py`](AGENTS/calibration_agent.py)
- [`performance_safety_agent.py`](AGENTS/performance_safety_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
