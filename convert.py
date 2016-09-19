#!/usr/bin/python


import json
import sys

datafile = 'inc_5000_2015.json'

file = open('datafile', 'r')
data = file.read()
file.close()

fields = ['rank','workers','company','state_s','city','metro','growth','revenue','industry','yrs_on_list']

info = json.loads(data)

for field in fields:
	sys.stdout.write(field + ',')
sys.stdout.write("\n")
sys.stdout.flush()

for company in info:
	for field in fields:
		sys.stdout.write('"' + str(company[field]) + '",')
	sys.stdout.write("\n")
	sys.stdout.flush()

