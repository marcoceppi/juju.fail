#!/usr/bin/env python

import json
import datetime

from citools import check_blockers

data = {}

def format_title(s):
    _, uf = s.split(':', 1)
    return uf.replace('"', '', 1)[::-1].replace('"', '', 1)[::-1].strip()


lp = check_blockers.Launchpad.login_anonymously('juju.fail', 'production', version='devel')

for b in ['1.22', '1.23', '1.24', '1.25' 'master']:
    uhohs = check_blockers.get_lp_bugs(lp, b)

    data[b] = []

    if not uhohs:
        continue

    for bug, bdata in uhohs.iteritems():
        data[b].append({'id': bug, 'url': 'http://pad.lv/%s' % bug,
                        'title': format_title(bdata.title), 'status': bdata.status})


print(json.dumps({'updated': str(datetime.datetime.utcnow()), 'status': data},
                 indent=2))
