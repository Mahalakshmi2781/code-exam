import sqlite3
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCTS (
id INTEGER PRIMARY KEY,
cost REAL,
category TEXT,
retail_price REAL,
brand TEXT,
department TEXT,
sku TEXT,
distribution_center INTEGER)''')
conn.commit()
print(" Table 'products' created succesfully")
conn.close()
