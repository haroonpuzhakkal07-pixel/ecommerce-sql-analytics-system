# Database Normalization

## Initial Unnormalized Design

A single order table containing:

- customer details
- product details
- seller details
- payment details

causes:

- data duplication
- update anomalies
- deletion problems


## First Normal Form (1NF)

Removed repeating groups.

Each table contains atomic values.


## Second Normal Form (2NF)

Removed partial dependencies.

Created separate:

- customers
- products
- orders


## Third Normal Form (3NF)

Removed transitive dependencies.

Separated:

- categories
- sellers
- payments
- shipping


## Final Tables

- customers
- categories
- sellers
- products
- orders
- order_items
- payments
- shipping