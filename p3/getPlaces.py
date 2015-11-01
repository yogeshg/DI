import requests, json, time, unicodedata, csv

# Utility Functions
def norm(v):
	return unicodedata.normalize('NFKD', unicode(v)).encode('ASCII','replace')

def table2csv(table, csvfile):
	keys=table[0].keys()
	table=[ {k: norm(v) for k,v in row.items()} for row in table]
	with open (csvfile,'wb') as o:
		dw = csv.DictWriter(o,keys)
		dw.writeheader()
		dw.writerows(table)


# Variables
NUM_PLACES=100;

# Configs
url='https://maps.googleapis.com/maps/api/place/nearbysearch/json';
url_details='https://maps.googleapis.com/maps/api/place/details/json';

app_param={
	'key':'AIzaSyCkyaqllz55TVIsNlvbuyPTKJGlIrhkXHQ'
};

loc_param={
	'location':'0,0',
	'radius':'10'
};
locs_param=[
{
	'location':'18.9750,72.8258',
	'radius':'10000',
	'city':'Mumbai'
}
]
;


# Script

# Get and Save places (loc_param)

places=list();
loc_param.update(app_param);
iter_param=dict(app_param);
resp=requests.get(url,params=loc_param).text;

while(len(places)<NUM_PLACES):
	try:
		j=json.loads(resp)
		places.extend([{'placeid':p['place_id'],'name':p['name'],'city':'temp'} for p in j['results']])
		print len(places)
		time.sleep(1)
		iter_param.update({'pagetoken':j['next_page_token']})
		resp=requests.get(url,params=iter_param).text
	except Exception, e:
		print e
		break

table2csv(places,'places.csv')

# save places

reviews=list();
iter_param=dict(app_param);

for p in places:
	try:
		time.sleep(1)
		iter_param.update(p)
		resp=requests.get(url_details,params=iter_param).text
		j=json.loads(resp)
		reviews.extend([{ 'placeid':iter_param['placeid'],'review':r['text']} for r in j['result']['reviews'] ])
		print len(reviews)
	except Exception, e:
		print e


table2csv(reviews,'reviews.csv')
# save reviews







