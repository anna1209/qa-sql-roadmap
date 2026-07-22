SELECT customer_id, first_name, last_name, email
FROM customers
WHERE first_name IS NULL OR last_name IS NULL OR email IS NULL;