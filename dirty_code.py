#How many of seed users have follower and followee list?
#Do I have the right friends? or is the valid friends_list is a true list?
import os
# from the list of seed users find their friends (network) based on follower and followee folders.

ufile = open("Data/Galaxy_ds/valid_seed_users.txt")
i = 0
def get_list(source):

    f = open(source, 'r')
    friends= set()
    for line in f:
        line = line.strip()
        friends.add(line)
    return friends

def savetofile(uname, friends):
    f = open('Data/Galaxy_ds/Friends/'+uname+".txt", 'w')
    for friend in friends:
        f.write(friend+'\n')

#Form the network

# files = os.listdir('Data/Galaxy_ds/Friends')
# f = open("Data/Galaxy_ds/valid_seed_users_v2.txt", 'w+')
# for file in files:
#     if file.endswith('.txt'):
#         fname , txt = file.split(".txt")
#         f.write(fname+'\n')


#get the list of valid user:
# valid_friends = open("Data/Galaxy_ds/valid_friends_users_v2.txt", 'w+')
# users = open("Data/Galaxy_ds/valid_seed_users_v2.txt")
# for user in users:
#     user = user.rstrip()
#     ufile = open("Data/Galaxy_ds/Friends/"+user+'.txt', 'r')
#     for friend in ufile:
#         friend = friend.rstrip()
#         valid_friends.write(friend+'\n')

valid_friends_unique =

# for uname in ufile:
#     uname = uname.strip()
#     # print(uname)
#     if os.path.isfile( 'Data/Galaxy_ds/follower/' + uname + '.txt') is True and os.path.isfile('Data/Galaxy_ds/followee/' + uname + '.txt') is True:
#         #list of followers
#         follower = get_list('Data/Galaxy_ds/follower/' + uname + '.txt')
#         #list of followees
#         followee = get_list('Data/Galaxy_ds/followee/' + uname + '.txt')
#
#         #intersection of these lists are friends
#
#         friends = followee.intersection(follower)
#
#         savetofile(uname, friends)


