# /// script
# dependencies = [
#   "numpy",
# ]
# ///
from pathlib import Path
import argparse


def main(input_file: Path):
    print("Hello from day2!")

    with open(input_file, "r") as f:
        safe_reports = [
            test_report_variants(parse_line(line)) for line in f.readlines()
        ]
    # print(f"Safe reports: {safe_reports}")
    print(f"Result: {sum(safe_reports)}")


def parse_line(line: str) -> list[int]:
    return list(map(int, line.split()))


def test_report_variants(report: list[int]) -> bool:
    if report_is_save(report):
        return True
    else:
        for i in range(0, len(report)):
            test_report = report.copy()
            test_report.pop(i)
            if report_is_save(test_report):
                return True
    return False


def report_is_save(report: list[int], max_dist: int = 3) -> bool:
    if report[1] > report[0]:
        increasing = True
    elif report[1] < report[0]:
        increasing = False
    else:
        return False

    for i in range(0, len(report) - 1):
        if increasing and report[i] > report[i + 1]:
            return False
        elif not increasing and report[i] < report[i + 1]:
            return False
        diff = abs(report[i + 1] - report[i])
        if diff == 0 or diff > max_dist:
            return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 2 of Advent of Code 2024")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    main(Path(args.input))
