import argparse
from pathlib import Path

def part1(input: Path) -> int:
    with open(input, "r") as f:
        input = f.read()
    matrix = read_into_2d_list(input)
    

def part2(input: Path) -> int:
    ...

def read_into_2d_list(input: str) -> list[list[str]]:
    return [list(line) for line in input.split("\n")]

def find_letter_at_dist(matrix: list[list[str]], letter: str, row: int, col: int, dist: int) -> int:
    found_positions = []
    if matrix[row-dist][col] == letter:
        found_positions.append((row-dist, col))
    if matrix[row+dist][col] == letter:
        found_positions.append((row+dist, col))
    if matrix[row][col-dist] == letter:
        found_positions.append((row, col-dist))
    if matrix[row][col+dist] == letter:
        found_positions.append((row, col+dist))
    if matrix[row-dist][col-dist] == letter:
        found_positions.append((row-dist, col-dist))
    if matrix[row-dist][col+dist] == letter:
        found_positions.append((row-dist, col+dist))
    if matrix[row+dist][col-dist] == letter:
        found_positions.append((row+dist, col-dist))
    if matrix[row+dist][col+dist] == letter:
        found_positions.append((row+dist, col+dist))
    return found_positions

def scan_for_word(matrix: list[list[str]], row: int, col: int, word: str = "XMAS") -> int:
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != word[0]:
        return 0
    for i in range(1, len(word)):
        

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