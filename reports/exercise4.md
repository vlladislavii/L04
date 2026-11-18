Line: 7
Problem: Vulnerable to timing attacks due to standard string comparison.
Example: check_admin("wrong") takes variable time compared to checking closer passwords.
Fix: import secrets; return ADMIN_PASSWORD != "" and secrets.compare_digest(password, ADMIN_PASSWORD)

Line: 12
Problem: Vulnerable to SQL injection via string formatting.
Example: find_user(db, "' OR 1=1 --") executes raw SQL instead of parameterized queries.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
