#!/bin/bash
# Find big files in the repo

git rev-list --objects --all \
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| awk '/^blob/ {print substr($0,6)}' \
| grep -vF "$(git ls-tree -r HEAD | awk '{print $3}')" \
| sort --numeric-sort --key=2 \
| cut --complement --characters=13-40 \
| numfmt --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
