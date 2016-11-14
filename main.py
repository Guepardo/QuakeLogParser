import os

from lib.quake3 import LogParser

game_log_path = os.path.join(os.getcwd(), 'resources', 'game.log')

log_parser = LogParser()

print(log_parser.parse(fullpath= game_log_path))