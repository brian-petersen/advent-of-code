# --- Day 4: Ceres Search ---
#
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a
# device and pushes the only button on it. After a brief flash, you recognize the
# interior of the Ceres monitoring station!
#
# As the search for the Chief continues, a small Elf who lives on the station
# tugs on your shirt; she'd like to know if you could help her with her word
# search (your puzzle input). She only has to find one word: XMAS.
#
# This word search allows words to be horizontal, vertical, diagonal, written
# backwards, or even overlapping other words. It's a little unusual, though, as
# you don't merely need to find one instance of XMAS - you need to find all of
# them. Here are a few ways XMAS might appear, where irrelevant characters have
# been replaced with .:
#
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
#
# The actual word search will be full of letters instead. For example:
#
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
#
# In this word search, XMAS occurs a total of 18 times; here's the same word
# search again, but where letters not involved in any XMAS have been replaced
# with .:
#
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
#
# Take a look at the little Elf's word search. How many times does XMAS appear?


from dataclasses import dataclass


TARGET = 'XMAS'
TARGET_LEN = len(TARGET)


@dataclass
class Maze:
    maze: list[str]
    width: int
    height: int


def parse_input(raw):
    maze = []

    for line in raw:
        maze.append(line.strip())

    return Maze(maze=maze, width=len(maze[0]), height=len(maze))


def check(r, c, vr, vc, maze: Maze):
    er = r + vr*(TARGET_LEN-1)
    if er < 0 or er >= maze.height:
        return False

    ec = c + vc*(TARGET_LEN-1)
    if ec < 0 or ec >= maze.width:
        return False

    for i in range(TARGET_LEN):
        nr = r + vr*i
        nc = c + vc*i

        if maze.maze[nr][nc] != TARGET[i]:
            return False

    return True


def print_dotted_board(r, c, vr, vc, maze: Maze):
    points = generate_points(r, c, vr, vc)

    for r in range(maze.height):
        for c in range(maze.width):
            if (r, c) not in points:
                print('.', end='')
            else:
                print(maze.maze[r][c], end='')
        print('')


def generate_points(r, c, vr, vc):
    return [(r + vr*i, c + vc*i) for i in range(TARGET_LEN)]


# if __name__ == '__main__':
#     # input = './test_input'
#     input = './input'
#
#     with open(input) as raw:
#         maze = parse_input(raw)
#
#     search_vertices = [
#         (0, 1),   # right
#         (0, -1),  # left
#         (1, 0),   # down
#         (-1, 0),  # up
#         (1, 1),   # right up
#         (-1, 1),  # right down
#         (1, -1),  # left up
#         (-1, -1), # left down
#     ]
#
#     # final_board = [['.'] * maze.width for _ in range(maze.height)]
#
#     count = 0
#     for r in range(maze.height):
#         for c in range(maze.width):
#             for vr, vc in search_vertices:
#                 if check(r, c, vr, vc, maze):
#                     count += 1
#
#                     # print_dotted_board(r, c, vr, vc, maze)
#                     # print()
#
#                     # for tr, tc, in generate_points(r, c, vr, vc):
#                     #     final_board[tr][tc] = maze.maze[tr][tc]
#
#     # for i in range(len(final_board)):
#     #     print(''.join(final_board[i]))
#
#     print(count)


# --- Part Two ---
#
# The Elf looks quizzically at you. Did you misunderstand the assignment?
#
# Looking for the instructions, you flip over the word search to find that this
# isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to
# find two MAS in the shape of an X. One way to achieve that is like this:
#
# M.S
# .A.
# M.S
#
# Irrelevant characters have again been replaced with . in the above diagram.
# Within the X, each MAS can be written forwards or backwards.
#
# Here's the same example from before, but this time all of the X-MASes have been
# kept instead:
#
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
#
# In this example, an X-MAS appears 9 times.
#
# Flip the word search from the instructions back over to the word search side
# and try again. How many times does an X-MAS appear?


def check2(r, c, maze: Maze):
    m = maze.maze

    if r <= 0 or r >= maze.height-1:
        return False

    if c <= 0 or c >= maze.width-1:
        return False

    if m[r][c] != 'A':
        return False

    mas1 = (m[r-1][c-1] == 'M' and m[r+1][c+1] == 'S') or \
            (m[r-1][c-1] == 'S' and m[r+1][c+1] == 'M')
    if not mas1:
        return False

    mas2 = (m[r+1][c-1] == 'M' and m[r-1][c+1] == 'S') or \
            (m[r+1][c-1] == 'S' and m[r-1][c+1] == 'M')
    if not mas2:
        return False

    return True


if __name__ == '__main__':
    # input = './test_input'
    input = './input'

    with open(input) as raw:
        maze = parse_input(raw)

    # final_board = [['.'] * maze.width for _ in range(maze.height)]

    count = 0
    for r in range(maze.height):
        for c in range(maze.width):
            if check2(r, c, maze):
                count += 1

                # final_board[r][c] = maze.maze[r][c]
                # final_board[r-1][c-1] = maze.maze[r-1][c-1]
                # final_board[r-1][c+1] = maze.maze[r+1][c+1]
                # final_board[r+1][c-1] = maze.maze[r+1][c+1]
                # final_board[r+1][c+1] = maze.maze[r+1][c+1]

    # for i in range(len(final_board)):
    #     print(''.join(final_board[i]))

    print(count)
