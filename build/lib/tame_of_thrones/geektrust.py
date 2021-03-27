import os
import sys
from typing import IO

from rule_universe import RuleUniverseCheck


def read_file(file_name: str) -> IO:
    try:
        if os.path.getsize(file_name) == 0:
            print('File is empty')
            exit()
        return open(file_name)
    except FileNotFoundError as msg:
        print('The file does not exist, please try again.', msg)
        exit()


def parse_kingdom_messages(file_handler: IO) -> dict:
    kingdom_messages_to_send = {}
    for line in file_handler:
        kingdom, proposal = line.strip().split(' ', 1)
        kingdom_messages_to_send[kingdom.lower()] = proposal.lower()

    return kingdom_messages_to_send


if __name__ == '__main__':
    """
    python -m geektrust ABSOLUTE_FILE_PATH
    """
    input_file = sys.argv[1]
    sender_ruler = 'SPACE'
    
    with read_file(input_file) as file_handler:
        kingdom_messages_to_send = parse_kingdom_messages(file_handler)

    alliances = RuleUniverseCheck(sender_ruler).send_messages(kingdom_messages_to_send)
    print(*alliances)