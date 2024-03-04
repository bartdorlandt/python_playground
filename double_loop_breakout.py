#!/usr/bin/env python3

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def is_what_i_want(*args):
    pass


def do_something(*args):
    pass


# Can't break out of a double loop
for row in board:
    for cell in row:
        if is_what_i_want(cell):
            do_something(cell)
            break  # ??? :(


# possible solution, using generators
# this and the next one are actually the same thing
# def cells(board):
#     """Iterate over the cells in a 2D list"""
#     for row in board:
#         for cell in row:
#             yield cell


def cells(board):
    """Iterate over the cells in a 2D list."""
    for row in board:
        yield from row


for cell in cells(board):
    if is_what_i_want(cell):
        do_something(cell)
        break  # !!! :)
