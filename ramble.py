
MAP_SIZE = 50
VIEW_DEPTH = 4

class Ramble:

    def __init__(self, move, scan):
        self.map = [['0' for i in range(MAP_SIZE)] for j in range(MAP_SIZE)]
        self.enemies = [[0 for i in range(MAP_SIZE)] for j in range(MAP_SIZE)]
        self.move = move
        self.scan = scan
        self.scan_count = 0
        self.curr_direction = 'west'
        self.need_check = True

        self.next_scan()

    def next_move(self, scan_result):
        self_x, self_y = -1, -1
        for coord, obj_data_list in scan_result:
            x, y = coord
            for obj_data in obj_data_list:
                d = dict(obj_data)
                if d['type'] == 'terrain':
                    terrain = d['identifier']
                    if self.map[x][y] == '0':
                        self.map[x][y] = '=' if terrain == 'water' else '#'
                        self.scan_count += 1
                        if self.scan_count == MAP_SIZE * MAP_SIZE:
                            self.store_map()
                elif d['type'] == 'object':
                    if d['identifier'] == 'game_object_1':
                        self_x, self_y = x, y
                    else:
                        self.enemies[x][y] = 1

        if self.curr_direction == 'west':
            if self_x > 0:
                if self.enemies[self_x - 1][self_y] == 1:
                    self.move('south-west')
                else:
                    self.move('west')
            else:
                self.store_map()
                # self.curr_direction = 'south'
                # self.move('south')
        elif self.curr_direction == 'south':
            if self_y != 0:
                self.move('south')
            else:
                self.curr_direction = 'east'
                self.move('east')
        elif self.curr_direction == 'east':
            if self_x != 49:
                self.move('east')
            else:
                self.curr_direction = 'north'
                self.move('north')
        else:
            if self_y != 49:
                self.move('north')
            else:
                self.curr_direction = 'west'
                self.move('west')

    def next_scan(self):
        if self.need_check:
            self.scan()

    def store_map(self):
        with open('map.txt', 'w+') as f:
            for i in range(MAP_SIZE - 1, -1, -1):
                for j in range(MAP_SIZE):
                    f.write(self.map[j][i])
                f.write('\n')