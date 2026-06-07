from faker import Faker
import random

fake = Faker()

with open("database/categories.sql", "w", encoding="utf-8") as file:

    file.write("""
INSERT INTO categories (category_name) VALUES
('Electronics'),
('Clothing'),
('Books'),
('Home Appliances'),
('Sports'),
('Beauty'),
('Toys'),
('Furniture'),
('Food'),
('Accessories');
""")

with open("database/customers.sql", "w", encoding="utf-8") as file:

    for _ in range(100):

        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")

        # safer email generation
        email = fake.unique.user_name()[:20] + "@gmail.com"

        phone = fake.phone_number().replace("'", "''")
        city = fake.city().replace("'", "''")

        sql = f"""
INSERT INTO customers
(first_name,last_name,email,phone,city)
VALUES
('{first_name}','{last_name}','{email}','{phone}','{city}');
"""

        file.write(sql)

with open("database/sellers.sql", "w", encoding="utf-8") as file:

    for _ in range(20):

        seller_name = fake.company().replace("'", "''")

        email = fake.unique.user_name()[:20] + "@seller.com"

        rating = round(random.uniform(3.0, 5.0), 1)

        sql = f"""
INSERT INTO sellers
(seller_name,email,rating)
VALUES
('{seller_name}','{email}',{rating});
"""

        file.write(sql)

product_prefixes = [
    "Premium",
    "Smart",
    "Ultra",
    "Wireless",
    "Professional",
    "Portable",
    "Advanced",
    "Digital"
]

product_types = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Phone",
    "Speaker",
    "Camera",
    "Headphones",
    "Book",
    "Chair"
]

with open("database/products.sql", "w", encoding="utf-8") as file:

    for _ in range(200):

        product_name = (
            f"{random.choice(product_prefixes)} "
            f"{random.choice(product_types)}"
        )

        category_id = random.randint(1, 10)

        seller_id = random.randint(1, 20)

        price = round(random.uniform(100, 50000), 2)

        stock_quantity = random.randint(10, 500)

        sql = f"""
INSERT INTO products
(product_name,category_id,seller_id,price,stock_quantity)
VALUES
(
'{product_name}',
{category_id},
{seller_id},
{price},
{stock_quantity}
);
"""

        file.write(sql)

from datetime import timedelta

# ------------------
# Orders
# ------------------

with open("database/orders.sql", "w", encoding="utf-8") as file:

    statuses = [
        "Pending",
        "Completed",
        "Cancelled"
    ]

    for _ in range(500):

        customer_id = random.randint(1, 100)

        order_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        status = random.choice(statuses)

        total_amount = round(
            random.uniform(500, 100000),
            2
        )

        sql = f"""
INSERT INTO orders
(customer_id, order_date, status, total_amount)
VALUES
(
{customer_id},
'{order_date}',
'{status}',
{total_amount}
);
"""

        file.write(sql)

# ------------------
# Order Items
# ------------------

with open("database/order_items.sql", "w", encoding="utf-8") as file:

    for _ in range(1500):

        order_id = random.randint(1, 500)

        product_id = random.randint(1, 200)

        quantity = random.randint(1, 5)

        price = round(
            random.uniform(100, 50000),
            2
        )

        sql = f"""
INSERT INTO order_items
(order_id, product_id, quantity, price)
VALUES
(
{order_id},
{product_id},
{quantity},
{price}
);
"""

        file.write(sql)

# ------------------
# Payments
# ------------------

with open("database/payments.sql", "w", encoding="utf-8") as file:

    payment_methods = [
        "Credit Card",
        "Debit Card",
        "UPI",
        "Net Banking",
        "Wallet"
    ]

    payment_statuses = [
        "Paid",
        "Failed",
        "Pending"
    ]

    for order_id in range(1, 501):

        amount = round(
            random.uniform(500, 100000),
            2
        )

        payment_method = random.choice(payment_methods)

        payment_status = random.choice(payment_statuses)

        payment_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        sql = f"""
INSERT INTO payments
(order_id, amount, payment_method, payment_status, payment_date)
VALUES
(
{order_id},
{amount},
'{payment_method}',
'{payment_status}',
'{payment_date}'
);
"""

        file.write(sql)

# ------------------
# Shipping
# ------------------

with open("database/shipping.sql", "w", encoding="utf-8") as file:

    shipping_statuses = [
        "Processing",
        "Shipped",
        "Delivered"
    ]

    for order_id in range(1, 501):

        address = fake.address().replace("\n", ", ").replace("'", "''")

        status = random.choice(shipping_statuses)

        sql = f"""
INSERT INTO shipping
(order_id, shipping_address, delivery_status)
VALUES
(
{order_id},
'{address}',
'{status}'
);
"""

        file.write(sql)