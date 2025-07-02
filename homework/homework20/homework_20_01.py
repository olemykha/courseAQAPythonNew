import sqlite3
import os

base_dir = "/Users/olemykha/Desktop/courseAQAPythonNew"
db_filename = "sqlite_db.sqlite"
db_path = os.path.join(base_dir, db_filename)

conn = sqlite3.connect(db_path)

# create
"""
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    description TEXT
);


CREATE TABLE IF NOT EXISTS products (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT    NOT NULL,
    description   TEXT,
    price         REAL    NOT NULL,
    category_id   INTEGER NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);
"""

# insert
"""
  ('Fruits', 'Fresh fruits'),
  ('Vegetables', 'Fresh vegetables');

INSERT INTO products (name, description, price, category_id) VALUES
  ('Bananas', 'Organic bananas from Canada', 1.10, 1),
  ('Cucumbers', 'Green cucumbers from Uzbekistan', 1.50, 2),
  ('Tomatoes', 'Red tomatoes from USA', 2.50, 2);
"""

# join
"""
SELECT
  products.id,
  products.name,
  products.description,
  products.price,
  categories.name
FROM products
JOIN categories
  ON products.category_id = categories.id
"""