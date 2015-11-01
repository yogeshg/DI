import csv, nltk, numpy

import matplotlib.pyplot as plt


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

def getTopQuantileIdx(fq,q):
	cs=([w[1] for w in fq.items()])
	cumsum=q*sum(cs)
	# print cumsum
	for i in range(len(cs)):
		cumsum=cumsum-cs[i]
		if(cumsum<0):
			break
	return i

def save_plot(p_words_fd,n_words_fd,cname):
	plt.bar(numpy.arange(len(p_words_fd)), [w[1] for w in p_words_fd], 1, color='g',alpha=0.25)
	plt.bar(numpy.arange(len(n_words_fd)), [w[1] for w in n_words_fd], 1, color='r',alpha=0.25)
	[plt.text(i,p_words_fd[i][1],p_words_fd[i][0]) for i in range(len(p_words_fd))]
	[plt.text(i,n_words_fd[i][1],n_words_fd[i][0]) for i in range(len(n_words_fd))]
	# plt.show()
	plt.savefig('plot_'+cname+'.png')

def get_score(p_words_fd,n_words_fd):
	p=sum([w[1] for w in p_words_fd])
	n=sum([w[1] for w in n_words_fd])
	return (p-n)/float(p+n)


def analyse(cname):
	fname='reviews_'+cname+'.csv'
	rs=csv2table(fname)
	txt=[r['review'] for r in rs]
	tagd=[nltk.pos_tag(nltk.word_tokenize(t)) for t in txt]
	# tags=[tag for sl in tagd for (txt,tag) in sl]
	# f1=nltk.FreqDist(tags)
	jjs=[txt for sl in tagd for (txt,tag) in sl if tag==('JJ')]
	f2=nltk.FreqDist(jjs)
	ws={}
	for item in kvpairs2table('words.tff'):
	   word1 = item.pop('word1')
	   ws[word1] = item
	f2_half=f2.items()[0:getTopQuantileIdx(f2,0.5)]
	p_words_fd=([w for w in f2_half if (w[0] in ws.keys()) and ws[w[0]]['priorpolarity']=='positive'])
	n_words_fd=([w for w in f2_half if (w[0] in ws.keys()) and ws[w[0]]['priorpolarity']=='negative'])
	print 'Score for '+fname+':', get_score(p_words_fd,n_words_fd)
	save_plot(p_words_fd,n_words_fd,cname)



analyse('Bombay')
# analyse('NewYork')
