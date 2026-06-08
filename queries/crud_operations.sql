INSERT INTO customers
(
    first_name,
    last_name,
    email,
    phone,
    city
)
VALUES
(
    'Haroon',
    'Rasheed',
    'haroon7@gmail.com',
    '9876543210',
    'Ottappalam'
);


SELECT *
FROM customers
WHERE city = 'Ottappalam';


UPDATE products
SET stock_quantity = stock_quantity + 50
WHERE product_id = 1;


DELETE FROM customers
WHERE customer_id = 101;