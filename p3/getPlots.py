import csv, nltk

def csv2table(csvfile):
	table=list()
	with open(csvfile) as f:
		reader = csv.DictReader(f)
		for row in reader:
			table.append(row)
	return table

def kvpairs2table(kvfile):
	table=list()
	with open(kvfile) as f:
		for l in f:
			try:
				table.append(dict([kv.split('=') for kv in l.split()]))
			except:
				continue
	return table


rs=csv2table('reviews.csv')

txt=[r['review'] for r in rs]

tagd=[nltk.pos_tag(nltk.word_tokenize(t)) for t in txt]

tags=[tag for sl in tagd for (txt,tag) in sl]
f1=nltk.FreqDist(tags)
f1.plot()
f1.tabulate()

jjs=[txt for sl in tagd for (txt,tag) in sl if tag==('JJ')]
f2=nltk.FreqDist(jjs)
f2.plot()
f2.tabulate()

ws= {}
for item in kvpairs2table('words.tff'):
   word1 = item.pop('word1')
   ws[word1] = item

d_words=[ {'word':w, 'count':c} for (w,c) in f2.items()[0:15] ]

p_words=[w for w in d_words if (w['word'] in ws.keys()) and ws[w['word']]['priorpolarity']=='positive']
n_words=[w for w in d_words if (w['word'] in ws.keys()) and ws[w['word']]['priorpolarity']=='negative']

sum([w['count'] for w in p_words])
([w['word'] for w in p_words])
sum([w['count'] for w in n_words])
([w['word'] for w in n_words])


