class TestChannelApi(object):
    def test_channel_track(self, client):
        response = client.post('/channels/track', data={'channel': 'shroud'})

        assert response.status_code == 200
        assert b'Tracking' in response.data

    def test_channel_messages_by_time(self, client):
        response = client.get('/channels/messages?channel=shroud')

        assert response.status_code == 200
        assert response.json == {'minute': '2000', 'second': '150'}

    def test_channel_mood(self, client):
        response = client.get('/channels/mood?channel=shroud')

        assert response.status_code == 200
        assert response.json == {'mood': 'Mind blowing ultra-hyped'}