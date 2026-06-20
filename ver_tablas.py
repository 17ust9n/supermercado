import sqlite3

# Ruta a tu base de datos SQLite
db_path = 'db.sqlite3'

# Conectar a la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Consultar todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"Cantidad de tablas: {len(tables)}")
print("Tablas existentes:")
for table in tables:
    print(f"- {table[0]}")

conn.close()
