# Payment Rules

This sample repository is used for testing an Agentic PR Review tool.

## Business Rules

1. Payment amount must be greater than zero.
2. If no coupon is provided, final amount should equal the original amount.
3. A valid coupon should reduce the payment amount by `discount_amount`.
4. An expired coupon should not apply any discount.
5. Final payment amount should never go below zero.

## Review Scenarios

This repo is intentionally small so that test pull requests can be created easily.
Useful PR scenarios:

- Docs-only change
- Business logic change with missing tests
- Coupon validation bug
- Good PR with complete tests
- Configuration or dependency change
