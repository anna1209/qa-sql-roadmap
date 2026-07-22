# Test Cases — Customer Management Module

Test cases for validating data integrity and schema constraints on the `customers` and `addresses` tables. For live execution tracking with status dropdowns and auto-calculated pass rate, see [`customer_management_test_cases.xlsx`](./customer_management_test_cases.xlsx).

## Summary

| ID | Scenario | Priority | Type |
|---|---|---|---|
| [TC-CM-001](#tc-cm-001) | Total customer count | Medium | Functional |
| [TC-CM-002](#tc-cm-002) | Total address count | Medium | Functional |
| [TC-CM-003](#tc-cm-003) | Every customer has an address | High | Data Integrity |
| [TC-CM-004](#tc-cm-004) | No orphaned addresses | High | Data Integrity |
| [TC-CM-005](#tc-cm-005) | Customer can have more than one address | Medium | Functional |
| [TC-CM-006](#tc-cm-006) | Nullable columns — customers | Medium | Schema |
| [TC-CM-007](#tc-cm-007) | Nullable columns — addresses | Medium | Schema |
| [TC-CM-008-a](#tc-cm-008) | NULLs in critical fields — customer | High | Data Quality |
| [TC-CM-008-b](#tc-cm-008) | NULLs in critical fields — addresses | High | Data Quality |
| [TC-CM-009](#tc-cm-009) | Constraints — customers  | Medium | Schema |
| [TC-CM-010](#tc-cm-010) | Constraints — addresses | Medium | Schema |
| [TC-CM-011](#tc-cm-011) | FK rejects invalid customer_id | High | Negative |
| [TC-CM-012](#tc-cm-012) | UNIQUE rejects duplicate email | High | Negative |
| [TC-CM-013](#tc-cm-013) | NOT NULL rejects missing email | High | Negative |

---

## Row Count Validation

### TC-CM-001
**Verify total customer count**

| Field | Detail |
|---|---|
| Preconditions | Database is accessible; `customers` table exists |
| Priority / Type | Medium / Functional |
| Expected Result | Actual count matches expected baseline and is greater than 0 |

**Steps**
1. Connect to database
2. Run count query
3. Compare against expected baseline

```sql
SELECT COUNT(*) AS Customer_count FROM customers;
```

### TC-CM-002
**Verify total address count**

| Field | Detail |
|---|---|
| Preconditions | Database is accessible; `addresses` table exists |
| Priority / Type | Medium / Functional |
| Expected Result | Actual count matches expected baseline and is greater than 0 |

**Steps**
1. Connect to database
2. Run count query
3. Compare against expected baseline

```sql
SELECT COUNT(*) AS Address_count FROM addresses;
```

### TC-CM-003
**Verify every customer has at least one associated address**

| Field | Detail |
|---|---|
| Preconditions | Database is accessible; `customers` &`addresses` table exists |
| Priority / Type | HIGH / Data Integrity |
| Expected Result | 0 rows returned (no customers without an address) |

**Steps**
1. Connect to database
2. Run not exits query
3. Check returned result

```sql
SELECT c.customer_id FROM customers c
WHERE NOT EXISTS(
    SELECT * 
    FROM addresses a 
    WHERE a.customer_id = c.customer_id
);
```

### TC-CM-004
**Verify no addresses without a valid customer**

| Field | Detail |
|---|---|
| Preconditions | Database is accessible; `customers` &`addresses` table exists |
| Priority / Type | HIGH / Data Integrity |
| Expected Result | 0 rows returned ( No orphaned addresses) |

**Steps**
1. Connect to database
2. Run not exits query
3. Check returned result

```sql
SELECT a.address_id, a.customer_id
FROM addresses a
WHERE NOT EXISTS (
    SELECT *
    FROM customers c
    WHERE c.customer_id = a.customer_id
);
```
### TC-CM-005
**Verify a customer can have more than one address**

| Field | Detail |
|---|---|
| Preconditions | 	Business rule confirms multiple addresses per customer are permitted |
| Priority / Type | Medium / Functional |
| Expected Result | Insert succeeds with no constraint violation; addresses table contains 2+ rows for that customer_id |

**Steps**
1. Select one existing customer_id
2. Insert a new address record for that customer
3. Verify Insert succeeds
4. Rollback

```sql
INSERT INTO addresses (customer_id, address_type, address_line_1, address_line_2, city, state, postal_code, country, is_default)
VALUES ('1', 'shipping', '123 test st', 'apt 123', 'Atlanta','GA', '12345', 'USA', '0');
```

### TC-CM-006

**List nullable columns in the customers table and compare against data dictionary**

| Field | Detail |
|---|---|
| Preconditions | Access to `schema-overview` |
| Priority / Type | Medium / Schema |
| Expected Result | Nullability matches documented schema with no discrepancies |

**Steps**
1. Query `information_schema.columns` for `customers` table
2. Compare nullability to  data dictionary

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'shopsmart_test' AND TABLE_NAME = 'customers';
```

### TC-CM-007

**List nullable columns in the addresses table and compare against data dictionary**

| Field | Detail |
|---|---|
| Preconditions | Access to `schema-overview` |
| Priority / Type | Medium / Schema |
| Expected Result | Nullability matches documented schema with no discrepancies |

**Steps**
1. Query `information_schema.columns` for `addresses` table
2. Compare nullability to  data dictionary

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'shopsmart_test' AND TABLE_NAME = 'addresses';
```


## Data Quality

### TC-CM-008-a
**Detect unexpected NULLs in business-critical customer fields**

| Field | Detail |
|---|---|
| Preconditions | `customers` table populated |
| Priority / Type | High / Data Quality |
| Expected Result | 0 rows returned |

**Steps**
1. Query customers where `email`, `first_name`, or `last_name IS NULL`
2. Review result set
```sql
SELECT customer_id, first_name, last_name, email
FROM customers
WHERE first_name IS NULL OR last_name IS NULL OR email IS NULL;
```
### TC-CM-008-b
**Detect unexpected NULLs in business-critical address fields**

| Field | Detail |
|---|---|
| Preconditions | `addresses` table populated |
| Priority / Type | High / Data Quality |
| Expected Result | 0 rows returned |

**Steps**
1. Query customers where `customer_id` or `address_line_1` IS NULL
2. Review result set
```sql
SELECT address_id, customer_id, address_line_1
FROM addresses
WHERE customer_id IS NULL OR address_line_1 IS NULL;
```

## Constraint Validation

### TC-CM-009
**Enumerate all constraints defined on the customers table**

| Field | Detail |
|---|---|
| Preconditions | Access to `information_schema` |
| Priority / Type | Medium / Schema |
| Expected Result | All expected constraints present (PK, UNIQUE); no missing or extra constraints |

**Steps**
1. Query `information_schema.KEY_COLUMN_USAGE` for `customers`
2. Compare against design
```sql
SELECT column_name, constraint_name
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'shopsmart_test' AND TABLE_NAME = 'customers';
```

### TC-CM-010
**Enumerate all constraints defined on the addresses table**

| Field | Detail |
|---|---|
| Preconditions | Access to `information_schema` |
| Priority / Type | Medium / Schema |
| Expected Result | All expected constraints present (PK, FK); no missing or extra constraints |

**Steps**
1. Query `information_schema.KEY_COLUMN_USAGE` for `addresses`
2. Compare against design

```sql
SELECT column_name, constraint_name
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'shopsmart_test' AND TABLE_NAME = 'addresses';
```

### TC-CM-011
**Verify foreign key constraint rejects an address referencing a non-existent customer**

| Field | Detail |
|---|---|
| Preconditions | FK constraint defined on `addresses.customer_id` |
| Priority / Type | High / Negative |
| Expected Result | Insert fails with FK constraint violation error |

**Steps**
1. Attempt INSERT into addresses with invalid `customer_id`
2. Observe result
3. `ROLLBACK` if Insert succeed

```sql
INSERT INTO addresses (address_id, customer_id, street, city, state, zip)
VALUES (99999, -1, 'Test St', 'Test City', 'TS', '00000');
```

### TC-CM-012
**Verify UNIQUE constraint rejects a duplicate customer email**

| Field | Detail |
|---|---|
| Preconditions | UNIQUE constraint defined on `customers.email` |
| Priority / Type | High / Negative |
| Expected Result | Insert fails with UNIQUE constraint violation error |

**Steps**
1. Attempt INSERT using an existing email
2. Observe result
3. `ROLLBACK` if Insert succeed

```sql
INSERT INTO customers (customer_id, email, first_name, last_name)
VALUES (999, 'michelle.james5@yahoo.com', 'Test', 'User');
```

### TC-CM-013
**Verify NOT NULL constraint rejects a customer insert missing a required field**

| Field | Detail |
|---|---|
| Preconditions | NOT NULL constraint defined on `customers.email`|
| Priority / Type | High / Negative |
| Expected Result | Insert fails with NOT NULL constraint violation error |

**Steps**
1. Attempt INSERT omitting required email field
2. Observe result
3. `ROLLBACK` if Insert succeed

```sql
INSERT INTO customers (customer_id, first_name, last_name)
VALUES (999, 'Test', 'User');
```
---

*Execution results (Actual Result, Status, Executed By, Defect ID) are tracked in [`customer_management_test_cases.xlsx`](./customer_management_test_cases.xlsx) and summarized in [`test_summary_report.md`](./test_summary_report.md) after each test cycle.*
