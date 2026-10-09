from __future__ import annotations

import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "FloodDecisionIntelligence-v1.1.zip"

parts = sorted(HERE.glob("part_*.b64"))
if not parts:
    raise SystemExit("No release parts were found.")

payload = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
OUT.write_bytes(base64.b64decode(payload))

print(f"Created: {OUT}")
print(f"Parts: {len(parts)}")
print(f"Bytes: {OUT.stat().st_size}")
