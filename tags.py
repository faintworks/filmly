import db

def normalize_tags(raw):
    if not raw:
        return []
    tags = [t.strip().lower() for t in raw.split(',')]
    tags = [t for t in tags if t]
    tags = [t[:30] for t in tags]
    seen = set(); out = []
    for t in tags:
        if t not in seen:
            seen.add(t); out.append(t)
    return out

def upsert_tag(name):
    db.execute("INSERT INTO tags (name) VALUES (?) ON CONFLICT(name) DO NOTHING;", [name])
    row = db.query("SELECT id FROM tags WHERE name = ?;", [name])
    return row[0]['id'] if row else None

def link_item_tag(item_id, tag_id):
    db.execute("INSERT OR IGNORE INTO item_tags (item_id, tag_id) VALUES (?, ?);", [item_id, tag_id])

def replace_item_tags(item_id, tag_names):
    db.execute("DELETE FROM item_tags WHERE item_id = ?;", [item_id])
    for name in tag_names:
        tag_id = upsert_tag(name)
        if tag_id is not None:
            link_item_tag(item_id, tag_id)

def get_tags_for_items(item_ids):
    if not item_ids:
        return {}
    placeholders = ",".join(["?"] * len(item_ids))
    sql = f"""
      SELECT it.item_id, t.name
      FROM item_tags it
      JOIN tags t ON t.id = it.tag_id
      WHERE it.item_id IN ({placeholders})
      ORDER BY t.name
    """
    rows = db.query(sql, item_ids)
    by_item = {}
    for r in rows:
        by_item.setdefault(r['item_id'], []).append(r['name'])
    return by_item