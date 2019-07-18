# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from bs4 import BeautifulSoup
import urllib.request
import os
import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

# user input
query = input("Image research : ")

# handle spaces from the user
query= query.split()
folder_name = '_'.join(query)
print("folder name")
print(folder_name)
query='+'.join(query)

# url for the google search
url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

# avoid 403 forbidden error
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

soup = get_soup(url,headers)

# contains the link for Large original images, type of  image
ActualImages=[]

# store for each image a tuple --> url/type
for a in soup.find_all("div",{"class":"rg_meta"}):
    link, Type=json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("Total number of images we are supposed to download : ",len(ActualImages))

# index of image to save it with different name
ind_img = 0

# create a folder for the user research if it does not exists yet
dirName = folder_name
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


# go through all the url we received
for images in ActualImages:
    
    print(ind_img)
    print(images[1])
    
    try:
        # store the url and the type
        url_address = images[0]
        img_type = images[1]
        
        # The assembled request
        request_=urllib.request.Request(url_address,None,headers) 
        
        # store the response
        response = urllib.request.urlopen(request_) 
        
        # test if the image extension is correct
        accepted_extension = {'jpg', 'png', 'gif'}
        if img_type in accepted_extension:
            #create a new file and write the image
            f = open(folder_name + '/' + folder_name + '_' + str(ind_img) + '.' + img_type, 'wb')
            f.write(response.read())
            f.close()
            ind_img += 1
        

    except Exception as e:
        print ("Could not load : " + images[0])
        print ("Error : " + e)
       

