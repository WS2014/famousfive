'''
Copyright [2014] [Chirag Nagpal]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


import cPickle as pkl
from sklearn.cluster import KMeans
from numpy import array, mean,	corrcoef, arange
from matplotlib import pyplot as plt
from scipy.stats import spearmanr

vec = pkl.load(open('500vecdic.pkl','rb'))
pos = pkl.load(open('pos.pkl','rb'))
neu = pkl.load(open('neu.pkl','rb'))

#print vec

print type(pos)

print len(vec)
l=[]
n=0
for item in vec:
	n+=1
	#print n
#	print item
	l.append(vec[item])






a = array(l)

cluster = KMeans(n_clusters=10).fit(a)


l = []

for item in vec:
	
	l.append([item,cluster.predict(vec[item])])
	
temp = [[] for i in range(10)]
for item in l:
	temp[(int(item[1][0]))].append(item[0][:-4])

n=0
i=0
for item in temp:

	for point in item:
		if point in pos.keys():
#			print "HERE"
#			print pos[point]
			plt.scatter(n,(pos[point]),color='red',s=10)
                	plt.scatter(n,(neu[point]),color='black',s=10)
	n+=1

plt.show()

red = [[] for i in range(26)]
green = [[] for i in range(26)]
blue = [[] for i in range(26)]

for item in vec:
	
	if item[:-4] not in pos.keys():

		continue

	red[int(vec[item][45]/10)].append(pos[item[:-4]])
	green[int(vec[item][46]/10)].append(pos[item[:-4]])
        blue[int(vec[item][47]/10)].append(pos[item[:-4]])

#	plt.scatter(vec[item][0],pos[item[:-4]],color='red',s=10)
#	plt.scatter(vec[item][1],pos[item[:-4]],color='green',s=10)
#	plt.scatter(vec[item][2],pos[item[:-4]],color='blue',s=10)

plt.plot([i for i in range(26)],[mean(red[i]) for i in range(26)],color='red')
plt.plot([i for i in range(26)],[mean(blue[i]) for i in range(26)],color='green') 
plt.plot([i for i in range(26)],[mean(green[i]) for i in range(26)],color='blue')


plt.show()
plt.savefig('fig_15.png')


spearman = []
pearson = []
for i in range(48):
	l = []
	r = []
	for item in vec:
	        if item[:-4] not in pos.keys():
			continue
		l.append(vec[item][i])
		r.append(pos[item[:-4]])
	
	print "Pearson for " + str(i) + "th:" 
	pearson.append(corrcoef(l,r)[0, 1])
        print "Spearman for " + str(i) + "th:"
	spearman.append(spearmanr(l,r))


plt.bar([i for i in range(48)],[i[0] for i in spearman],color='red')
plt.show()
plt.bar([i for i in range(48)],[i for i in pearson],color='blue')
plt.show()


print temp
pkl.dump(cluster,open('clusteroutput.pkl','wb'))
print a


