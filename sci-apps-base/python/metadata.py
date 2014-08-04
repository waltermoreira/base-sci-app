import os
import stat
import subprocess
import time

import requests


# Variables with this prefix are considered metadata
PREFIX = '_'

DOCS_BASE = '/docs'


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
            # give some time to start the tcp server for socket
            time.sleep(1)
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


def collect_files():
    for root, dirs, files in os.walk(DOCS_BASE):
        for name in files:
            filename = os.path.join(root, name)
            st = os.stat(filename)
            if stat.S_ISREG(st[stat.ST_MODE]):
                yield filename, st[stat.ST_MTIME]


def get_files(kind='intro'):
    key = lambda x: x[1]
    # iterate over files sorted by modification time
    for filename, _ in sorted(collect_files(), key=key, reverse=True):
        dir, name = os.path.split(filename)
        if name.startswith(kind):
            yield filename, os.path.basename(dir)
