import os

LINE = "If attention is all you need, then I've got twelve heads and they're all on you."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
