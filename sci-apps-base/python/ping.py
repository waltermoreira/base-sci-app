#!/usr/bin/env python

import json
import os
import sys
import datetime

import metadata

import requests

SERVER_URL = 'http://192.168.59.3:5000'
DISALLOW_PING = '/etc/NO_PING'


def ping_allowed():
    return not os.path.exists(DISALLOW_PING)


def do_ping():
    md = metadata.get_metadata()
    md['timestamp'] = datetime.datetime.now().isoformat(' ')
    resp = requests.post(SERVER_URL, data=json.dumps(md),
                         headers={'Content-Type': 'application/json'})


def main():
    if ping_allowed():
        do_ping()
    return 0


if __name__ == '__main__':
    sys.exit(main())
