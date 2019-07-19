# -*- coding: utf-8 -*-

import sys

last = None

values = 0.0
beta = 0
N = 4.0

last_data = None

data_dict = {}
final_dict = {}
for l in sys.stdin:
	data = l.strip().split(' ')
	web, value = data[0], float(data[1])

	c_data = data[3:][:]
	if data[2] not in data_dict:
		data_dict[data[2]] = ' '.join(c_data)

	if data[0] != last:
		if last:
			values = (1 - beta) * values + beta / N

			if final_dict:
				for f, v in final_dict.iteritems():
					if data_dict.get(f):
						print '%s %s %s' % (f, v[0], data_dict.get(f))
						data_dict.pop(f, None)
				final_dict = {}

			if data_dict.get(last, None):
				print '%s %s %s' % (last, values, data_dict.get(last, 1))
				data_dict.pop(last, None)
			else:
				final_dict[last] = [values, None]
		last = data[0]
		last_data = data
		values = value
	else:
		values += value

if last and last_data:
	data_dict[last] = ' '.join(last_data[3:][:])
	values = (1 - beta) * values + beta / N
	final_dict[last] = [values, data_dict.get(last, None)]

if final_dict:
	for f, v in final_dict.iteritems():
		if data_dict.get(f):
			print '%s %s %s' % (f, v[0], data_dict.get(f))
			data_dict.pop(f, None)
	final_dict = {}



# print '=====', str(data_dict)