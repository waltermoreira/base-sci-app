#!/bin/sh

/usr/bin/supervisord -c /etc/supervisor.conf
exec "$@"
