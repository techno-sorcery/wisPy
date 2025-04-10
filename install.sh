#!/bin/bash
if test -f "~/.local/bin/wispy"; then
    rm ~/.local/bin/wispy
fi

cp wispy ~/.local/bin
