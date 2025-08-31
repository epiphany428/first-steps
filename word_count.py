# 使い方: python3 word_count.py sample.txt
import sys
import re
from collections import Counter

def tokenize(text: str):
    # 英数字の単語で分割（小文字化）。日本語は対応外でOK（後で拡張）。
    return [w for w in re.split(r"\W+", text.lower()) if w]

path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"

with open(path, "r", encoding="utf-8") as f:
    words = tokenize(f.read())

for word, cnt in Counter(words).most_common(10):
    print(f"{word}\t{cnt}")