# Sample Payment Service

A small Python repository for testing an Agentic PR Review & Code Quality Orchestrator.

This is not a production payment system. It is intentionally simple so that pull requests can be reviewed by an AI PR review workflow.

## Features

- Payment amount validation
- Coupon discount model
- Discount policy
- Payment final amount calculation
- Basic pytest test suite

## Business Rules

1. Amount must be greater than zero.
2. No coupon means no discount.
3. Valid coupon applies discount.
4. Expired coupon does not apply discount.
5. Final amount cannot go below zero.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
python -m pip install -e ".[dev]"
pytest
```

## Run Example

```bash
python -m app.main
```

## Why this repo exists

This repository is used as the target repo for creating sample PRs. The Agentic PR Review Orchestrator will fetch PR diffs from this repo and review them.
