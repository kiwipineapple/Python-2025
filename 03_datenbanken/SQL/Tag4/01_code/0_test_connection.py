"""
MySQL Connector installieren:

python.exe -m pip install --upgrade pip
"""


from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="alice",
        password="abcd1234",
        port=3306
    ) as conn:
        with conn.cursor() as cursor:
            sql_query = "SELECT version();"
            cursor.execute(sql_query)
            print(cursor.fetchone())
except Error as e:
    print("Ausgabe:", e)
except Exception as e:
    print(e)
