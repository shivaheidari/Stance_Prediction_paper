import glob
uname_list= []

import sys,glob
import os



for fileName_relative in glob.glob("../Data/Galaxy_ds/preproc_target_friends/*.txt",recursive=True):

    fileName_absolute = os.path.basename(fileName_relative)

    # print("Only file name: ", fileName_absolute)
    unmaes,t = fileName_absolute.split(".txt")
    uname_list.append(unmaes)

    # uname_files.append(fileName_absolute)
print(uname_list)
ufile = open("../Data/Galaxy_ds/valid_friends_users.txt", 'w+')
for user in uname_list:
    ufile.write(user+'\n')