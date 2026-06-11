BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 2
WHERE product_id = 1;

INSERT INTO orders
(
    customer_id,
    order_date,
    status,
    total_amount
)
VALUES
(
    1,
    CURRENT_TIMESTAMP,
    'Pending',
    1500
);

COMMIT;




BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 10000
WHERE product_id = 1;

ROLLBACK;