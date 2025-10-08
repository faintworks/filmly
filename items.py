import db

def add_item(title, movie, review, score, user_id):
    sql = """INSERT INTO items (title, movie, review, score, user_id) 
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, movie, review, score, user_id])

def get_items():
    sql = "SELECT id, title, movie, score FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.movie, 
                    items.review, 
                    items.score,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, movie, review, score):
    sql = """UPDATE items SET title = ?, movie = ?, review = ?, score = ? WHERE id = ?"""
    db.execute(sql, [title, movie, review, score, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title
             FROM items
             WHERE title LIKE ? OR movie LIKE ? OR review LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])
