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
img = cv2.imread('images/3736456425.jpg')

height, width = img.shape[:2]

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
	cv2.imshow('image',item)
	cv2.waitKey(0)
n = 0
for i in range(4):
	for j in range(4):

		for pixel in img[i*(t_h):(i+1)*(t_h),(j)*(t_w):(j+1)*(t_w)]:
			pixel[0] = rgb[n]
			pixel[1] = rgb[n+1]
			pixel[2] = rgb[n+2]
		n+=3	
cv2.imshow('image',img)

cv2.waitKey(0)

