#!/bin/bash
# Simple BMv2 compile + run script

P4FILE=src/switch1.p4
JSONOUT=configs/basic.json

echo "[*] compiling..."
p4c-bm2-ss $P4FILE -o $JSONOUT

if [ $? -ne 0 ]; then
    echo "[!] Compilation failed"
    exit 1
fi

echo "[*] running simple_switch with $JSONOUT"
simple_switch $JSONOUT
