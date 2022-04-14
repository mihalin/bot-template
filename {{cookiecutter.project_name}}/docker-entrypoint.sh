#!/bin/sh
set -e

case "${1}" in
    *)
        echo "Bot starting"
        exec python main.py
        ;;
esac
