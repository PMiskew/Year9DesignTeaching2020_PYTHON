import cv2
import time
from clarifai.rest import ClarifaiApp

# Create your API key in your account's Application details page:
# https://clarifai.com/apps

app = ClarifaiApp(api_key='65d4e71d02134ee38e1fbf37919bde33')

# You can also create an environment variable called `CLARIFAI_API_KEY`
# and set its value to your API key.
# In this case, the construction of the object requires no `api_key` argument.

app = ClarifaiApp()

model = app.models.get('face-v1.3')

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
	time.sleep(1)  

cv2.destroyWindow("preview")