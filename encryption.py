# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:05:22 2017

@author: Kiran
"""
import secrets
import base64
from PIL import Image
import os
libmat = [0 for x in range(40)]
key=[0 for x in range(40)]
txt = 'a'
num = int(-1)
t = int(0)
pt = int(0)
for i in range(26):
    a = secrets.choice(range(0,10))
    b = secrets.choice(range(30,40))
    c = secrets.choice(range(10,20))
    d = secrets.choice(range(20,30))
    if(libmat[a]==0):
        libmat[a]=chr(ord(txt)+i)
    elif(libmat[b]==0):
        libmat[b]=chr(ord(txt)+i)
    elif(txt=='z'):
        break
    elif(libmat[c]==0):
        libmat[c]=chr(ord(txt)+i)
    elif(libmat[d]==0):
        libmat[d]=chr(ord(txt)+i)
    else:
        for j in range (40):
            if(libmat[j]==0):
                libmat[j]=chr(ord(txt)+i)
                break
for i in range (40):
    a = secrets.choice(range(0,10))
    b = secrets.choice(range(30,40))
    c = secrets.choice(range(10,20))
    d = secrets.choice(range(20,30))
    num = num + 1
    if(libmat[a]==0):
        libmat[a]=str(num)
    elif(libmat[b]==0):
        libmat[b]=str(num)
    elif(num==10):
        break
    elif(libmat[c]==0):
        libmat[c]=str(num)
    elif(libmat[d]==0):
        libmat[d]=str(num)
    else:
        for i in range (40):
            if(libmat[i]==0):
                    libmat[i]=str(num)
                    break
for i in range(40):
    if(libmat[i]==0):
        libmat[i]=" "
        break
for i in range(40):
    if(libmat[i]==0):
        libmat[i]="_"
        break
for i in range(40):
    if(libmat[i]==0):
        libmat[i]=","
        break
for i in range(40):
    if(libmat[i]==0):
        libmat[i]="$"
        break
userinput = list(map(str,input().lower()))
inputlen = len(userinput)
mapmat = [0 for x in range(40)]
encodedinput = [0 for x in range(inputlen)]
print(libmat)
incrementer = secrets.choice(range(1,999))
startval = secrets.choice(range(1,9999))
print(startval)
print(incrementer)
for i in range(40):
    mapmat[i]=startval+incrementer*i
print(mapmat)
print(userinput)
for i in range(inputlen):
    tempchar = userinput[i]
    for j in range (40):
        if(tempchar==libmat[j]):
            print(j)
            encodedinput[t]=mapmat[j]
            t=t+1
print(encodedinput)
strout = "".join(str(x) for x in encodedinput)
print(strout)
newsplit = [strout[i:i+2] for i in range(0,len(strout),2)]
print(newsplit)
stringoutlen = len(newsplit)
k=int(0)
img = Image.new( 'RGB', (255,255), "white")
pixels = img.load() 
for i in range(stringoutlen):
  for j in range(stringoutlen):
      newsplit = list(map(int, newsplit))
      if(k==stringoutlen or k>stringoutlen):
          break
      pixels[i,j] = (int(newsplit[k]),int(newsplit[k]),int(secrets.choice(range(0,255))))
      k=k+1
#img.show()
outpath=input("Enter the path")
outname=input("Enter the file name")
fileformat=input('Enter the file format with dot in front')
outname=str(outname+fileformat)
img.save(os.path.join(outpath, outname))
with open(os.path.join(outpath, outname), "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)
keystr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ',',','$','_']
for i in range(40):
    tempvar = keystr[i]
    for j in range(40):
        if(tempvar==libmat[j]):
            key[pt]=mapmat[j]
            pt=pt+1

