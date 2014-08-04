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
    url_template = 'http://{0}:{1}/containers/{2}/json'
    url = url_template.format(get_gateway(), 2375, os.environ['HOSTNAME'])
    try:
        all_info = requests.get(url).json()
    except Exception:
        # docker daemon doesn't seem to be listening in tcp
        # see if socket is mounted in standard place
        try:
            sock = subprocess.Popen(
                'socat -d -d TCP-L:8080,fork '
                'UNIX:/var/run/docker.sock'.split())
            all_info = requests.get(
                url_template.format(
                    '127.0.0.1', 8080, os.environ['HOSTNAME'])).json()
        except Exception:
            all_info = {'hostname': os.environ['HOSTNAME']}
        finally:
            sock.kill()
    return {
        'container_info': all_info,
        'metadata': get_metadata()
    }
