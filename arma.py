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

import numpy as np
from scipy import stats
import pandas
import matplotlib.pyplot as plt
from pymongo import MongoClient
import statsmodels.api as sm
import pickle as pkl

client = MongoClient()
db = client.flickr
collection = db.comments
collection2 = db.arma
x = []
y = []
x1 = []
y1 = []
n=-1

vec = {'dummy':0}
print type(vec)
for item in collection.find():
	print (item['photoid'])
	
	n+=1	
	if len(item['comment'][1])>100 and len(item['comment'][0]) >100:
		print n
		l1 = []
		for item2 in item['comment'][1]:
		    l1.append(int(item2[1]))
		r1 = [i for i in range(len(l1))]
		l2 = []
		for item2 in item['comment'][0]:
		    l2.append(int(item2[1]))
		r2 = [i for i in range(len(l2))]
#		plt.plot(l1,r1,lw=1,marker='o',linestyle='--')
#		plt.plot(l2,r2,lw=1,color='red',marker='o',linestyle='--')
#		plt.show()

		t_min = min(min(l1),min(l2))
		t_max = max(max(l1),max(l2))
		m1 = [0 for i in range(int((t_max-t_min)/3600)+1)]
		m2 = [0 for i in range(int((t_max-t_min)/3600)+1)]

		temp = t_min
		n =0

		for i in range(len(m1)):
		    for item in l1:
			if (item >= temp) and (item < temp+3600):
			    m1[n]+=1
		    temp = temp + 3600
		    n+=1
		#print m1

		temp = t_min

		n=0
		for i in range(len(m2)):
		    for item in l2:
			if (item >= temp) and (item < temp+3600):
			    m2[n]+=1
		    temp = temp + 3600
		    n+=1
		#print m2

#		plt.bar(range(len(m1)),m1)
#		plt.bar(range(len(m1)),m2,color='red')
#		plt.show()
		print max(m1),max(m2)
		
		p = input("Enter p order:")
		q = input("Enter q order:")		
		
		ad_21 = sm.tsa.ARMA(m2, (p,q)).fit()
		print "ARMA Parameters:"
		print ad_21.params
		predicted =  ad_21.predict()
#	    	print "Chi Square:"
#               print stats.chisquare(predicted,m2)
		
	
		plt.plot(range(len(m2)),m2)
		plt.plot(range(len(m2)),predicted,color='red')		
		plt.show()

#		print type(vec)
#		vec[str(item['photoid'])] = {'comments':m1,'ads':m2,'predicted':predicted}
#               collection.insert({'photoid':item['photoid'],'comments':m1,'ads':m2,'predicted':predicted})

#	       	try:
#		      	pkl.dump(vec,open('arma.pkl','wb'))

#		except Exception as e:
#			print e
#			print "ERROR AAGAYA"
#			continue


		

		

