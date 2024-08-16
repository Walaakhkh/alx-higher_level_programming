#!/usr/bin/python3
import sys

def main():
    # sys.argv contains the script name and all command-line arguments
    # sys.argv[1:] skips the script name itself
    total_sum = sum(int(arg) for arg in sys.argv[1:])
    print(total_sum)

if __name__ == "__main__":
    main()
