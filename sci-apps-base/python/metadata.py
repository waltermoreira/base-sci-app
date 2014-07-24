import os
import stat
import traceback

import yaml

ROOT = '/etc/metadata.yml'
BASE = '/etc/metadata.d'


def collect_files():
    for root, dirs, files in os.walk(BASE):
        for name in files:
            filename = os.path.join(root, name)
            st = os.stat(filename)
            if stat.S_ISREG(st[stat.ST_MODE]):
                yield filename, st[stat.ST_MTIME]


def collect_metadata():
    key = lambda x: x[1]
    # iterate over .yml files sorted by modification time
    for filename, _ in sorted(collect_files(), key=key):
        if filename.endswith('.yml'):
            yield read_yml(filename)


def read_yml(filename):
    try:
        return yaml.load(open(filename))
    except Exception:
        print 'Metadata for', filename, 'could not be loaded'
        traceback.print_exc()
        return {}


def get_metadata():
    metadata = read_yml(ROOT)
    for m in collect_metadata():
        metadata.update(m)
    return metadata
