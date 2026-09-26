# This class defines a PlayingCard
class PlayingCard:
    _SUIT_CODEPOINT_OFFSETS = {
        'SPADES': 0x00,
        'HEARTS': 0x10,
        'DIAMONDS': 0x30,
        'CLUBS': 0x20,
    }
    _RANK_CODEPOINT_OFFSETS = {
        1: 0x01,
        2: 0x02,
        3: 0x03,
        4: 0x04,
        5: 0x05,
        6: 0x06,
        7: 0x07,
        8: 0x08,
        9: 0x09,
        10: 0x0A,
        11: 0x0B,
        12: 0x0D,
        13: 0x0E,
    }

    def __init__(self, card_id, card_suit, card_rank, card_face_value):
        ''' A Card has a unique id (1-52),
        is of a certain card suit (Hearts, Spades, etc.),
        has a rank (e.g. king, seven, etc.)
        and has a face value (e.g. 13, 7, etc.).
        In this game aces are low and have a face value of 1.
        The face value of the other cards is equal to their rank (e.g. a 2 has a face value of 2, a 3 has a face value of 3, etc.).
        The face value of the face cards is as follows: Jack = 11, Queen = 12, King = 13.
        '''
        self.__card_id = card_id  # 1 - 52 for a regular poker deck of cards. Each card will have a unique id.
        self.__card_suit = card_suit  # Spades, Hearts, Diamonds, Clubs
        self.__card_rank = card_rank  # Ace, Two, Three, etc.
        self.__card_face_value = card_face_value  # 1, 2, 3, etc.

    def get_card_id(self):
        return self.__card_id

    def get_card_suit(self):
        return self.__card_suit;

    def get_card_rank(self):
        return self.__card_rank

    def get_card_face_value(self):
        return self.__card_face_value

    def __str__(self):
        '''Return a string representation of the card, including its rank, suit, face value, and Unicode symbol.'''
        suit_offset = self._SUIT_CODEPOINT_OFFSETS[self.__card_suit]  # Unicode code point offset for the suit
        rank_offset = self._RANK_CODEPOINT_OFFSETS[self.__card_face_value]  # Unicode code point offset for the rank
        card_symbol = chr(0x1F0A0 + suit_offset + rank_offset)  # Unicode code point for the card symbol
        return str(self.__card_rank).upper() + ' of ' + self.__card_suit.upper() + '  (' + str(
            self.__card_face_value) + ') ' + card_symbol
