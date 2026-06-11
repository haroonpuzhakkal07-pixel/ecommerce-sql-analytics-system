CREATE OR REPLACE FUNCTION customer_lifetime_value(
    p_customer_id INT
)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE

    total_spent NUMERIC;

BEGIN

    SELECT SUM(total_amount)
    INTO total_spent
    FROM orders
    WHERE customer_id = p_customer_id;

    RETURN COALESCE(total_spent, 0);

END;
$$;




CREATE OR REPLACE FUNCTION total_orders(
    p_customer_id INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE

    order_count INT;

BEGIN

    SELECT COUNT(*)
    INTO order_count
    FROM orders
    WHERE customer_id = p_customer_id;

    RETURN order_count;

END;
$$;