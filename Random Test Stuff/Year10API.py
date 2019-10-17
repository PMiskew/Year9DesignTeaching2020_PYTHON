'''
myapi.py 
This is a simple program to demo using a web API with requests Python module.
Later we will add to this example to incorporate our findings into a Webpage
(HTML) format

The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

'''

import requests
import json

# Find APIs at - https://apilist.fun/

def main():

    # use API to get appropriate website info
    # this required signing up but it is free!
    myrequest = requests.get("https://gnews.io/api/v3/top-news?token=e5509443651c0842b01c9142e25ef5f0")
    
    
    # The type of the return value of .json() is a dictionary, 
    # so you can access values in the object by key.

    data_json = myrequest.json()

    x = data_json['articleCount']
    print (x)

    y = data_json['timestamp']
    print (y)

    # trying to grab a specific field from one of the articles....
    #z = data_json['articles[2].get(description)']
    #print (z)
    
    z = data_json['articles'][2]['description']
    print (z)
    
 
# Here is the call to the MAIN function after we have defined when 
# the function defintions are above


main()
