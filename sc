#!/bin/bash
# Executes shellcheck for all files

FILES=$(fd '.sh$')

while read -r file; do
    shellcheck "$file"
    grep -e "set -" "$file" >/dev/null || {
        echo "$file  (no 'set -e')"
    }
done <<<"$FILES"

echo "(done)"
