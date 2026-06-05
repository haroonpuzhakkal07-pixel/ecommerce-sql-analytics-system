CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE sellers (
    seller_id SERIAL PRIMARY KEY,
    seller_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 0 AND 5)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,

    category_id INT NOT NULL,
    seller_id INT NOT NULL,

    price DECIMAL(10,2) NOT NULL CHECK (price > 0),

    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0),

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    FOREIGN KEY (seller_id)
        REFERENCES sellers(seller_id)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status VARCHAR(20)
        CHECK (
            status IN (
                'Pending',
                'Completed',
                'Cancelled'
            )
        ),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,

    order_id INT NOT NULL,

    product_id INT NOT NULL,

    quantity INT NOT NULL
        CHECK (quantity > 0),

    price DECIMAL(10,2) NOT NULL
        CHECK (price > 0),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,

    order_id INT UNIQUE NOT NULL,

    amount DECIMAL(10,2) NOT NULL,

    payment_method VARCHAR(50),

    payment_status VARCHAR(20)
        CHECK (
            payment_status IN (
                'Paid',
                'Failed',
                'Pending'
            )
        ),

    payment_date TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

CREATE TABLE shipping (
    shipping_id SERIAL PRIMARY KEY,

    order_id INT UNIQUE NOT NULL,

    shipping_address TEXT NOT NULL,

    delivery_status VARCHAR(30)
        CHECK (
            delivery_status IN (
                'Processing',
                'Shipped',
                'Delivered'
            )
        ),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

