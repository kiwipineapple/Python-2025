
"""
Einträge in der Datenbank shop machen.

INSERT, UPDATE, DELETE

execute() => Führt SQL aus
executemany() => Bei schreibenden Aktionen von vielen Einträgen
commit() => Führt eine schreibende Aktion auf der DB aus.
"""

from mysql.connector import connect, MySQLConnection, Error


def insert_products(conn, products: list[str], category_id: int) -> int:
    """Füge mehrere Produkte in eine Kategorie ein."""
    sql = "INSERT INTO product (name, category_id) VALUES (%s, %s);"
    # prepare Data for Multi-Insert
    values = [(name, category_id) for name in products]
    try:
        with conn.cursor() as cursor:
            cursor.executemany(sql, values)  # executemany
            conn.commit()
            return cursor.rowcount  # Wieviele Objekte wurden eingetragen
    except Error as e:
        raise RuntimeError(f"Error inserting products: {e}") from e


def insert_product(conn, product_name: str, category_id: int) -> int:
    """Füge ein Produkt mit einem Namen und einer Kategorie ein."""
    sql = "INSERT INTO product (name, category_id) VALUES (%s, %s);"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (product_name, category_id))
            conn.commit()  # Schreibende Aktion bestätigen
            return cursor.lastrowid
    except Error as e:
        raise RuntimeError(f"Error inserting product: {e}") from e


if __name__ == "__main__":

    account = {
        "host": "localhost",
        "user": "alice",
        "password": "abcd1234",
        "port": 3306,
        "database": "shop",  # use shop;
    }

    try:
        with connect(**account) as conn:
            last_id = insert_product(conn, "Wasserball eckig", 1)
            print(f"Id des zuletzt eingefügten Produkts: {last_id}")
            products = ["Autoreifen", "Wanderstab", "Schwimmflügel"]
            inserted_products = insert_products(conn, products, category_id=2)
            print(f"Es wurden {inserted_products} in die DB eingetragen.")

    except Error as e:
        print("Ausgabe:", e)
    except Exception as e:
        print(e)
