
class Ramble:

    def __init__(self, move, scan=None):
        self.map = None
        self.move = move
        self.scan = scan
        self.start()

    def start(self):
        direction = 'west'
        self.move(direction)