from PIL import Image
import sys
import os
def celtofare(a):
        f=float(a*1.8+32)
        return float(f)
def faretocel(a):
         c=(a-32)/1.8
         return float(c)
def assigncolor(choice,temp):
    if(choice=='R' or cc=='r'):
        x=temp
        return x
    elif(cc=='G' or cc=='g'):
        y=temp
        return y
    elif(cc=='B' or cc=='b'):
        z=temp
        return z
    
print("Encryption and Decryption Hacks")
print('\n\n\nIs the value in 1.Celsius or 2.Farenheit')
a=int(input())
if a==1 :
               c=float(input('Celsius='))
               f=celtofare(c)
               if c<0:
                       c=float(c*-1)+100
               if f<0:
                       f=float(f*-1)+100
               if c>150 or c<-150 or f>250 or f<-250:
                       print("Range exceeded")
                       sys.exit()
                       
             
elif a==2 :
               f=float(input('Farenheit='))
               c=faretocel(f)
               if c<0:
                       c=float(c*-1)+100
               if f<0:
                       f=float(f*-1)+100
               if c>150 or c<-150 or f>250 or f<-250:
                       print("Range exceeded")
                       sys.exit()

db=(float(f*10)%10)
da=(float(c*10)%10)
d=(da*10)+db
print(float(c))
print(float(f))
print(int(d))
root=input("Enter the path")
file_name=input("Enter the file name")
aa=int(input("Enter the first location"))
ab=int(input("Enter second location"))
cc=input("Color for Celsius ?")
asd=assigncolor(cc,c)
print(asd)
fc=input("Color for Farenheit ?")
if(fc=='R' or fc=='r'):
        x=f
        kf=1
elif(fc=='G' or fc=='g'):
        y=f
        kf=2
elif(fc=='B' or fc=='b'):
        z=f
        kf=3
dc=input("Color for Decimal ?")
if(dc=='R' or dc=='r'):
        x=d
        kd=1
elif(dc=='G' or dc=='g'):
        y=d
        kd=2
elif(dc=='B' or dc=='b'):
        z=d
        kd=3
img = Image.new( 'RGB', (255,255), "black")
pixels = img.load() 
for i in range(img.size[0]):
  for j in range(img.size[1]):
      pixels[i,j] = (int(x), int(y), int(z))
img.show()
pic =Image.open(os.path.join(root, file_name))
r,g,b = img.getpixel((1,1))
pic.putpixel((int(aa),int(ab)),(r,g,b))
pic.show()
key=((str(kc)+str(kf)+str(kd)+str(aa)+str(ab)))
print(key)

