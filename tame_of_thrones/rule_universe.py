from seasar_cipher import SeasarCipher


class RuleUniverseCheck:
    ALLIANCES_REQUIRED = 3
    KINGDOM_CODES = {
        'air': 'owl',
        'fire': 'dragon',
        'ice': 'mammoth',
        'land': 'panda',
        'space': 'gorilla',
        'water': 'octopus'
    }

    def __init__(self, ruler: str) -> None:
        self.ruler = ruler

    def send_messages(self, kingdom_messages_to_send: dict) -> list:
        alliances = [self.ruler]
        for receiver_kingdom, message in kingdom_messages_to_send.items():
            if self.check_alliance(receiver_kingdom, message, alliances):
                alliances.append(receiver_kingdom.upper())
        if len(alliances) >= 3:
            return alliances
        return ['NONE']

    def check_alliance(self, kingdom: str, message: str, existing_alliances: list) -> bool:
        """
        check if the kingdom can become alliance by receiving the given encrypted code.
        :param kingdom: kingdom name
        :param message: code sent to the kingdom
        :param existing_alliances: list of allies till now
        :return: True
        """
        is_alliance = False
        try:
            decrypted_code = list(SeasarCipher().decrypt(message, len(self.KINGDOM_CODES[kingdom])))
            kingdom_code = list(self.KINGDOM_CODES[kingdom])
            # write algorithm to check kingdom_code exist in decrypted_code
            is_alliance = False
            for char in kingdom_code:
                if char in decrypted_code:
                    decrypted_code.remove(char)
                    is_alliance = True
                else:
                    is_alliance = False
                    break
        except KeyError as err_msg:
            print("Such a Country Does Not Exist : ", err_msg)
        return is_alliance and kingdom not in existing_alliances
