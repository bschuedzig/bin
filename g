#!/bin/bash
# Short for git / git status

if [[ $# = 0 ]]; then
    git status
else
    git $@
fi
