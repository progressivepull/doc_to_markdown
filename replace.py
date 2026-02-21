#!/usr/bin/env python3

# Arrays of patterns
before = ["`$", "$`", "``` math", "```"]
after  = ["$", "$", "$$", "SS"]

def replace_all(text, before, after):
    for b, a in zip(before, after):
        text = text.replace(b, a)
    return text

def main():
    input_file = "main.md"
    output_file = "final.md"

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    updated = replace_all(content, before, after)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Created {output_file}")

if __name__ == "__main__":
    main()
