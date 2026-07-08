#!/usr/bin/python3
"""
Need to fill this docstring at the end
"""
import sys
import re


pattern = re.compile(
    r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
)

VALID_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total_size, status_dict):
    """prints metrics given in parameters"""
    print(f"File size: {total_size}")

    for code in VALID_CODES:
        if status_dict.get(code, 0) > 0:
            print(f"{code}: {status_dict[code]}")


if __name__ == "__main__":
    total_size = 0
    counter = 0
    status_code = {}

    try:
        for line in sys.stdin:
            matching_line = pattern.fullmatch(line.strip())

            if matching_line:
                status = matching_line.group(1)
                size = int(matching_line.group(2))
                total_size += size

                if status in VALID_CODES:
                    status_code[status] = status_code.get(status, 0) + 1

                counter += 1

                if counter % 10 == 0:
                    print_stats(total_size, status_code)
        print_stats(total_size, status_code)

    except KeyboardInterrupt:
        print_stats(total_size, status_code)
        raise
