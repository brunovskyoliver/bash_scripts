#!/usr/bin/env bash

w3m -dump "$(cat ~/.cache/last_url)" -o accept_encoding="identity;q=0" -T text/html | ~/.local/scripts/newsboat_formatter.py > ~/.cache/preloaded_buffer
# w3m -dump "$(cat ~/.cache/last_url)" -o accept_encoding="identity;q=0" | python "$(~/.local/scripts/newsboat_formatter.py)"


