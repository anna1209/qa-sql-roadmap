# Test Strategy

## Purpose
This document defines the approach used to validate data quality and business rule compliance in the project's sample database. It applies to all validation queries, test cases, and bug investigations produced throughout the project.

## Objectives
* Verify that the database enforces the business rules defined in `database/docs/schema-overview.md`.
* Detect data integrity issues: missing data, duplicate records, orphaned foreign keys, and constraint violations.
* Validate that derived/aggregate values (e.g. order totals, payment amounts) are calculated correctly.
* Document and investigate any defects found, including root cause.

## Scope

**In scope:**
* All tables in the sample database: `customers`, `addresses`, `categories`, `products`, `inventory`, `orders`, `order_items`, `payments`, `shipments`, `reviews`.
* Data integrity and referential integrity between related tables.
* Business rule verification, as documented per entity in the schema overview.
* Regression checks after schema or seed-data changes.

**Out of scope:**
* Application/UI-level testing (no application layer exists in this project).
* Performance and load testing.
* Security/penetration testing.

## Test Data & Environment Strategy
### Environment Separation
Testing runs against an isolated copy so that schema validation and negative tests can be performed freely without risking the source dataset.

| Environment | Purpose | Access |
|---|---|---|
| Source / Primary | The AI-generated sample dataset used as the canonical schema + data | Read-only reference |
| Test (`shopsmart_test`) | Local copy restored from a schema+data dump, used for all test execution | Full read/write, disposable |

This mirrors real-world `dev → test/QA → staging → production` separation, scaled down to fit a single-developer portfolio project.

### Setting Up the Test Environment

```
bash setup_test_db.sh
```

All test cases are run against `shopsmart_test`, not `shopsmart`. If the test schema drifts or gets corrupted by a failed test, it's dropped and re-restored from the dump — cheap and disposable by design.

### Transactions for Destructive Tests

For negative/constraint tests that intentionally attempt an invalid insert (e.g., TC-CM-005a, TC-CM-011, TC-CM-012, TC-CM-013), each test is wrapped in a transaction and rolled back regardless of outcome.


### Why This Matters

- **Isolation** — a failed or buggy test case can't corrupt data other tests depend on.
- **Repeatability** — the test schema can be torn down and rebuilt from the dump at any time, giving every test run a known starting state.
- **Honesty in reporting** — test results reflect the schema's actual constraint enforcement, not artifacts of leftover test data from a previous run.

## Test Levels

| Level                     | What it checks                                                        |
| -------------------------- | ------------------------------------------------------------------------ |
| Data integrity             | Nulls, uniqueness (e.g. customer email, product SKU), format/type validity |
| Referential integrity      | Foreign keys resolve correctly (e.g. every `order_items.order_id` exists in `orders`) |
| Business rule verification | Rules such as "order total = sum(order_items)" or "ship date >= order date" |
| Regression                 | Re-running prior validation queries after schema/data changes to confirm no new violations |

## Test Case Design
Each test case documented in `test-cases/` follows a consistent format: objective, preconditions, SQL query, expected result, actual result, and pass/fail status. Test cases are traced back to the specific business rule they validate wherever possible.

## Defect Management
Issues found during validation are logged as bug investigations in `bug-investigations/`, each including:
* A description of the discrepancy and the query that surfaced it
* Root-cause analysis
* Affected table(s) and business rule violated
* Corresponding Jira issue ID for tracking

## Entry Criteria
* Sample database schema and seed data are loaded and accessible.
* Business rules for the relevant entity are documented.

## Exit Criteria
* All documented business rules have at least one corresponding validation query.
* All identified defects are logged with root-cause analysis.
* Validation queries are re-run and pass after any schema or seed-data changes (regression).

## Tools
MySQL / MySQL Workbench / DBeaver for query execution; Jira for defect and task tracking; GitHub for version control of all validation queries, test cases, and reports.
