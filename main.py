import os
from lib.quake3             import LogParser
from lib.print_data_quake   import print_data_prompt

game_log_path = os.path.join(os.getcwd(), 'resources', 'game.log')
log_parser = LogParser()

data = log_parser.parse(fullpath= game_log_path)

print_data_prompt(data)