import sqlite3
import pytest
from exercise4 import check_admin, find_user

def test_check_admin():
    assert check_admin("admin123") == True
    assert check_admin("wrong") == False

def test_find_user_sql_injection():
    # Setup an in-memory database to test the SQL Injection vulnerability
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('admin')")
    db.commit()
    
    # Under SQL Injection, a payload like "' OR '1'='1" returns a row instead of None
    result = find_user(db, "' OR '1'='1")
    assert result is None
