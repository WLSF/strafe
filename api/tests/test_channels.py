class TestChannelApi(object):
    def test_channel_track(self, client, monkeypatch):
        def track(channel):
            return True

        monkeypatch.setattr('api.src.models.Channel.track_messages', track)
        response = client.post('/channels/track', json={'channel': 'shroud'})

        assert response.status_code == 200
        assert response.json == {'message': 'Tracking'}

    def test_channel_messages_by_time(self, client, monkeypatch):
        def mood_counter(channel):
            return 50

        monkeypatch.setattr('api.src.models.average_minute', mood_counter)
        monkeypatch.setattr('api.src.models.average_second', mood_counter)
        response = client.get('/channels/messages?channel=shroud')

        assert response.status_code == 200
        assert response.json == {'minute': 50, 'second': 50}

    def test_channel_mood(self, client, monkeypatch):
        def mood_counter(channel):
            return 50

        monkeypatch.setattr('api.src.models.average_minute', mood_counter)
        response = client.get('/channels/mood?channel=shroud')

        assert response.status_code == 200
        assert response.json == {'mood': 'Collecting spammers'}