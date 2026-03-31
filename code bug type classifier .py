"""
data_prep.py — Bug Dataset Builder
Code Bug Type Classifier | BYOP Project
"""

import csv
import os
import random

random.seed(42)

# ── Step 1: Clean code snippets ──────────────────────────

clean_snippets = [
    "def add(a, b):\n    return a + b\nprint(add(3, 4))",
    "numbers = [1, 2, 3]\nfor n in numbers:\n    print(n)",
    "def is_even(n):\n    if n % 2 == 0:\n        return True\n    return False",
    "name = 'Alice'\nage = 25\nprint(name, age)",
    "items = ['apple', 'banana']\nfor i in range(len(items)):\n    print(items[i])",
    "x = 10\ny = 2\nprint(x + y)\nprint(x * y)",
    "def greet(name):\n    return 'Hello ' + name\nprint(greet('Bob'))",
    "scores = [80, 90, 70]\naverage = sum(scores) / len(scores)\nprint(average)",
]


# ── Step 2: Bug injectors ─────────────────────────────────

def inject_syntax_error(code):
    # Remove colon from first def/if/for line
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if line.strip().endswith(":"):
            lines[i] = line.rstrip()[:-1]
            return "\n".join(lines)
    return code + "\nprint('hello'"   # unclosed bracket fallback

def inject_logic_error(code):
    # Flip a comparison or operator
    if "% 2 == 0" in code:
        return code.replace("% 2 == 0", "% 2 == 1")
    if " + " in code:
        return code.replace(" + ", " - ", 1)
    return code.replace("True", "False")

def inject_runtime_error(code):
    # Add index out of range
    return code + "\nprint(items[99])"

def inject_type_error(code):
    # Add string + int
    return code + '\nresult = "score: " + 100'

def inject_name_error(code):
    # Use an undefined variable
    return code + "\nprint(total_score)"


# ── Step 3: Build dataset ─────────────────────────────────

injectors = {
    "syntax_error":  inject_syntax_error,
    "logic_error":   inject_logic_error,
    "runtime_error": inject_runtime_error,
    "type_error":    inject_type_error,
    "name_error":    inject_name_error,
}

rows = []

for snippet in clean_snippets:
    for label, inject in injectors.items():
        bugged_code = inject(snippet)
        rows.append({"code": bugged_code, "label": label})

random.shuffle(rows)


# ── Step 4: Save to CSV ───────────────────────────────────

os.makedirs("data", exist_ok=True)

with open("data/dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["code", "label"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Done! {len(rows)} samples saved to data/dataset.csv")

# Quick check
from collections import Counter
counts = Counter(r["label"] for r in rows)
for label, count in sorted(counts.items()):
    print(f"  {label}: {count} samples")