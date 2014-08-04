#!/bin/sh

export PATH=$PATH:/root/python/bin

/usr/bin/supervisord -c /etc/supervisor.conf
if [[ ("$#" -eq 0) || ("$1" =~ ^-.*) ]]; then
    # no arguments, or something that looks like an option:
    # redirect to 'intro' to show docs, etc.
    exec intro "$@"
else
    exec "$@"
fi
