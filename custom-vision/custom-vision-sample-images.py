
# coding: utf-8

# In[1]:


import httplib, urllib, base64, json
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

print("All packages loaded ...")


# In[7]:


customvisionapi_key = '69aad4e0a3d4480f89083c9a6231d4c0'
uri_base = 'southcentralus.api.cognitive.microsoft.com'
headers = {
    'Prediction-Key': customvisionapi_key,
    'Content-Type': 'application/octet-stream'
}

filename = '1label_image10016.png'
img_data = open(filename, mode="rb")

print("Variables set")


# In[8]:


get_ipython().magic(u'matplotlib inline')
testimage = Image.open(filename, 'r')
imshow(np.asarray(testimage))


# In[9]:


body = img_data

custom_vision_url = "ce201e8e-ef0e-46d3-a442-ae75f60fb4b5/image?iterationId=474ea099-61e0-4e6e-8ffe-bacec13487d3" #'INSERT YOUR URL FROm CUSTOM VISIOPN MODEL PREDICTIVE URL HERE' 

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)
    conn.request("POST", "/customvision/v2.0/Prediction/" + custom_vision_url, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data.decode())
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    
    conn.close()

except Exception as e:
    print('Error:')
    print(e)


