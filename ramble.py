
MAP_SIZE = 100
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

        self.begin_x = MAP_SIZE - 1 - (VIEW_DEPTH - 2)
        self.end_x = VIEW_DEPTH - 2
        self.begin_y = MAP_SIZE - 1 - (VIEW_DEPTH - 2)
        self.end_y = VIEW_DEPTH - 2

        self.next_scan()

    def next_move(self, scan_result):
        print(self.scan_count)
        if self.begin_x <= self.end_x or self.begin_y <= self.end_y:
            self.store_map()
            return
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
                    if d['identifier'] == 'game_object_6':
                        self_x, self_y = x, y
                    else:
                        self.enemies[x][y] = 1

        if self.curr_direction == 'west':
            if self_x > self.end_x:
                if self.enemies[self_x - 1][self_y] == 1:
                    self.move('south-west')
                else:
                    self.move('west')
            else:
                self.begin_y -= (VIEW_DEPTH - 1)
                self.curr_direction = 'south'
                self.move('south')
        elif self.curr_direction == 'south':
            if self_y > self.end_y:
                if self.enemies[self_x][self_y - 1] == 1:
                    self.move('south-east')
                else:
                    self.move('south')
            else:
                self.end_x += (VIEW_DEPTH - 1)
                self.curr_direction = 'east'
                self.move('east')
        elif self.curr_direction == 'east':
            if self_x < self.begin_x:
                if self.enemies[self_x + 1][self_y] == 1:
                    self.move('north-east')
                else:
                    self.move('east')
            else:
                self.end_y += (VIEW_DEPTH - 1)
                self.curr_direction = 'north'
                self.move('north')
        else:
            if self_y < self.begin_y:
                if self.enemies[self_x][self_y + 1] == 1:
                    self.move('north-west')
                else:
                    self.move('north')
            else:
                self.begin_x -= (VIEW_DEPTH - 1)
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