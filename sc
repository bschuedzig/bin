#!/bin/bash
# Executes shellcheck for all files

FILES=$(fd '.sh$')

while read -r file; do

    DIR=$(dirname "$file")
    FILE=$(basename "$file")
    cd "$DIR" || exit 1
    shellcheck -x "$FILE"
    cd - >/dev/null || exit 1

    grep -e "set -" "$file" >/dev/null || {
        echo "$file  (no 'set -e')"
    }

done <<<"$FILES"

echo "(done)"
