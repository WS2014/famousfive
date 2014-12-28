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

from pymongo import MongoClient
from matplotlib import pyplot as plt

client = MongoClient()

db = client.flickr

collection = db.comments
n=0

def norm():
	for item in collection.find():
	
		l1 = []
		for item2 in (item['comment'][1]):
	#		print item2[1]
			l1.append(int(item2[1]))

	#	print l
		r1 = [i for i in range(len(l1))]

		l2=[]

		for item2 in (item['comment'][0]):
		        l2.append(int(item2[1]))

		r2 = [i for i in range(len(l2))]

		plt.plot(l1,r1,lw=1,marker='o',linestyle='--')
		plt.plot(l2,r2,lw=1,color='red',marker='o',linestyle='--')
		plt.show()

def diff():
		for item in collection.find():
			temp = int(item['comment'][1][0][1])

			l1 =[]
	  		for item2 in (item['comment'][1]): 
				dy = int(item2[1]) - temp 	
				if (dy!=0):				
					l1.append((1/float(dy)))
				temp = int(item2[1])
			r1 = [i for i in range(len(l1))]

			plt.plot(r1,l1,lw=5,marker='o')

			l2 = []
			if len(item['comment'][0])>0:
				
				temp = int(item['comment'][0][0][1])

				for item2 in (item['comment'][0]):
					dy = int(item2[1]) - temp	
					if (dy!=0):						
						l2.append((1/float(dy)))	

				r2 = [i for i in range( len(l2))]
		

				plt.plot(r2,l2,lw=5,color='red',marker='o')
			plt.show()


norm()
#diff()
