#How many of seed users have follower and followee list?
#Do I have the right friends? or is the valid friends_list is a true list?
import os
# from the list of seed users find their friends (network) based on follower and followee folders.

ufile = open("Data/Galaxy_ds/valid_seed_users.txt")
i = 0
for uname in ufile:
    uname = uname.strip()
    # print(uname)
    if os.path.isfile( 'Data/Galaxy_ds/followee/' + uname + '.txt') is False:
        i+=1
print(i)

