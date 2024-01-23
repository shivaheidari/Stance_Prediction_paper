#list of users: valid users seed
# input: detected topic for each users from Galaxy/topic_Detection/seeds_users_topics
#output : weighted network of users based on jaccard of topics



#read users name

import math


file = open("Data/Galaxy_ds/valid_seed_users.txt", 'r')

users = file.readlines()

edge_num = 0
node_num = 0
all_topics = open("Data/Galaxy_ds/Topic_Detection/total_topics.txt", 'r')
network = open("Data/Galaxy_ds/seed_network_0.8.txt", 'w')
all_topics = all_topics.readlines()

all_topics = [topic.rstrip() for topic in all_topics]


def topic_to_dict(file):
    my_dict = {}
    for line in file:
        parts = line.strip().split(" ")
        if len(parts) == 2:
            key, value = parts
            my_dict[key] = value

    return my_dict

def similarity(topics1,topics2):
    dict1 = topics1
    dict2 = topics2
    intersection = dict((key, value) for key, value in dict1.items() if key in dict2)
    print(len(intersection))
    var1 = len(topics1)/len(all_topics)
    var2 = len(topics2)/len(all_topics)
    #sim = (len(intersection)/ (min(len(topics1), len(topics2)))) * math.log(1/max(var1,var2))
    #normalize by the maximum number of topics
    sim = (len(intersection)/ (min(len(topics1), len(topics2))))
    return sim
    
    
# similarity({'a': 1, 'b': 8, 'd9': 3,'e':0}, {'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6})

for user1 in users:
    
    node_num += 1
    for user2 in users:
        user1 = user1.rstrip()
        user2 = user2.rstrip()
        if user1 != user2:
            u1_file  = open("Data/Galaxy_ds/Topic_Detection/seed_users_topics/"+user1.rstrip()+".txt", 'r')
            u2_file = open("Data/Galaxy_ds/Topic_Detection/seed_users_topics/"+user2.rstrip()+".txt", 'r')  
            u1_topis = topic_to_dict(u1_file)
            u2_topis = topic_to_dict(u2_file)
            sim = similarity(u1_topis, u2_topis)
            #[0.5-0.9]
            if sim >0.8:
                network.write(user1 + " " + user2 + " " + str(sim) + "\n")
                #intersection of topics 
                edge_num += 1
                print(user1, user2, sim)

