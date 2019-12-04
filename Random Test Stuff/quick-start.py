#This works 
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key="65d4e71d02134ee38e1fbf37919bde33")

model = app.models.get('demographics')
image = ClImage(url='https://samples.clarifai.com/demographics.jpg')
print(model.predict([image]))

