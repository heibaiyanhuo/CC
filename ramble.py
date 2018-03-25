
class Ramble:

    def __init__(self, move, scan, scan_finished=False):
        # self.scan_finished = scan_finished
        # if not scan_finished:
        #     self.map = [[0 for i in range(100)] for j in range(100)]
        self.move = move
        self.scan = scan
        self.curr_direction = 'west'
        self.next_scan()

    def next_move(self, scan_result):
        curr_x, curr_y = -1, -1
        for coord, obj_data_list in scan_result:
            x, y = coord
            if len(obj_data_list) > 1:
                for obj_data in obj_data_list:
                    d = dict(obj_data)
                    if d['type'] == 'object' and d['identifier'] == 'game_object_1':
                        curr_x, curr_y = x, y
                        break
        if self.curr_direction == 'west':
            if curr_x != 0:
                self.move('west')
            else:
                self.curr_direction = 'south'
                self.move('south')
        elif self.curr_direction == 'south':
            if curr_y != 0:
                self.move('south')
            else:
                self.curr_direction = 'east'
                self.move('east')
        elif self.curr_direction == 'east':
            if curr_x != 49:
                self.move('east')
            else:
                self.curr_direction = 'north'
                self.move('north')
        else:
            if curr_y != 49:
                self.move('north')
            else:
                self.curr_direction = 'west'
                self.move('west')

    def next_scan(self):
        self.scan()