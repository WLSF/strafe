import os
import sqlite3

db = None


def init_db():
    global db
    db = sqlite3.connect(os.getenv('DATABASE', ''), detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db


def insert_message(params):
    try:
        global db
        if db:
            db.execute("INSERT INTO `chats` (`channel`,`username`, `message`, `created_at`, `created_at_second`) VALUES (?, ?, ?, ?, ?)", params)
            db.commit()
        return True
    except Exception as e:
        raise e


def close_db():
    global db
    if db:
        db.close()

    return True
