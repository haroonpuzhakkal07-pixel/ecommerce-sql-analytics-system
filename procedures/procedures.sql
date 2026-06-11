CREATE OR REPLACE PROCEDURE update_stock(
    p_product_id INT,
    p_quantity INT
)
LANGUAGE plpgsql
AS $$
BEGIN

    UPDATE products
    SET stock_quantity = stock_quantity - p_quantity
    WHERE product_id = p_product_id;

END;
$$;