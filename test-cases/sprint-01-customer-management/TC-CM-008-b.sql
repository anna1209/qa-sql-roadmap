SELECT address_id, customer_id, address_line_1
FROM addresses
WHERE customer_id IS NULL OR address_line_1 IS NULL;