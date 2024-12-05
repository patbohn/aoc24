import argparse
from pathlib import Path
from enum import Enum


class Direction(Enum):
    N=1
    NE=2
    E=3
    SE=4
    S=5
    SW=6
    W=7
    NW=8

directions = [dir.__repr__() for dir in Direction]

class Position():
    row: int
    col: int
    matrix: list[list[int]]

    def __init__(self, matrix: list[list[int]], row: int, col: int):
        self.row = row
        self.col = col
        self.matrix = matrix

    def move(self, compounded_direction: Direction) -> str | None:
        for direction in compounded_direction:
            match direction:
                case "N":
                    self.row -= 1
                case "E":
                    self.col += 1
                case "S":
                    self.row += 1
                case "W":
                    self.col -= 1
        return self.current_letter
    
    @property
    def current_letter(self):
        if len(self.matrix) > self.row >= 0:
            if len(self.matrix[0]) > self.col >= 0:
                return self.matrix[self.row][self.col]
        return None


def find_letter(matrix: list[list[str]], search_letter: str="X") -> list[Position]:
    positions = []
    for row, rows in enumerate(matrix):
        for col, letter in enumerate(rows):
            if letter == search_letter:
                positions.append(Position(matrix, row, col))
    return positions

def find_string(position: Position, word: str = "XMAS") -> int:
    start_position = position.row, position.col
    count = 0
    for direction in directions:
        for letter in list(word)[1:]:
            if matrix_letter := position.move(direction):
                if letter == matrix_letter: 
                    pass
                else:
                    break
            else:
                break
        # exit loop without breaking means match found
        else:
            count += 1
        position.row, position.col = start_position
    return count

def check_direction(direction: Direction, position: Position, word: str = "MAS"):
    start_position = position.row, position.col
    if word[0] != position.current_letter:
        position.row, position.col = start_position
        return False
    for letter in word[1:]:
        if current_letter := position.move(direction):
            if current_letter == letter:
                pass
            else:
                break
        else:
            break
    else:
        position.row, position.col = start_position
        return True
    position.row, position.col = start_position
    return False

def check_direction_both_ways(direction: Direction, position: Position, word: str = "MAS") -> bool:
    return check_direction(direction, position, word) or check_direction(direction, position, word[::-1])

def find_crosses(position: Position, word: str = "MAS") -> int:
    start_position = position.row, position.col
    # check diagonal fw
    crosses = 0
    if position.move("NW"):
        if check_direction_both_ways("SE", position):
            position.row, position.col = start_position
            if position.move("NE"):
                if check_direction_both_ways("SW", position):
                    crosses += 1
    # position.row, position.col = start_position
    # if position.move("N"):
    #     if check_direction_both_ways("S", position):
    #         position.row, position.col = start_position
    #         if position.move("W"):
    #             if check_direction_both_ways("E", position):
    #                 crosses += 1
    return crosses


def part1(input: Path) -> int:
    with open(input, "r") as f:
        input = f.read()
    matrix = read_into_2d_list(input)
    matches_found = 0
    for x in find_letter(matrix):
        matches_found += find_string(x)
    return matches_found

def part2(input: Path) -> int:
    with open(input, "r") as f:
        input = f.read()
    matrix = read_into_2d_list(input)
    matches_found = 0
    for a in find_letter(matrix, search_letter="A"):
        matches_found += find_crosses(a)
    return matches_found

def read_into_2d_list(input: str) -> list[list[str]]:
    return [list(line) for line in input.split("\n")]



if __name__ == "__main__":
    print("Hello from day4!")
    parser = argparse.ArgumentParser(description="Day 2 of Advent of Code 2024")
    parser.add_argument("part", help="Part 1 or 2")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    if args.part == "1":
        result = part1(Path(args.input))
    elif args.part == "2":
        result = part2(Path(args.input))
    else:
        print("Invalid part")
        exit(1)

    print(f"Result: {result}")