#!/bin/bash
# Find big files in the repo

git rev-list --objects --all |
    git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
    awk '/^blob/ {print substr($0,6)}' |
    sort --numeric-sort --key=2 |
    cut -d " " -f2- |
    numfmt --field=1 --to=iec-i --suffix=B --padding=7 --round=nearest |
    tail -50
