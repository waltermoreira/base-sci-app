import os
import subprocess

import requests


# Variables with this prefix are considered metadata
PREFIX = '_'


def get_metadata():
    metadata = {}
    for k in os.environ:
        if k.startswith(PREFIX):
            metadata[k[1:]] = os.environ[k]
    return metadata


def get_gateway():
    outside_ip = subprocess.Popen(
        'dig +short google.com'.split(),
        stdout=subprocess.PIPE).communicate()[0].splitlines()[0]
    gateway_line = subprocess.Popen(
        'ip route get {0}'.format(outside_ip).split(),
        stdout=subprocess.PIPE).communicate()[0].splitlines()[0]
    return gateway_line.split()[2]


def get_container_info():
    url = 'http://{0}:2375/containers/{1}/json'.format(
        get_gateway(), os.environ['HOSTNAME'])
    all_info = requests.get(url).json()
    return all_info
