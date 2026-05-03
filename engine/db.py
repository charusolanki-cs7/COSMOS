import sqlite3

conn = sqlite3.connect("sophia.db")
cursor = conn.cursor()

# ---------- sys_command table ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sys_command(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    path VARCHAR(1000)
)
""")

cursor.execute(
    "INSERT INTO sys_command VALUES (NULL, ?, ?)",
    ('OneNote', r'C:\Program Files\Microsoft Office\root\Office16\ONENOTE.exe')
)

# ---------- web_command table ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS web_command(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    url VARCHAR(1000)
)
""")

cursor.execute(
    "INSERT INTO web_command VALUES (NULL, ?, ?)",
    ('Facebook', 'https://facebook.com')
)

conn.commit()

# ---------- testing module ----------
query = "OneNote"
cursor.execute(
    "SELECT path FROM sys_command WHERE name = ?",
    (query,)
)

results = cursor.fetchall()
print(results[0][0])

# ✅ close ONLY once, at the end
conn.close()
