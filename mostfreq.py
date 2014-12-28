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
import re

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from numpy import mean
from collections import Counter

#blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
#print blob.sentiment[1]

noise = ['<a href','<img src']
n=[]
text_feat = {}

comments = os.listdir('comments')

print len(comments)

str = " "

n=0
for comment in comments[1:500]:
	n+=1
	print n
	try:
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
		
				
				if not flag:
                	                str = str + " " + com['_content']
	except:
		continue	

	
words = re.findall(r'\w+',str)

cap_words = [word.upper() for word in words]

word_count = Counter(cap_words)
word_count.most_common(100)
pkl.dump(word_count,open('word_count.pkl','wb'))
