from collections import Counter
from rich.table import Table
from rich.console import Console
import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
with open(path, encoding="utf-8") as f:
    words = [w for w in re.split(r"\W+", f.read().lower()) if w]

counts = Counter(words).most_common(10)

table = Table(title=f"Top 10 words in {path}")
table.add_column("Word")
table.add_column("Count", justify="right")
for w, c in counts:
    table.add_row(w, str(c))

Console().print(table)
