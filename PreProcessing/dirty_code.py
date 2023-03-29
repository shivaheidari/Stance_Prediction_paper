# from nltk.corpus import opinion_lexicon
#
# oplist = set(opinion_lexicon.words())
# print(len(oplist))
import os
u_list = open("../Data/Galaxy_ds/target_seed.txt", 'r')
users=[]

users_source_dir = "../Data/Galaxy_ds/users_target_tweets"
def find_path(u_name):
  if os.path.exists(users_source_dir + '/' + u_name + '.txt'):
     return users_source_dir + '/' + u_name + '.txt'


for uname in u_list:
    uname = uname.rstrip()
    print(uname)
    print(find_path(uname))
    users.append(uname)

print(len(set(users)))
