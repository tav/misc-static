#! /bin/sh

# ideally just this would work:
# curl -D headers --head $@ > /dev/null

curl -D headers $@ > /dev/null
