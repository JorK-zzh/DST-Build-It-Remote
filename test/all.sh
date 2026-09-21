#!/usr/bin/env bash
# 跑全部测试。用法: bash test/all.sh [modmain路径]
set -e
cd "$(dirname "$0")/.."
PY="${PY:-python}"
"$PY" test/all.py "$@"
