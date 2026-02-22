#!/usr/bin/env python3
import os
import sys

def main():
    # Make sure the user passed a filename
    if len(sys.argv) != 2:
        print("Usage: python delete_file.py <filename>")
        return

    filename = sys.argv[1]

    # Check if file exists before deleting
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
    else:
        print(f"{filename} does not exist")

if __name__ == "__main__":
    main()

