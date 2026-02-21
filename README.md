
# Microsoft Document to Markdown

## Convert Mirosoft Word Documents to Markdown

* [Pandoc a Universal Document Converter](https://pandoc.org/)
* [How to Convert a Word Document to Markdown for Free using Pandoc](https://www.youtube.com/watch?v=HPSK7q13-40)
* [Download Software](https://github.com/jgm/pandoc)

That command is a compact little powerhouse, and each piece plays a
specific role. Breaking it down makes the whole thing feel much more
intuitive.

``` bash
pandoc -t gfm --extract-media . "main.docx" -o main.md
```

## Command Line

### Change Directory

**Git Bash**
``` Bash
cd /D/pinkt/Documents/OneDrive/Desktop/doc_to_markdown
```

**Microsoft Power Shell**
```
$ cd D:\pinkt\Documents\OneDrive\Desktop\doc_to_markdown
```

# Code  

##  Search to Change Characters in File

Here you go — a clean, reproducible setup that gives you:

- A **Bash script** that calls

- A **Python script** that reads **main.md**,

- Replaces items from a **before‑array** with items from an
  **after‑array**,

- And writes the result to **final.md**.

Everything is shown with a clear file structure, and all code is ready
to run.

**📁 File Structure**

Code

project/

```

│

├── run.sh

├── replace.py

└── main.md
```

You can explore each component further using File structure or
Replacement logic.

**🐍 replace.py (Python Program)**

``` python

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

```

You can dive deeper into Python arrays or File reading.

**🖥️ run.sh (Bash Script)**

``` bash

#!/bin/bash

# Run the Python replacement script

python3 replace.py
```

Make it executable:

``` Code

chmod +x run.sh
```

Run it:

``` Code

./run.sh
```
## 🐍 Updated replace.py — now deletes main.md

Here’s a clean rewrite of your Python program so that instead of reading main.md, it deletes it.

``` python
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


```
