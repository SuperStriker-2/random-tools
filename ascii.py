from PIL import Image
import math

REFERENCE="ssss.png"
WIDTH=100

#resizing the image
im = Image.open(REFERENCE)
width,height=im.size
newidth=WIDTH
sf=newidth/width
newheight=int(0.5*height*sf)
im = im.resize((newidth,newheight), Image.Resampling.LANCZOS)

#actually performing operation
pixels = list(im.getdata())
width,height=im.size
chars=['.', '-', ':', '=', '+', 'x', '#', '%', '@']
val=0
strin=""
newlist=[]
for i in pixels:
    val=(i[0]+i[1]+i[2])/3
    val=len(chars)*val/255
    val=math.ceil(val)-1
    newlist.append(chars[val])
for i in range(len(newlist)):
    if i%width==0:
        strin+="\n"
    strin+=newlist[i]
with open("newfile.txt","w") as file:
    file.write(strin)
