#!env python
from launchpadlib.launchpad import Launchpad
from datetime import datetime
import sys

watchlist = [
	'chihchun', 
	'alextu',
	'cyruslien',
	'fourdollars',
	'kchsieh',
	'lihow731',
	'ycheng-twn',
	'binli',
	'xueshengyao',
]

lp = Launchpad.login_anonymously('Ubuntu Karma Ranking Script', service_root='production', version='1.0')
for name in watchlist:
    person = lp.people(name)
    print ("%s,%s,%s" % (datetime.now().__str__(), person.name, person.karma))
