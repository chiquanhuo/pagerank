# -*- coding: utf-8 -*-

import sys
for l in sys.stdin:
	data = l.strip().split(' ')

	webs = data[2:]
	v = 0
	num = len(webs)
	if num > 0:
		v = float(data[1]) / float(num)
	c_web = webs[:]
	for web in webs:
		print '%s %s %s %s' % (web, v, data[0], ' '.join(c_web))
