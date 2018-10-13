import sqlite3, click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('../resources/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    "Starts the database and run the migrations"
    init_db()
    click.echo('Database up.')


def setup_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def select(query):
    try:
        cur = get_db().execute('SELECT {}'.format(query))

        data = []
        for row in cur:
            data.append({'channel': row['channel'],
                         'username': row['username'],
                         'message': row['message'],
                         'created_at': row['created_at']})

        cur.close()
        return data
    except Exception as e:
        raise e


def insert(query, params):
    try:
        cur = get_db()
        cur.execute('INSERT {}'.format(query), params)
        cur.commit()
        cur.close()
        return True
    except Exception as e:
        raise e