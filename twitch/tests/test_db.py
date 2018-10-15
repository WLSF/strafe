import tempfile
from twitch.src.db import init_db, close_db, insert_message

class TestDB(object):
    def test_init_db(self, monkeypatch):
        def getenv(v1, v2):
            a, b = tempfile.mkstemp()
            return b

        monkeypatch.setattr('os.getenv', getenv)
        result = init_db()

        assert result

    def test_close_db(self, monkeypatch):
        def getenv(v1, v2):
            a, b = tempfile.mkstemp()
            return b

        monkeypatch.setattr('os.getenv', getenv)
        result = init_db()
        assert result

        result = close_db()
        assert result


    def test_insert_message(self, monkeypatch):
        def getenv(v1, v2):
            a, b = tempfile.mkstemp()
            return b

        monkeypatch.setattr('os.getenv', getenv)
        db = init_db()
        if db:
            with open('api/resources/schema.sql') as fp:
                db.executescript(fp.read())

        result = insert_message(('shroud', 'whiplk', 'Test message', '201811150454', '20181115045420'))

        assert result
