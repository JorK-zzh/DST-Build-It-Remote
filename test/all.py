"""Run the Lua 5.1 regression suites and the existing server benchmark."""
import argparse
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("target", nargs="?", default=str(root.parent / "modmain.lua"))
parser.add_argument("--lag-mod", help="Path to the optional client lag mod's modmain.lua")
args = parser.parse_args()
target = str(Path(args.target).resolve())
lag_mod = str(Path(args.lag_mod).resolve()) if args.lag_mod else None
for suite in ("harness.lua", "client.lua", "sync_refresh.lua", "bench.lua"):
    cmd = [sys.executable, str(root / "runner.py"), suite, target]
    if suite == "sync_refresh.lua" and lag_mod:
        cmd.append(lag_mod)
    result = subprocess.run(cmd, cwd=root.parent)
    if result.returncode:
        sys.exit(result.returncode)
