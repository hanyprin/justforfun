import os
import os.path
filelist=os.listdir("F:\\注会\\税法\\刘颖\\mp3\\东奥税法")
dirc="F:\\注会\\税法\\刘颖\\mp3\\东奥税法"
for l in filelist:
    name=l.replace('13注会税法·刘颖基础班·','')
    newdirc=os.path.join(dirc,name)
    olddirc=os.path.join(dirc,l)
    os.rename(olddirc,newdirc)
    
