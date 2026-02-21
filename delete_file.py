#!/usr/bin/env python3
import os

def main():
    filename = "main.md"

    # Check if file exists before deleting
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
    else:
        print(f"{filename} does not exist")

if __name__ == "__main__":
    main()
