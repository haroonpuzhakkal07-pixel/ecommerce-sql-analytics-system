SELECT *
FROM products
WHERE price >
(
    SELECT AVG(price)
    FROM products
);


SELECT
    customer_id,
    total_spent
FROM
(
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
) t
WHERE total_spent >
(
    SELECT AVG(total_amount)
    FROM orders
);


SELECT *
FROM products
WHERE price =
(
    SELECT MAX(price)
    FROM products
);