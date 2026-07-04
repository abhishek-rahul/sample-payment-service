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

## PR Review Testing Scenarios

This repository is also used to test an Agentic PR Review workflow.

Recommended sample PR categories:

1. Documentation-only change
2. Business logic change without matching tests
3. Coupon validation bug
4. Good change with proper tests

The PR review workflow should treat documentation-only changes as low risk and should not report unrelated legacy code issues.
