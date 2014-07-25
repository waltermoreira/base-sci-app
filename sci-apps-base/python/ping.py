#!/usr/bin/env python

import json
import os
import sys
import datetime

import metadata

import requests

SERVER_URL = os.environ['SERVER_URL']


def ping_allowed():
    return not os.environ.get('NO_PING', False)


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
