import db

def add_item(movie, review, score, user_id):
    sql = """INSERT INTO items (movie, review, score, user_id) 
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [movie, review, score, user_id])