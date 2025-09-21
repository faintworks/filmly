import db

def add_item(movie, review, score, user_id):
    sql = """INSERT INTO items (movie, review, score, user_id) 
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [movie, review, score, user_id])

def get_items():
    sql = "SELECT id, movie, score FROM items ORDER BY id DESC"

    return db.query(sql)
