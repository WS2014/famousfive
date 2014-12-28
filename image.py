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

import cv2
import os
import cPickle as pkl



def vectorise(image):
	
#	print image
	img = cv2.imread('images/'+image)
	height, width = img.shape[:2]
	#print height
	#print width



	t_h = height/4
	t_w = width/4

	t = []

	for i in range(4):
		for j in range(4):
		
			t.append(img[i*(t_h):(i+1)*(t_h),(j)*(t_w):(j+1)*(t_w)])
		#	cv2.imshow('image',t)print os.listdir('images')

		#	cv2.waitKey(0)

	T =[]

	rgb = []

	for item in t:
		r_t=0
		g_t=0
		b_t=0
		htemp,wtemp = (item.shape[:2])	
		n = 0	
		temp = []	
		for i in range(htemp):
			for j in range(wtemp):
				r_t+=item[i][j][0]
				g_t+=item[i][j][1]
				b_t+=item[i][j][2]
	
				n+=1
		rgb.append(r_t/n)
		rgb.append(g_t/n)
		rgb.append(b_t/n)	
	

	return rgb


def fun(l):
	for item in l:
		n+=1
		print n
		if item in vec.keys():
			continue

	
		try:
			vec[item]=vectorise(item)
	#		print vec	
			pkl.dump(vec,open('500vecdic.pkl','wb'))
		
		except Exception as e:
			print e
			print "ERROR AT:" + item
			continue




	
a = input("No. of Cores:")



vec = pkl.load(open('500vecdic.pkl','rb'))
n=0

l = os.listdir('images')

for i in range(a):
	fun(l[i*(len(l)/a):(i+1)*(len(l)/a)])











