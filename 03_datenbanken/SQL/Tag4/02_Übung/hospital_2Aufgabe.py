from mysql.connector import connect, MySQLConnection, Error


def get_doctor_details(conn: MySQLConnection, doctor_id: int) -> tuple:
    sql = "SELECT * FROM doctor WHERE doctor_id = %s;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (doctor_id,))
            return cursor.fetchone()
    except Error as e:
        # Fehler loggen
        raise RuntimeError(f"Error fetching product: {doctor_id}: {e}") from e


def get_hospital_details(conn: MySQLConnection, hospital_id: int) -> tuple:
    sql = "SELECT * FROM hospital WHERE hospital_id = %s;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (hospital_id,))
            return cursor.fetchone()
    except Error as e:
        # Fehler loggen
        raise RuntimeError(
            f"Error fetching product: {hospital_id}: {e}") from e


if __name__ == "__main__":

    account = {
        "host": "localhost",
        "user": "alice",
        "password": "abcd1234",
        "port": 3306,
        "database": "hospital_management",
    }

    try:
        with connect(**account) as conn:
            doctor_details = get_doctor_details(conn, doctor_id=106)
            hospital_details = get_hospital_details(conn, hospital_id=3)
            print(doctor_details)
            print(hospital_details)
    except Error as e:
        print("Ausgabe:", e)
    except Exception as e:
        print(e)
