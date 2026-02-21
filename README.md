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
