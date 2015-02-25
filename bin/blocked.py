#!/usr/bin/env python

import json
import datetime

from citools import check_blockers

class AllTheThings(object):
    pass

args = AllTheThings()
data = {}

def format_title(s):
    _, uf = s.split(':', 1)
    return uf.replace('"', '', 1)[::-1].replace('"', '', 1)[::-1].strip()


for b in ['1.20', '1.21', 'master']:
    args.branch = b
    uhohs = check_blockers.get_lp_bugs(args)

    data[b] = []

    if not uhohs:
        continue

    for bug, bdata in uhohs.iteritems():
        data[b].append({'id': bug, 'url': 'http://pad.lv/%s' % bug,
                        'title': format_title(bdata['title']), 'status': bdata['status']})


print(json.dumps({'updated': str(datetime.datetime.utcnow()), 'status': data},
                 indent=2))
