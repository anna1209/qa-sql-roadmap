from conftest import db_connection
import mysql.connector

def test_verify_customers_have_addresses(db_connection):
    """
    TC-CM-003:
    Verify every customer has at least one address in the addresses table.
    """

    conn = db_connection
    cursor = conn.cursor()

    query = """
    SELECT c.customer_id 
    FROM customers c
    WHERE NOT EXISTS(SELECT * FROM addresses a 
       WHERE a.customer_id = c.customer_id);
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    assert len(results) == 0, (
        f"Found {len(results)} customer(s) without an address: {results}"
    )