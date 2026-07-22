from conftest import db_connection
import mysql.connector

def get_connection():
    return mysql.connector.connect(**db_connection)

def verity_total_customer_count():
    """
    TC-CM-001:
    Verify total customer count
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) AS Customer_count 
    FROM customers
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()