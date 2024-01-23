def get_totla_topics(file):
    file = open(file, 'r')
    topics = set()
    users = file.readlines()
    for user in users:
        user = user.rstrip()
        user_file = open("Data/Galaxy_ds/Topic_Detection/seed_users_topics/"+user+".txt", 'r')
        user_topics = user_file.readlines()
        for line in user_topics:
            parts = line.strip().split(" ")
            key , value = parts
            topics.add(key)
    return topics
topics = get_totla_topics("Data/Galaxy_ds/valid_seed_users.txt")
topic_file = open("Data/Galaxy_ds/Topic_Detection/total_topics.txt", 'w')
for topic in topics:
    topic_file.write(topic + "\n")

    