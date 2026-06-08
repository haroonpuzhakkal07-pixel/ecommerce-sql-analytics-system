SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date,
    o.status
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;


SELECT
    p.product_name,
    c.category_name,
    p.price
FROM products p
INNER JOIN categories c
ON p.category_id = c.category_id;


SELECT
    s.seller_name,
    p.product_name,
    p.price
FROM sellers s
INNER JOIN products p
ON s.seller_id = p.seller_id;


SELECT
    o.order_id,
    o.total_amount,
    p.payment_method,
    p.payment_status
FROM orders o
INNER JOIN payments p
ON o.order_id = p.order_id;