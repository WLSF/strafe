import os

class Config(object):
    DATABASE = os.getenv('DATABASE', '')
    SERVER = os.getenv('SERVER', '')
    PORT = int(os.getenv('PORT', ''))