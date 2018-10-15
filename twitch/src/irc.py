import os
import socket
import logging
import threading
from db import insert_message, init_db, close_db
from datetime import datetime


logging.basicConfig(level=logging.INFO)


class TwitchThread(threading.Thread):
    server = os.getenv('SERVER', '')
    port = int(os.getenv('PORT', ''))
    password = os.getenv('PASSWORD', '')
    nick = os.getenv('NICK', '')

    def __init__(self, channel):
        super(TwitchThread, self).__init__()
        self.channel = channel

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.init_socket()
        self.login()
        self.join_channel(self.channel)

    def init_socket(self):
        self.irc.connect((self.server, self.port))

    def command(self, cmd, val):
        self.irc.send('{} {}\n'.format(cmd, val).encode())

    def login(self):
        self.command('PASS', 'oauth:{}'.format(self.password))
        self.command('NICK', self.nick)

    def join_channel(self, channel):
        self.command('JOIN', '#{}'.format(channel))

    def depart_channel(self, channel):
        self.command('PART', '#{}'.format(channel))

    @staticmethod
    def create_datetime_now():
        return str(datetime.now().strftime('%Y%m%d%H%M'))

    @staticmethod
    def create_datetime_now_second():
        return str(datetime.now().strftime('%Y%m%d%H%M%S'))


    def run(self):
        logging.info('Started Twitch Thread on: {}'.format(self.channel))

        init_db()
        logging.info('Started db connection')
        while True:
            try:
                msg = self.irc.recv(1024).decode()
                logging.info('New message received from twitch IRC: {}'.format(msg))
                msg = msg.split()
                if msg[0] == 'PING':
                    self.command('PONG', msg[1])
                    logging.info('PONG cmd answered')

                if msg[1] == 'PRIVMSG':
                    name = msg[0]
                    phr = ' '.join(msg[3:])
                    insert_message((
                        self.channel,
                        name[1:name.find('!')],
                        phr[1:],
                        TwitchThread.create_datetime_now(),
                        TwitchThread.create_datetime_now_second()
                    ))
                    logging.info('Collecting message from twitch')
            except Exception as e:
                logging.error(e)
                close_db()