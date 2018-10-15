DROP TABLE IF EXISTS chats;

CREATE TABLE chats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  channel TEXT NOT NULL,
  username TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TEXT NOT NULL,
  created_at_second TEXT NOT NULL
);