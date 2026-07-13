# QA Engineer Portfolio — SQL, Database Testing & Agile QA Workflows

![Project Status](https://img.shields.io/badge/status-In%20Progress-blue)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A hands-on portfolio project demonstrating SQL proficiency, database testing methodology, and Agile QA practices — built by simulating the day-to-day work of a QA Engineer on a software team, rather than completing isolated tutorial exercises.

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
├── leetcode/                # SQL problem-solving practice
├── portfolio/               # Polished, portfolio-ready deliverables
├── sprint-workbooks/        # Daily checklists per sprint (goals, tasks, Jira IDs, reflections)
│   └── sprint-00/
│       └── day-01.md
├── sql/                     # SQL practice organized by concept (joins, subqueries, window functions, etc.)
└── test-cases/               # Written QA test cases
```

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

Work is organized into 12 Agile sprints, each producing a reviewable deliverable.

| Sprint    | Focus                                     |
| --------- | ------------------------------------------ |
| Sprint 0  | Project setup & planning                    |
| Sprint 1  | SQL fundamentals                            |
| Sprint 2  | Filtering & aggregation                     |
| Sprint 3  | SQL joins                                   |
| Sprint 4  | Advanced joins & reporting                  |
| Sprint 5  | Subqueries                                  |
| Sprint 6  | Window functions                            |
| Sprint 7  | CTEs & date functions                       |
| Sprint 8  | Database validation                         |
| Sprint 9  | Bug investigation                           |
| Sprint 10 | Reporting & QA scenarios                     |
| Sprint 11 | Portfolio polish & interview preparation     |

---

## QA Focus Areas

This project is built around the SQL skills QA Engineers use most in practice:

* Data integrity validation
* Referential integrity checks
* Duplicate record detection
* Missing data validation
* Business rule verification
* Reporting validation
* Root cause investigation
* Regression testing with SQL

---

## Current Status

**Sprint 0 — Project Initialization** (in progress)

- [x] Environment setup
- [ ] Database setup
- [ ] Schema exploration
- [ ] Jira project planning
- [ ] Repository organization
- [ ] QA documentation foundation
- [ ] Sprint 0 review

This repository is under active development, with new sprints, SQL work, and QA deliverables committed regularly. Check back for updates, or see the [Project Roadmap](#project-roadmap) above for what's coming next.

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