SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 10;


SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;


SELECT
    p.product_name,
    SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 10;


SELECT
    c.category_name,
    SUM(oi.quantity * oi.price) AS revenue
FROM categories c
JOIN products p
ON c.category_id = p.category_id
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY c.category_name
ORDER BY revenue DESC;


SELECT
    s.seller_name,
    SUM(oi.quantity * oi.price) AS revenue
FROM sellers s
JOIN products p
ON s.seller_id = p.seller_id
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY s.seller_name
ORDER BY revenue DESC;


SELECT
    product_name,
    stock_quantity
FROM products
WHERE stock_quantity < 50
ORDER BY stock_quantity;


SELECT
    status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY status;


SELECT
    payment_status,
    COUNT(*) AS total
FROM payments
GROUP BY payment_status;


SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC
LIMIT 10;


SELECT
    ROUND(AVG(total_amount), 2)
AS average_order_value
FROM orders;