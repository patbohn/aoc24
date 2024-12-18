import argparse
from pathlib import Path
import re


def main(input_file: Path):
    print("Hello from day3!")
    with open(input_file, "r") as f:
        result = 0
        for line in f.readlines():
            instructions = find_good_instructions(line)
            result += multiply_and_sum_instructions(instructions)
        print(f"Result: {result}")


def find_good_instructions(line: str) -> list[str]:
    return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)


def multiply_and_sum_instructions(instructions: list[str]) -> int:
    return sum(int(inst[0]) * int(inst[1]) for inst in instructions)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 2 of Advent of Code 2024")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    main(Path(args.input))
