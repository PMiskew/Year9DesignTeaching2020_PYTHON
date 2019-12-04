from clarifai.rest import ClarifaiApp

65d4e71d02134ee38e1fbf37919bde33

app = ClarifaiApp()

app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg', concepts=['my puppy'])
app.inputs.create_image_from_url(url='https://samples.clarifai.com/wedding.jpg', not_concepts=['my puppy'])