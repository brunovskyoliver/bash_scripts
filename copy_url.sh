#!/bin/bash
echo "$1" > ~/.cache/last_url
echo "$1" | pbcopy
~/.local/scripts/newsboat_to_txt.sh &
