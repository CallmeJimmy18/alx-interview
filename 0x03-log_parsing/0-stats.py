#!/usr/bin/python3
"""
    log parsing
"""
import sys
import re


def display(log: dict) -> None:
    """
        this displays the stats
    """
    print("File size: {}".format(log["file_size"]))
    for line in sorted(log["code_frequency"]):
        if log["code_frequency"][line]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
       r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    lines = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if (match):
                lines += 1
                code = match.group(1)
                file_size = int(match.group(2))

                log["file_size"] += file_size

                if (code.isdecimal()):
                    log["code_frequency"][code] += 1

                if (lines % 10 == 0):
                    display(log)
    finally:
        display(log)
