SELECT column_name, constraint_name
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'shopsmart_test' AND TABLE_NAME = 'addresses';