# Project Charter

## Project Name
QA Engineer Portfolio — SQL, Database Testing & Agile QA Workflows

## Purpose
This project exists to demonstrate, through real deliverables rather than isolated exercises, the core skills a QA Engineer applies day to day: SQL proficiency, database testing, defect investigation, and Agile process discipline. It simulates the role of a QA Engineer embedded on a software team working against a live application database.

## Background
Traditional SQL courses teach syntax in isolation. This project instead builds and tests a realistic e-commerce database — customers, orders, products, inventory, payments, shipments, and reviews — so every SQL concept learned is immediately applied to a QA task: writing a validation query, investigating a simulated defect, or documenting a test case.

## Objectives
* Build working fluency in SQL, from fundamentals through joins, subqueries, window functions, and CTEs.
* Design and populate a realistic sample database to serve as a consistent testing target.
* Apply SQL to core QA activities: data integrity validation, referential integrity checks, business rule verification, and defect root-cause analysis.
* Practice Agile delivery using Jira — sprint planning, tracking, and retrospectives.
* Produce a portfolio of reviewable artifacts (queries, test cases, bug reports, documentation) suitable for sharing with hiring teams.

## Scope

**In scope:**
* SQL practice and application against the project's sample database
* Data validation queries covering the schema's documented business rules
* Simulated bug investigations with root-cause analysis
* QA test case documentation
* Sprint-based planning and tracking in Jira
* Portfolio documentation (README, schema overview, sprint reviews)

**Out of scope (for now):**
* Production or live-system testing
* Automated UI/API test frameworks (tracked separately under Future Enhancements)
* Performance/load testing

## Deliverables
| Deliverable                  | Location            |
| ----------------------------- | -------------------- |
| Sample database (schema + seed data) | `database/`      |
| Schema documentation & ER diagram    | `database/docs/` |
| SQL practice by concept              | `sql/`            |
| Data validation queries              | `validation/`     |
| Bug investigation reports             | `bug-investigations/` |
| QA test cases                         | `test-cases/`     |
| Sprint workbooks & reviews            | `sprint-workbooks/`, `docs/` |
| Portfolio-ready summaries             | `portfolio/`      |

## Timeline
The project runs across 12 Agile sprints (Sprint 0 through Sprint 11), moving from environment setup and SQL fundamentals through advanced SQL, database validation, bug investigation, and finally portfolio polish and interview preparation. See the README's Project Roadmap for the full sprint breakdown.

## Tools
MySQL, MySQL Workbench / DBeaver, Jira, Git/GitHub, VS Code.

## Success Criteria
* All 12 sprints completed with a corresponding sprint review and retrospective.
* Validation queries and test cases cover every documented business rule in the schema.
* At least one full bug investigation report demonstrating root-cause analysis via SQL.
* Repository is organized, documented, and reviewable by a hiring manager without additional explanation.

## Owner
This project is authored and maintained by a single contributor, acting as both developer and QA Engineer for the purposes of this simulation.
