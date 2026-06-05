from faker import Faker
import random

fake = Faker()

with open("database/insert_data.sql", "w", encoding="utf-8") as file:

    # ------------------
    # Categories
    # ------------------

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

    # ------------------
    # Customers
    # ------------------

    for _ in range(100):

        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        email = fake.unique.email().replace("'", "''")
        phone = fake.phone_number().replace("'", "''")
        city = fake.city().replace("'", "''")

        sql = f"""
INSERT INTO customers
(first_name, last_name, email, phone, city)
VALUES
('{first_name}', '{last_name}', '{email}', '{phone}', '{city}');
"""

        file.write(sql)

    # ------------------
    # Sellers
    # ------------------

    for _ in range(20):

        seller_name = fake.company().replace("'", "''")
        email = fake.unique.company_email().replace("'", "''")
        rating = round(random.uniform(3.0, 5.0), 1)

        sql = f"""
INSERT INTO sellers
(seller_name, email, rating)
VALUES
('{seller_name}', '{email}', {rating});
"""

        file.write(sql)

print("insert_data.sql generated successfully.")