#Change File Names in batches

import os
import os.path

filelist=os.listdir("F:\\")
dirc="F:\\"
for l in filelist:
    name=l.replace('tobereplaced','')
    newdirc=os.path.join(dirc,name)
    olddirc=os.path.join(dirc,l)
    os.rename(olddirc,newdirc)
    
