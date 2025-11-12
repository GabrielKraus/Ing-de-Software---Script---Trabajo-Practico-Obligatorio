import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE u(id INT, user TEXT, pass TEXT); INSERT INTO u VALUES(1,'admin','pass100');")

def vuln(user, pw):
    q = f"SELECT * FROM u WHERE user='{user}' AND pass='{pw}'"
    print("VULN >", q); return bool(db.execute(q).fetchone())

def safe(user, pw):
    q = "SELECT * FROM u WHERE user=? AND pass=?"
    print("SAFE >", q, (user, pw)); return bool(db.execute(q,(user,pw)).fetchone())

payload = "' OR '1'='1"
print("Vulnerable ->", vuln("admin", payload))   # True (attack succeeds)
print("Parametrized ->", safe("admin", payload)) # False (attack neutralizado)
print("Credenciales reales ->", safe("admin","pass100")) # True
db.close()