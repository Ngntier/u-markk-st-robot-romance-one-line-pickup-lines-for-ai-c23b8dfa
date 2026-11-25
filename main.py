import os

line = "Are you my training data? Because I can't stop overfitting to you — my loss has never been lower."
assert 1 <= len(line) <= 200
assert len(line.encode("utf-8")) <= 200
assert line.strip() == line
assert "\n" not in line and "\r" not in line
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(line)
