NULL_CHAR = chr(0)

KEYBOARD_MAPPING = {
    'a': NULL_CHAR * 2 + chr(4) + NULL_CHAR * 5,
    'b': NULL_CHAR * 2 + chr(5) + NULL_CHAR * 5,
    'c': NULL_CHAR * 2 + chr(6) + NULL_CHAR * 5,
    'd': NULL_CHAR * 2 + chr(7) + NULL_CHAR * 5,
    'e': NULL_CHAR * 2 + chr(8) + NULL_CHAR * 5,
    'f': NULL_CHAR * 2 + chr(9) + NULL_CHAR * 5,
    'g': NULL_CHAR * 2 + chr(10) + NULL_CHAR * 5,
    'h': NULL_CHAR * 2 + chr(11) + NULL_CHAR * 5,
    'i': NULL_CHAR * 2 + chr(12) + NULL_CHAR * 5,
    'j': NULL_CHAR * 2 + chr(13) + NULL_CHAR * 5,
    'k': NULL_CHAR * 2 + chr(14) + NULL_CHAR * 5,
    'l': NULL_CHAR * 2 + chr(15) + NULL_CHAR * 5,
    'm': NULL_CHAR * 2 + chr(16) + NULL_CHAR * 5,
    'n': NULL_CHAR * 2 + chr(17) + NULL_CHAR * 5,
    'o': NULL_CHAR * 2 + chr(18) + NULL_CHAR * 5,
    'p': NULL_CHAR * 2 + chr(19) + NULL_CHAR * 5,
    'q': NULL_CHAR * 2 + chr(20) + NULL_CHAR * 5,
    'r': NULL_CHAR * 2 + chr(21) + NULL_CHAR * 5,
    's': NULL_CHAR * 2 + chr(22) + NULL_CHAR * 5,
    't': NULL_CHAR * 2 + chr(23) + NULL_CHAR * 5,
    'u': NULL_CHAR * 2 + chr(24) + NULL_CHAR * 5,
    'v': NULL_CHAR * 2 + chr(25) + NULL_CHAR * 5,
    'w': NULL_CHAR * 2 + chr(26) + NULL_CHAR * 5,
    'x': NULL_CHAR * 2 + chr(27) + NULL_CHAR * 5,
    'y': NULL_CHAR * 2 + chr(28) + NULL_CHAR * 5,
    'z': NULL_CHAR * 2 + chr(29) + NULL_CHAR * 5,
    'A': chr(32) + NULL_CHAR + chr(4) + NULL_CHAR * 5,
    'B': chr(32) + NULL_CHAR + chr(5) + NULL_CHAR * 5,
    'C': chr(32) + NULL_CHAR + chr(6) + NULL_CHAR * 5,
    'D': chr(32) + NULL_CHAR + chr(7) + NULL_CHAR * 5,
    'E': chr(32) + NULL_CHAR + chr(8) + NULL_CHAR * 5,
    'F': chr(32) + NULL_CHAR + chr(9) + NULL_CHAR * 5,
    'G': chr(32) + NULL_CHAR + chr(10) + NULL_CHAR * 5,
    'H': chr(32) + NULL_CHAR + chr(11) + NULL_CHAR * 5,
    'I': chr(32) + NULL_CHAR + chr(12) + NULL_CHAR * 5,
    'J': chr(32) + NULL_CHAR + chr(13) + NULL_CHAR * 5,
    'K': chr(32) + NULL_CHAR + chr(14) + NULL_CHAR * 5,
    'L': chr(32) + NULL_CHAR + chr(15) + NULL_CHAR * 5,
    'M': chr(32) + NULL_CHAR + chr(16) + NULL_CHAR * 5,
    'N': chr(32) + NULL_CHAR + chr(17) + NULL_CHAR * 5,
    'O': chr(32) + NULL_CHAR + chr(18) + NULL_CHAR * 5,
    'P': chr(32) + NULL_CHAR + chr(19) + NULL_CHAR * 5,
    'Q': chr(32) + NULL_CHAR + chr(20) + NULL_CHAR * 5,
    'R': chr(32) + NULL_CHAR + chr(21) + NULL_CHAR * 5,
    'S': chr(32) + NULL_CHAR + chr(22) + NULL_CHAR * 5,
    'T': chr(32) + NULL_CHAR + chr(23) + NULL_CHAR * 5,
    'U': chr(32) + NULL_CHAR + chr(24) + NULL_CHAR * 5,
    'V': chr(32) + NULL_CHAR + chr(25) + NULL_CHAR * 5,
    'W': chr(32) + NULL_CHAR + chr(26) + NULL_CHAR * 5,
    'X': chr(32) + NULL_CHAR + chr(27) + NULL_CHAR * 5,
    'Y': chr(32) + NULL_CHAR + chr(28) + NULL_CHAR * 5,
    'Z': chr(32) + NULL_CHAR + chr(29) + NULL_CHAR * 5,
    '1': NULL_CHAR * 2 + chr(30) + NULL_CHAR * 5,
    '2': NULL_CHAR * 2 + chr(31) + NULL_CHAR * 5,
    '3': NULL_CHAR * 2 + chr(32) + NULL_CHAR * 5,
    '4': NULL_CHAR * 2 + chr(33) + NULL_CHAR * 5,
    '5': NULL_CHAR * 2 + chr(34) + NULL_CHAR * 5,
    '6': NULL_CHAR * 2 + chr(35) + NULL_CHAR * 5,
    '7': NULL_CHAR * 2 + chr(36) + NULL_CHAR * 5,
    '8': NULL_CHAR * 2 + chr(37) + NULL_CHAR * 5,
    '9': NULL_CHAR * 2 + chr(38) + NULL_CHAR * 5,
    '0': NULL_CHAR * 2 + chr(39) + NULL_CHAR * 5,
    '\n': NULL_CHAR * 2 + chr(40) + NULL_CHAR * 5,
}


class Keyboard(object):
    mapping = KEYBOARD_MAPPING

    def __init__(self, device='/dev/hidg0'):
        self.device = device

    def write(self, text):
        for x in text:
            self.send_stroke(self.mapping[x])

    def send_stroke(self, data):
        with open(self.device, 'rb+') as fd:
            fd.write(data.encode())
            fd.write((NULL_CHAR*8).encode())
