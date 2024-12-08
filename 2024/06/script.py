# The Historians use their fancy device again, this time to whisk you all away
# to the North Pole prototype suit manufacturing lab... in the year 1518! It
# turns out that having direct access to history is very convenient for a group
# of historians.
#
# You still have to be careful of time paradoxes, and so it will be important
# to avoid anyone from 1518 while The Historians search for the Chief.
# Unfortunately, a single guard is patrolling this part of the lab.
#
# Maybe you can work out where the guard will go ahead of time so that The
# Historians can search safely?
#
# You start by making a map (your puzzle input) of the situation. For example:
#
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
#
# The map shows the current position of the guard with ^ (to indicate the guard
# is currently facing up from the perspective of the map). Any
# obstructions - crates, desks, alchemical reactors, etc. - are shown as #.
#
# Lab guards in 1518 follow a very strict patrol protocol which involves
# repeatedly following these steps:
#
#     - If there is something directly in front of you, turn right 90 degrees.
#     - Otherwise, take a step forward.
#
# Following the above protocol, the guard moves up several times until she
# reaches an obstacle (in this case, a pile of failed suit prototypes):
#
# ....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
#
# Because there is now an obstacle in front of the guard, she turns right
# before continuing straight in her new facing direction:
#
# ....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
#
# Reaching another obstacle (a spool of several very long polymers), she turns
# right again and continues downward:
#
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#...
#
# This process continues for a while, but the guard eventually leaves the
# mapped area (after walking past a tank of universal solvent):
#
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v..
#
# By predicting the guard's route, you can determine which specific positions
# in the lab will be in the patrol path. Including the guard's starting
# position, the positions visited by the guard before leaving the area are
# marked with an X:
#
# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..
#
# In this example, the guard will visit 41 distinct positions on your map.
#
# Predict the path of the guard. How many distinct positions will the guard
# visit before leaving the mapped area?


class Floor:
    def __init__(self, input):
        lines = input.strip().split('\n')

        self.done = False

        # Assuming width and height are the same dimension
        self.d = len(lines)

        self.map = [[False for _ in range(self.d)] for _ in range(self.d)]
        self.visited = [[0 for _ in range(self.d)] for _ in range(self.d)]

        self.pos = None
        self.dir = None

        for r in range(self.d):
            for c in range(self.d):
                if lines[r][c] == '#':
                    self.map[r][c] = True

                if lines[r][c] == '^':
                    self.pos = (r, c)
                    self.dir = (-1, 0)

    def move(self):
        if self.done:
            return

        r, c, = self.pos
        dr, dc =  self.dir

        nr = r + dr
        nc = c + dc

        if nr < 0 or nr >= self.d or nc < 0 or nc >= self.d:
            self.done = True
        elif self.map[nr][nc]:
            self.dir = (dc, -dr)
        else:
            self.visited[r][c] = 1
            self.visited[nr][nc] = 1
            self.pos = (nr, nc)

    def print(self):
        for r in range(self.d):
            for c in range(self.d):
                if (r, c) == self.pos:
                    print(dir_symbol(self.dir), end='')
                elif self.map[r][c]:
                    print('#', end='')
                elif self.visited[r][c] == 1:
                    print('x', end='')
                else:
                    print('.', end='')
            print()


def dir_symbol(dir):
    r, c = dir

    if c == -1:
        return '<'

    if c == 1:
        return '>'

    if r == 1:
        return 'v'

    if r == -1:
        return '^'

    raise RuntimeError('Unknown direction')


# if __name__ == '__main__':
#     import signal
#
#     print_debug = False
#
#     def signal_handler(sig, frame):
#         global print_debug 
#         print_debug = True
#
#     signal.signal(signal.SIGINT, signal_handler)
#
#
#     # input_file = './test_input'
#     input_file = './input'
#
#     with open(input_file) as raw:
#         input = raw.read()
#
#     f = Floor(input)
#     while not f.done:
#         f.move()
#
#         if print_debug:
#             print_debug = False
#             f.print()
#             print()
#
#     print(sum([sum(r) for r in f.visited]))


