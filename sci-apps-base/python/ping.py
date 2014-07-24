#!/usr/bin/env python

import json
import os
import sys

import intro

import requests

SERVER_URL = 'http://example.com'
DISALLOW_PING = '/etc/NO_PING'

def ping_allowed():
    return not os.path.exists(DISALLOW_PING)

def do_ping():
    md = intro.get_metadata()
    resp = requests.post(SERVER_URL, data=json.dumps(md))

def main():
    if ping_allowed():
        do_ping()
    return 0

if __name__ == '__main__':
    sys.exit(main())