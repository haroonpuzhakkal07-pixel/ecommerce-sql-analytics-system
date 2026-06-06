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

