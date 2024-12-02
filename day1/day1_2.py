# /// script
# dependencies = [
#   "numpy",
# ]
# ///

import argparse
from pathlib import Path
import re
from collections import Counter


def main(input_file: str):
    print("Hello from day1!")
    regex = re.compile(r"(\d+)\s*(\d+)")
    arr1 = []
    arr2 = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            if match := regex.match(line):
                arr1.append(int(match.group(1)))
                arr2.append(int(match.group(2)))
    counter2 = Counter(arr2)
    result = sum([number * counter2.get(number, 0) for number in arr1])
    print(f"Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 1 of Advent of Code 2024")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    main(Path(args.input))
