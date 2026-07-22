SELECT a.address_id, a.customer_id
FROM addresses a
WHERE NOT EXISTS (
    SELECT *
    FROM customers c
    WHERE c.customer_id = a.customer_id
);