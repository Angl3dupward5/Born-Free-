import sqlite3

conn = sqlite3.connect("poll.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS votes (
    option TEXT PRIMARY KEY,
    count INTEGER
)
""")

cursor.execute("INSERT OR IGNORE INTO votes VALUES ('loved', 0)")
cursor.execute("INSERT OR IGNORE INTO votes VALUES ('good', 0)")
cursor.execute("INSERT OR IGNORE INTO votes VALUES ('notforme', 0)")

conn.commit()
conn.close()

print("Poll database created successfully!")