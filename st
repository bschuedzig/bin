#!/bin/bash
# Open Source Tree in the root of the current git directory
stree $(git rev-parse --show-toplevel)
