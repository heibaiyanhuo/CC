
class Ramble:

    def __init__(self, move, scan):
        self.map = None
        self.move = move
        self.scan = scan
        self.next_scan()

    def next_move(self, scan_result):
        self.move('south')
    
    def next_scan(self):
        self.scan()