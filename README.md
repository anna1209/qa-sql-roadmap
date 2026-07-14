# QA Engineer Portfolio — SQL, Database Testing & Agile QA Workflows

![Project Status](https://img.shields.io/badge/status-In%20Progress-blue)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A simulated QA project for a fictional e-commerce application,
demonstrating how a QA Engineer validates data,
creates test cases,
investigates defects,
and uses SQL throughout the software testing lifecycle.

---

## What This Project Demonstrates

* **SQL fluency**: fundamentals through joins, subqueries, window functions, CTEs, and date functions
* **Database design**: a custom, AI-generated sample database (schema, seed data) built from scratch to serve as a realistic testing target, rather than relying on a pre-built dataset
* **Database testing**: data integrity checks, referential integrity validation, duplicate/missing-data detection, business rule verification
* **Defect investigation**: root-cause analysis using SQL against a realistic schema
* **QA documentation**: test cases, bug reports, and validation queries written to industry standards
* **Agile process**: sprint planning and tracking in Jira, with sprint reviews and retrospectives committed alongside the code

Each item below links out once the corresponding work is committed, so this repo can be reviewed section by section rather than read start to finish.

---

## Repository Structure

```text
qa-engineer-portfolio-bootcamp/
│
├── bug-investigations/     # Simulated defect investigations with root-cause analysis
├── database/                # AI-generated sample database
│   ├── docs/                  # Schema overview, table reference, business rules, ER diagram
│   ├── schema/                # SQL scripts to create the database schema
│   └── seed-data/             # SQL scripts to populate sample data
│   └── checks/                # Sanity-check queries confirming the database was built correctly
├── docs/                   # Project charter, test strategy, and templates used across project
│   ├── project-charter.md
│   ├── test-strategy.md
│   └── templates/
│       └── daily-template.md
├── portfolio/               # Polished, portfolio-ready deliverables
│   ├──  sql-validation-report.md
│   └── customer-data-validation.md
├── sprint-workbooks/        # Daily checklists per sprint (goals, tasks, Jira IDs, reflections)
│   ├──  sprint-00/
│       └── setupo-progress.md
│   └── sprint-01/
│       └── sprint-01-progress.md
├── sql/                     # SQL practice organized by sprint/feature (joins, subqueries, window functions, etc.)
│   ├── sprint-01-customer-management/
│   ├── sprint-02-product-catalog/
│   ├── sprint-03-order-management/
│   ├── sprint-04-payment-processing/
│   ├── sprint-05-inventory-management/
│   └── sprint-06-reporting-analytics/
└── test-cases/               # Written QA test cases, organized by sprint/feature
│   ├── sprint-01-customer-management/
│   ├── sprint-02-product-catalog/
│   ├── sprint-03-order-management/
│   ├── sprint-04-payment-processing/
│   ├── sprint-05-inventory-management/
│   └── sprint-06-reporting-analytics/
```

> **Note:** `sprint-04` through `sprint-06` folders are named here to lock in the convention ahead of time; they'll be added to the repo as those sprints begin.

---

## Technology Stack

| Tool                      | Purpose                         |
| ------------------------- | -------------------------------- |
| MySQL                     | Database                         |
| MySQL Workbench / DBeaver | SQL client                       |
| Jira                      | Agile project management         |
| Git / GitHub               | Version control & portfolio host |
| VS Code                   | Documentation & SQL development  |

---

## Project Roadmap

This roadmap tracks the sprint-by-sprint development of the ShopSmart database portfolio project, structured to mirror a real Agile QA workflow — from environment setup through production-style bug investigation and final portfolio polish.

Each sprint builds on the SQL concepts from the previous one while introducing a distinct category of QA activity, so the project demonstrates range rather than repeating the same type of validation each time.

| Sprint | Feature | Primary SQL Topics | QA Focus | Sprint Artifacts |
|---|---|---|---|---|
| **Sprint 0** | Project Setup | — | Environment setup, GitHub/Jira configuration, ShopSmart database deployment and verification | Test strategy draft, environment setup checklist, Jira board configured with epics/backlog |
| **Sprint 1** | Customer Management | SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, LIKE, IS NULL | Boundary and negative testing — empty strings, NULL emails, duplicate customers, malformed input | Test cases (customer validation), 1–2 logged defects, sprint retro note |
| **Sprint 2** | Product Catalog | GROUP BY, COUNT, SUM, AVG, HAVING | Data quality checks — orphaned products, negative prices, inconsistent category assignments | Data quality test suite, defect log entries, sprint retro note |
| **Sprint 3** | Order Management | JOINs, multi-table queries | End-to-end order validation across customer, product, and order tables; referential integrity checks | Traceability matrix (stories → test cases), test case doc, sprint retro note |
| **Sprint 4** | Payment Processing | Subqueries, EXISTS, IN | Financial validation — reconciliation totals, rounding errors, failed/partial transaction states | Reconciliation test cases, defect log, sprint retro note |
| **Sprint 5** | Inventory Management | CTEs, CASE, COALESCE | Inventory reconciliation — recorded stock vs. actual stock, negative/impossible quantities | Reconciliation report, defect log, sprint retro note |
| **Sprint 6** | Reporting & Analytics | Window Functions, ranking, running totals | Report validation and regression testing against earlier sprint data | Regression test suite, test summary report (interim), sprint retro note |
| **Sprint 7** | Production Bug Investigation | All SQL concepts | Root cause analysis on injected/discovered defects, formal QA defect reporting | Defect investigation write-up, RCA doc, final test summary report |
| **Sprint 8** | Portfolio & Interview Prep | Review and optimization | Documentation review, portfolio polish, interview talking points | Final README/docs pass, polished repo structure, interview prep notes |

### Notes on Sequencing

Order Management (Sprint 3) is intentionally sequenced before Inventory Management (Sprint 5), even though in a live system order placement typically depends on inventory checks. This ordering follows SQL topic progression (JOINs before CTEs) rather than strict domain dependency — Sprint 5's reconciliation work revisits and validates the order data introduced in Sprint 3.

### Sprint Cadence

Each sprint closes with three deliverables, consistent across the project:
1. A test case or validation document specific to that sprint's feature
2. At least one logged defect or data quality finding (even if minor) — see [`docs/test-strategy.md`](docs/test-strategy.md) for defect severity conventions
3. A short retrospective note capturing what was learned or what would be done differently

This cadence is what ties the Jira board, commit history, and documentation together into a coherent story rather than a static set of deliverables.

---

## Current Status

### Sprint 0 — Completed ✅

- [x] Development environment configured
- [x] GitHub repository initialized
- [x] ShopSmart database created
- [x] Sample data imported
- [x] Database verification completed
- [x] Jira project configured
- [x] Repository structure established

---

### Sprint 1 — In Progress 🚧

Current Feature:

Customer Management

Working on:

- Business requirements review
- SQL validation queries
- Customer Registration test cases

---

## Planned Enhancements

* Automated SQL validation scripts
* API testing examples
* Playwright-based database validation scenarios
* CI/CD integration
* Additional sample databases and interview exercises

---

## License

MIT License.

## About Me

I'm a QA Engineer building this project to demonstrate practical SQL skills, database testing methodology, and Agile QA workflows against a realistic application dataset. Feedback and suggestions are welcome — feel free to open an issue.