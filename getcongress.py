import os
import urllib2
import json
from time import sleep
import psycopg2


def processChamber(congress, chamber):

	politician_url = 'https://api.propublica.org/congress/v1/'+str(congress)+'/'+str(chamber)+'/members.json'

	request = urllib2.Request(politician_url, headers={"X-API-KEY" : os.environ['PROPUBLICAAPIKEY']})
	b = urllib2.urlopen(request).read()
	j = json.loads(b)

	members = j['results'][0]['members']


	politicians = []

	for member in members:

		parsed_member = parseMember(member)

		politicians.append(parsed_member)

	#export to wherever you want
	exportPoliticians(politicians)

congress = 116
chambers = ['Senate','House']

politicians = []
for chamber in chambers:
	ps = processChamber(congress, chamber)

