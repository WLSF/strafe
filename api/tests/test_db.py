from api.src.db import get_db, s_all


class TestDB(object):
    def test_read_from_closed_db(self, app):
        with app.app_context():
            db = get_db()
            assert db is get_db()


        try:
            s_all()
        except Exception as e:
            assert 'Working outside of application context' in str(e)

    def test_init_db_from_cli(self, app, monkeypatch):
        class Recorder(object):
            called = False

        def fake_init_db():
            Recorder.called = True

        cli = app.test_cli_runner()
        monkeypatch.setattr('api.src.db.init_db', fake_init_db)
        response = cli.invoke(args=['init-db'])
        assert 'Database up' in response.output
        assert Recorder.called

    def test_reading_without_rows(self, app):
        with app.app_context():
            response = s_all()
            assert response == []

    def test_reading(self, app):
        with app.app_context():
            db = get_db()
            db.execute(
                "INSERT INTO `chats` (`channel`, `username`, `message`, `created_at`, `created_at_second`) VALUES(?, ?, ?, ?, ?)",
                ('shroud', 'whiplk', 'Test message, shroud rules!', '201811060420', '20181106042020')
            )

            response = s_all()

            obj = response.pop()
            assert obj.get('channel') == 'shroud'
            assert obj.get('username') == 'whiplk'
            assert obj.get('message') == 'Test message, shroud rules!'
            assert obj.get('created_at') == '20181106042020'