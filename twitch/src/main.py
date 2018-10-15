import socket
import logging
from irc import TwitchThread

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info('Starting twitch server')

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 49152))

    logging.info('Listening at 0.0.0.0:49152')

    thread = None
    old_channel = None

    while True:
        channel = server.recv(1024).decode()
        logging.info('Channel received from the API: {}'.format(channel))


        if old_channel:
            thread.depart_channel(old_channel)

        old_channel = channel

        if not thread:
            thread = TwitchThread(channel)
            thread.start()
        else:
            thread.join_channel(channel)
