#!/bin/bash
# Changes directory into the most recent Finder window

target=`osascript -e 'tell application "Finder" to if (count of Finder windows) > 0 then get POSIX path of (target of front Finder window as text)'`
if [ "$target" != "" ]; then
    cd "$target"; pwd
else
    echo 'No Finder window found' >&2
fi