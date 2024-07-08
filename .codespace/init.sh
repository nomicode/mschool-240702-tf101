#!/bin/sh -e

# Simple shell script in place of a Dockerfile to install dependencies

sudo apt-get update
sudo apt install -y --no-recommends \
    python3-pytest \
    shellcheck
s
udo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
