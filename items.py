import db

def add_item(movie, review, score, user_id):
    sql = """INSERT INTO items (movie, review, score, user_id) 
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [movie, review, score, user_id])

def get_items():
    sql = "SELECT id, movie, score FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.movie, 
                    items.review, 
                    items.score, 
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                items.id = ?"""
    return db.query(sql, [item_id])[0]