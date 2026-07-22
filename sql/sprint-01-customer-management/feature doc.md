
# Feature Name: Customer Management

Status: Ready for QA

Release: v1.0.0

Priority: High

Background: The development team has completed the Customer Management feature.

## Customers can:
* Register an account
* Search for existing customers
* View customer profiles
* Maintain multiple addresses

Before the feature can be released, QA must verify both the application behavior and the underlying database.

## Business Requirements
| ID     | Requirement                                                                      |
| ------ | -------------------------------------------------------------------------------- |
| BR-001 | Email address must be unique.                                                    |
| BR-002 | First name is required.                                                          |
| BR-003 | Last name is required.                                                           |
| BR-004 | Account status defaults to ACTIVE.                                               |
| BR-005 | `created_at` is automatically populated.                                         |
| BR-006 | Customers are soft deleted (`is_deleted = TRUE`) rather than physically removed. |

## Address Management
| ID     | Requirement                                            |
| ------ | ------------------------------------------------------ |
| BR-007 | A customer may have multiple addresses.                |
| BR-008 | Every address must belong to an existing customer.     |
| BR-009 | A customer may have only one default SHIPPING address. |
| BR-010 | Address type must be SHIPPING or BILLING.              |
