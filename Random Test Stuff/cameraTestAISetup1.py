#This works 
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key="65d4e71d02134ee38e1fbf37919bde33")

model = app.models.get('a403429f2ddf4b49b307e318f00e528b')
image = ClImage(url='http://0.0.0.0:8000/testPhoto.jpg')


#image = ClImage(url='https://samples.clarifai.com/demographics.jpg')
tags = (model.predict([image]))

#print(tags)
#print("*******************")
#for i in range (0, 3, 1):
	#print(tags['outputs'][0]['data']['regions'][i])