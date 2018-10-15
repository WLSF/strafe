import socket
from flask import current_app, jsonify, Response
from api.src.db import select_with, average_minute, average_second


class Channel:
    @staticmethod
    def track_messages(channel):
        udp = None
        try:
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            server = current_app.config['SERVER']
            port = current_app.config['PORT']

            udp.sendto(channel.encode(), (server, port))

        except Exception as e:
            return str(e)
        finally:
            udp.close()

        return True

    @staticmethod
    def get_messages_by_time(channel):
        return {'second': average_second(channel), 'minute': average_minute(channel)}

    @staticmethod
    def get_mood_from(channel):
        avg = average_minute(channel)

        msg = None

        if avg < 5:
            msg = 'Zzz'
        elif avg < 10:
            msg = 'Surviving smoothly'
        elif avg < 25:
            msg = 'Sounds interesting'
        elif avg < 40:
            msg = 'Blowing some minds'
        elif avg < 60:
            msg = 'Collecting spammers'
        else:
            msg = 'More than meets the eye'

        return {'mood': msg}
