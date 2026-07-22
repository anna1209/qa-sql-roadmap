SELECT c.customer_id FROM customers c
WHERE NOT EXISTS(SELECT * FROM addresses a 
       WHERE a.customer_id = c.customer_id
);