
"""
Einträge in der Datenbank shop als Transaktion machen.

INSERT, UPDATE, DELETE

execute() => Führt SQL aus
executemany() => Bei schreibenden Aktionen von vielen Einträgen
commit() => Führt eine schreibende Aktion auf der DB aus.
"""

from mysql.connector import connect, MySQLConnection, Error


def insert_products(conn, products: list[tuple], products2: list[tuple]):
    """Viele Produkte einfügen. Der Update geht absichtlich schief,
    damit der Rollback durchgeführt wird.

    products = [('Autoreifen', 2), ('Wanderstab', 2), ('Schwimmflügel', 2)]
    """
    sql = "INSERT INTO product (name, category_id) VALUES (%s, %s);"
    try:
        with conn.cursor() as cursor:
            conn.start_transaction()
            # Bei einem Rollback wird das allerdings wieder rückgängig gemacht.
            cursor.executemany(sql, products)
            # HIER FEHLER! Weil bei products2 gibt es Foreignkey, die nicht existiert.
            # cursor.executemany(sql, products2)
            conn.commit()
    except Error as e:
        # Alles zurück auf Anfang
        conn.rollback()
        print(f"Fehler{e}: Rollback wurde durchgefüht")


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
            products = [('Autoreifen42', 2), ('Wanderstab42', 2)]
            # Fehler, weil Kategorie 192 nicht existiert
            wrong_products = [('Autoreifen123', 192)]
            insert_products(conn, products, wrong_products)

    except Error as e:
        print("Ausgabe:", e)
    except Exception as e:
        print(e)