# --- Part Two ---
#
# While The Historians begin working around the guard's patrol route, you borrow
# their fancy device and step outside the lab. From the safety of a supply
# closet, you time travel through the last few months and record the nightly
# status of the lab's guard post on the walls of the closet.
#
# Returning after what seems like only a few seconds to The Historians, they
# explain that the guard's patrol area is simply too large for them to safely
# search the lab without getting caught.
#
# Fortunately, they are pretty sure that adding a single new obstruction won't
# cause a time paradox. They'd like to place the new obstruction in such a way
# that the guard will get stuck in a loop, making the rest of the lab safe to
# search.
#
# To have the lowest chance of creating a time paradox, The Historians would like
# to know all of the possible positions for such an obstruction. The new
# obstruction can't be placed at the guard's starting position - the guard is
# there right now and would notice.
#
# In the above example, there are only 6 different positions where a new
# obstruction would cause the guard to get stuck in a loop. The diagrams of these
# six situations use O to mark the new obstruction, | to show a position where
# the guard moves up/down, - to show a position where the guard moves left/right,
# and + to show a position where the guard moves both up/down and left/right.
#
# Option one, put a printing press next to the guard's starting position:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...
#
# Option two, put a stack of failed suit prototypes in the bottom right quadrant
# of the mapped area:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...
#
# Option three, put a crate of chimney-squeeze prototype fabric next to the
# standing desk in the bottom right quadrant:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...
#
# Option four, put an alchemical retroencabulator near the bottom left corner:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...
#
# Option five, put the alchemical retroencabulator a bit to the right instead:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...
#
# Option six, put a tank of sovereign glue right next to the tank of universal solvent:
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..
#
# It doesn't really matter what you choose to use as an obstacle so long as you
# and The Historians can put it into position without the guard noticing. The
# important thing is having enough options that you can find one that minimizes
# time paradoxes, and in this example, there are 6 different positions you could
# choose.
#
# You need to get the guard stuck in a loop by adding a single new obstruction.
# How many different positions could you choose for this obstruction?


from copy import deepcopy


# Pretty much the same as the first solution, but can detect cycles too
class Floor2:
    def __init__(self, input):
        lines = input.strip().split('\n')

        self.done = False
        self.cycle = False

        # Assuming width and height are the same dimension
        self.d = len(lines)

        self.map = [[False for _ in range(self.d)] for _ in range(self.d)]
        self.visited = [[0 for _ in range(self.d)] for _ in range(self.d)]
        self.visited_dirs = {}

        self.pos = None
        self.dir = None

        for r in range(self.d):
            for c in range(self.d):
                if lines[r][c] == '#':
                    self.map[r][c] = True

                if lines[r][c] == '^':
                    self.pos = (r, c)
                    self.dir = (-1, 0)

    def add_block(self, r, c):
        self.map[r][c] = True

    def move(self):
        if self.done:
            return

        r, c, = self.pos
        dr, dc =  self.dir

        nr = r + dr
        nc = c + dc

        outside = nr < 0 or nr >= self.d or nc < 0 or nc >= self.d
        cycle = (nr, nc) in self.visited_dirs and self.dir in self.visited_dirs[(nr, nc)]

        if outside:
            self.done = True
        elif cycle:
            self.done = True
            self.cycle = True
        elif self.map[nr][nc]:
            self.dir = (dc, -dr)
        else:
            self.update_visited((r, c), (dr, dc))
            self.update_visited((nr, nc), (dr, dc))
            self.pos = (nr, nc)

    def update_visited(self, pos, dir):
        r, c = pos
        self.visited[r][c] = 1

        if pos not in self.visited_dirs:
            self.visited_dirs[pos] = set()
        self.visited_dirs[pos].add(dir)

    def print(self):
        for r in range(self.d):
            for c in range(self.d):
                if (r, c) == self.pos:
                    print(dir_symbol(self.dir), end='')
                elif self.map[r][c]:
                    print('#', end='')
                elif self.visited[r][c] == 1:
                    print('x', end='')
                else:
                    print('.', end='')
            print()


if __name__ == '__main__':
    import signal

    print_debug = False

    def signal_handler(sig, frame):
        global print_debug 
        print_debug = True

    signal.signal(signal.SIGINT, signal_handler)

    # input_file = './test_input'
    input_file = './input'

    with open(input_file) as raw:
        input = raw.read()

    search_floor = Floor(input)
    while not search_floor.done:
        search_floor.move()

    og_floor = Floor2(input)

    cycle_count = 0
    for r in range(og_floor.d):
        for c in range(og_floor.d):
            # if never crosses this path, no need to simulate a run
            if not search_floor.visited[r][c]:
                continue

            f = deepcopy(og_floor)
            f.add_block(r, c)

            while not f.done:
                f.move()

                if print_debug:
                    print_debug = False
                    f.print()
                    print('searching', (r, c))
                    print('cycle_count', cycle_count)
                    print()

            if f.cycle:
                cycle_count += 1

    print(cycle_count)
