CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    title TEXT,
    movie TEXT,
    review TEXT,
    score INTEGER,
    user_id INTEGER REFERENCES users
);