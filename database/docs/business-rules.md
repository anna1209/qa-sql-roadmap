# Business Rules

This document defines the business rules enforced (or intended to be enforced) across the sample e-commerce database.

Each rule is written to be independently testable — most map to a single SQL check (constraint, uniqueness query, referential integrity check, or cross-table reconciliation).

---

## Customers

* Email must be unique.
* Customer cannot be deleted (soft delete only), to preserve referential integrity for historical orders, payments, and reviews.
* Customer may have multiple addresses.
* Customer must have at least one address on file before placing an order.

## Addresses

* Every address must belong to exactly one customer.
* A customer may designate one address as default shipping and one as default billing — never more than one of each.
* An address used on a past order should not be hard-deleted, as this would orphan shipment records; a soft delete or archival flag is preferred.

## Categories

* Category name must be unique.
* A category may contain zero or more products.

## Products

* SKU must be unique.
* Price must be greater than zero.
* Product belongs to exactly one category.
* A product should not be hard-deleted once it has been referenced by an order item; soft delete (e.g. `is_active` flag) preserves order history integrity.

## Inventory

* Quantity >= 0
* Reorder level >= 0
* Every product has exactly one corresponding inventory record — inventory cannot exist without a product, and a product should not exist without an inventory record.
* An order should only be permitted to complete if inventory quantity is sufficient at the time of purchase.
* Inventory quantity should decrement when an order is placed/paid, and increment when an order is cancelled.

## Orders

* Must contain at least one order item.
* Total amount equals `sum(order_items)`.
* Status values: `Pending`, `Paid`, `Shipped`, `Cancelled`.
* Every order must belong to exactly one customer.
* Status should progress in a defined sequence (`Pending → Paid → Shipped`); `Cancelled` may occur from `Pending` or `Paid` but not after `Shipped`.
* An order cannot move to `Shipped` unless its associated payment status is `Completed`.

## Order Items

* Every order item must reference a valid product.
* Quantity must be a positive integer (no zero or negative values).
* Unit price on the order item should reflect the product's price at the time of purchase, not a live lookup — this preserves historical accuracy if product prices change later.
* A given product should appear at most once per order (quantity should be incremented rather than duplicated as separate rows).

## Payments

* Amount = Order Total
* Status values: `Pending`, `Completed`, `Failed`, `Refunded`.
* Every payment must be linked to exactly one order.
* An order's status cannot be `Shipped` if its payment status is `Failed` or `Pending`.
* A `Refunded` payment should correspond to an order in `Cancelled` status (or a defined return/refund state).

## Shipments

* Ship date >= Order date
* Delivered date >= Ship date
* Every shipment must be linked to exactly one order.
* A shipment should not exist (or should remain unset) until the associated order's payment status is `Completed`.

## Reviews

* Every review must be linked to both a customer and a product.
* Rating must fall within a fixed range (1–5).
* A customer may only submit one review per product (uniqueness on customer + product).
* Ideally, a review should only be permitted for a product the customer has actually purchased ("verified purchase" constraint) — a good candidate for a validation query joining `reviews` against `order_items`.

---

## Cross-Cutting Rules

* **Referential integrity** — no address, order, order item, payment, shipment, or review should exist without a valid parent record (customer, order, or product as applicable).
* **Cascade behavior** — deletion behavior (cascade vs. restrict vs. soft delete) should be explicit and consistent for every foreign key relationship, particularly `customers`, `products`, and `orders`, which anchor the most downstream data.
* **Timestamps** — every table should carry `created_at` (and `updated_at` where records are mutable) to support auditability and time-based validation queries.
* **Status consistency** — order, payment, and shipment status fields are interdependent; validation should include cross-table checks (e.g. no `Shipped` order with a `Failed` payment) in addition to single-table enum checks.

---

## Mapping to Validation

| Rule Category      | Example Validation Check                                      |
| ------------------- | -------------------------------------------------------------- |
| Uniqueness           | `customers.email`, `products.sku`, `categories.name` uniqueness |
| Referential integrity| Orphan checks across all foreign keys                          |
| Enum validation       | `orders.status`, `payments.status` restricted to allowed values |
| Cross-table reconciliation | `orders.total` vs. `sum(order_items)`; `payments.amount` vs. `orders.total` |
| Date logic            | `shipments.ship_date >= orders.order_date`; `delivered_date >= ship_date` |
| Business logic (app-layer) | Reviews restricted to verified purchases; inventory sufficiency at checkout |
