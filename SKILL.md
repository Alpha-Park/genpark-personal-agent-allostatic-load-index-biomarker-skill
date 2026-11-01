---
name: genpark-personal-agent-allostatic-load-index-biomarker-skill
version: "1.0.0"
description: "Zero-dependency Bruce McEwen multi-system physiological wear-and-tear indexer, cardiometabolic-neuroendocrine strain evaluator, and allostatic recovery modeler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Allostatic Load Index Biomarker Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI health agents to quantify the cumulative physiological wear-and-tear of chronic stress using the Bruce McEwen and Teresa Seeman Allostatic Load (AL) multi-system clinical paradigm.

## Agent In-Context Capabilities

- **Multisystem Stress Quantification**: Synthesizes 10 clinical biomarkers spanning cardiovascular, metabolic, inflammatory, and neuroendocrine subsystems into a unified 0-10 index.
- **Vulnerability Partitioning**: Pinpoints the single most dysregulated physiological subsystem to guide high-leverage lifestyle interventions.
- **Recovery Trajectory Modeling**: Forecasts multi-week allostatic de-escalation under targeted behavioral interventions.

## Tools Summary

1. `calculate_allostatic_load_index`: Evaluates biomarker panel, computes AL index, and identifies primary subsystem vulnerability.
2. `simulate_allostatic_recovery_trajectory`: Projects 12-week recovery curve under targeted lifestyle protocols.
