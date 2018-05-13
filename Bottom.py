


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



path = 'e:\\tee\\'
path = 'E:\\Tee\\Bottom\\'
i = 1
j = 1
for DirIndex in range(1,26):
    newPath = path+str(DirIndex)+'\\';
    items = os.listdir(newPath)
    items.sort(compare)
    for file in items:
        if os.path.isfile(os.path.join(newPath,file))==True:
           new_name=file.replace(file,"1_%04d_B%d_1.png"%(j,i))
           os.rename(os.path.join(newPath,file),os.path.join(newPath,new_name))
           # shutil.copy(os.path.join(newPath,file),os.path.join(newPath,new_name))
           i += 1
           if i%4 == 0:
             j+=1
             i=1
