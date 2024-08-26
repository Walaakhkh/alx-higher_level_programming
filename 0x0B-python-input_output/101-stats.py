#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """

import sys


def print_metrics(file_size, status_codes):
    """ Prints the metrics """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """ Main function to process input and compute metrics """
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) > 6:
                try:
                    status_code = int(parts[6])
                    size = int(parts[7])
                except ValueError:
                    continue

                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size += size

            if line_count % 10 == 0:
                print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)

if __name__ == "__main__":
    main()
