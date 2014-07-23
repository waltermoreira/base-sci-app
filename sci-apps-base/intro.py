#!/usr/bin/env python

import os
import optparse
import stat
import sys
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
    except Exception as exc:
        print 'Metadata for', filename, 'could not be loaded'
        traceback.print_exc()
        return {}

def get_metadata():
    metadata = read_yml(ROOT)
    for m in collect_metadata():
        metadata.update(m)
    return metadata

def show_all():
    print "Full metadata:"
    print '---'
    print yaml.dump(get_metadata(), default_flow_style=False)

def main():
    parser = optparse.OptionParser()
    parser.add_option('-v', '--version', dest='version',
                      action='store_true',
                      help='display version of the container')
    options, _ = parser.parse_args()
    if options.version:
        md = get_metadata()
        try:
            print '%s (version %s)' %(md['metadata']['name'],
                                      md['metadata']['version'])
        except KeyError:
            print 'no version info'
        return 0
    show_all()


if __name__ == '__main__':
    sys.exit(main())