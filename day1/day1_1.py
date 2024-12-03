# /// script
# dependencies = [
#   "numpy",
# ]
# ///

import argparse
from pathlib import Path
import numpy as np
import re


def main(input_file: Path):
    print("Hello from day1!")
    regex = re.compile(r"(\d+)\s*(\d+)")
    arr1 = []
    arr2 = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            if match := regex.match(line):
                arr1.append(int(match.group(1)))
                arr2.append(int(match.group(2)))
    result = np.sum(np.abs(np.sort(arr1) - np.sort(arr2)))
    print(f"Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 1 of Advent of Code 2024")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    main(Path(args.input))
