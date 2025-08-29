"""
Die Datenbank shop auslesen

fetchone => ein Datensatz wird erwartet
fetchmany => er werden viele Datensätze erwartet
"""

from mysql.connector import connect, MySQLConnection, Error


def read_products(conn: MySQLConnection) -> list:
    """Lese alle Produkt aus der Shop-Datenbank."""
    sql = "SELECT * FROM product;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as e:
        raise RuntimeError(f"Error fetching products: {e}") from e


def read_product(conn: MySQLConnection, product_id: int) -> tuple:
    """Lese ein Produkt aus der Shop-Datenbank."""
    sql = "SELECT * FROM product WHERE id = %s;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (product_id,))
            return cursor.fetchone()
    except Error as e:
        # Fehler loggen
        raise RuntimeError(f"Error fetching product: {product_id}: {e}") from e


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
            product = read_product(conn, product_id=3)
            print(product)
            products = read_products(conn)
            print(products)
    except Error as e:
        print("Ausgabe:", e)
    except Exception as e:
        print(e)
