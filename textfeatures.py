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


import os
import cPickle as pkl
import csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from numpy import mean
from pymongo import MongoClient
#blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
#print blob.sentiment[1]

noise = ['<a href','<img src']
n=[]
text_feat = {}

comments = os.listdir('comments')
client = MongoClient()
db = client.flickr
collection = db.comments
print len(comments)

str = " "


for comment in comments:
	try:
		print comment
        	row_comment=[]
 		row_ad=[]

        	data = pkl.load(open("comments/"+comment,'rb'))	
		for com in data['comments']['comment']:
			flag = 0 
			for item in noise:
				if item in com['_content']:
					flag = 1
				else:
					flag = 0
			if flag:

				row_ad.append([com['_content'],com['datecreate']])	
#                                      row_ad.append([com['_content'],com['datecreate']])
			
			else:
#				senti = TextBlob(com['_content'],analyzer=NaiveBayesAnalyzer()).sentiment[1]
                                row_comment.append([com['_content'],com['datecreate']])
#				print "Working..."
#	               	                row_comment.append([com['_content'],com['datecreate']])
					
		collection.insert({'photoid':comment[:-9],'comment':[row_ad,row_comment]})
                
	except Exception as e:
		print  e
		continue	

	
#print text_feat
