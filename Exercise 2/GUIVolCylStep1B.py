import math


#Function: A small segment of code that can be called upon and run
#What it takes
#What it does/What it's name is
#What it returns

'''
This function takes radius and height and returns the volume.
If the passed values are invalid it returns -1
'''
def calcVolumeCylinder(radius, height):

	
	if (radius >= 0 and height >= 0):

		volume = math.pi * pow(radius,2) * height
		volume = round(volume,2)
		return volume
	else:
		return -1
	

	

print("Start Program")
result = calcVolumeCylinder(3,4)
print(result)
print("End Program")






