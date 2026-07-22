"""
run_queries.py

Script to run a list of MySQL queries using mysql-connector-python.

Usage:
  - Set DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME in the environment
"""

import os
import mysql.connector
from mysql.connector import errorcode
import sqlparse   # optional, used when reading .sql files with multiple statements
from typing import List, Tuple

# === Configuration: read from environment for safety ===
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", None),
    "autocommit": False,
}

# === Example queries (you can replace these or read from file) ===
QUERIES: List[str] = [
    "CREATE TABLE IF NOT EXISTS demo (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100))",
    "INSERT INTO demo (name) VALUES ('alice')",
    "INSERT INTO demo (name) VALUES ('bob')",
    "SELECT id, name FROM demo",
    # "DROP TABLE demo",  # destructive: use with caution
]

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def run_queries(queries: List[str], all_in_transaction: bool = True) -> List[Tuple[str, any]]:
    """
    Execute the provided queries.
    - If all_in_transaction=True: open one transaction for all queries (commit at end, rollback on error).
    - If False: commit after each non-SELECT statement; SELECTs are not committed.
    Returns a list of (query, result) where result is rows for SELECT or cursor.rowcount for DML.
    """
    results = []
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        if all_in_transaction:
            conn.start_transaction()
        for q in queries:
            q_stripped = q.strip()
            if not q_stripped:
                continue
            try:
                cursor.execute(q_stripped)
            except mysql.connector.Error as e:
                # If executing a multi-statement block fails, raise to trigger rollback (if in transaction)
                raise

            # If it's a SELECT, fetch rows
            if q_stripped.lower().startswith("select"):
                rows = cursor.fetchall()
                results.append((q_stripped, rows))
            else:
                # Non-SELECT: rowcount indicates affected rows
                results.append((q_stripped, cursor.rowcount))
                if not all_in_transaction:
                    conn.commit()
        if all_in_transaction:
            conn.commit()
    except Exception:
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        raise
    finally:
        if conn:
            cursor.close()
            conn.close()
    return results

def read_queries_from_file(path: str) -> List[str]:
    """
    Read SQL file and split to statements using sqlparse (handles comments, semicolons in strings better).
    pip install sqlparse
    """
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    statements = [s.strip() for s in sqlparse.split(sql) if s.strip()]
    return statements

def executemany_example():
    """Show how to use parameterized executemany for bulk inserts safely."""
    data = [("charlie",), ("diana",)]
    q = "INSERT INTO demo (name) VALUES (%s)"
    conn = connect()
    try:
        cur = conn.cursor()
        cur.executemany(q, data)
        conn.commit()
        print(f"Inserted {cur.rowcount} rows")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    # Example: run the QUERIES list. Change all_in_transaction as you need.
    try:
        results = run_queries(QUERIES, all_in_transaction=True)
        for q, res in results:
            if isinstance(res, list):
                print("RESULT for query:", q)
                for row in res:
                    print(row)
            else:
                print(f"EXECUTED: {q} -> affected rows: {res}")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: check DB_USER/DB_PASSWORD")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist: set DB_NAME or create the DB")
        else:
            print("MySQL error:", err)
    except Exception as e:
        print("Error:", e)