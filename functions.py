from conn import get_db

def insert_humedad(valor):
    db = get_db()
    cursor = db.cursor()
    query = f"INSERT INTO humedad VALUES (NULL, {valor})"
    cursor.execute(query)
    db.commit()
    return True

def get_humedad():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, humedad FROM humedad ORDER BY id"
    cursor.execute(query)
    return cursor.fetchall()