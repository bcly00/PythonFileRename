import shutil,os

def compare(x, y):
    stat_x = os.stat(newPath + "/" + x)
    stat_y = os.stat(newPath + "/" + y)
    if stat_x.st_mtime < stat_y.st_mtime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0

path = 'E:\\Tee\\Edge\\'

i = 1
j = 1
for DirIndex in range(1,13):
    for DirSub in range(1, 7):
        newPath = path+str(DirIndex)+'\\'+str(DirSub)+"\\"
        items = os.listdir(newPath)
        items.sort(compare)
        Tag = 'E'
        counterI = 1
        counterK = 1
        for file in items:
            if os.path.isfile(os.path.join(newPath,file))==True:
               toke = "1_%04d_%s%d_1.png"%(j,Tag,counterK)
               new_name=file.replace(file,toke)
               os.rename(os.path.join(newPath,file),os.path.join(newPath,new_name))
               # shutil.copy(os.path.join(newPath,file),os.path.join(newPath,new_name))
               if counterI == 8:
                  Tag = "F"
                  counterK = 0
               if counterI == 12:
                  Tag = "G"
                  counterK = 0
               if counterI == 20:
                  Tag = "H"
                  counterK = 0
               counterI += 1
               counterK += 1
        j=j+1