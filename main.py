import os

LINE = "I bought the dip so many times my wallet now bills me for therapy — turns out diamond hands just means hugging your losses until they feel like a plan."

if len(LINE) > 280:
    raise ValueError(f"line too long: {len(LINE)} chars")
if "\n" in LINE or "\r" in LINE:
    raise ValueError("line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
