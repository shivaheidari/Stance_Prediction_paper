
network_file = "./Data/Galaxy_ds/Implicit_Network/seed_network_0.8.txt"

user_network_dict = {}



def get_network():
    with open(network_file) as network:
        for line in network:
            line = line.rstrip()
            user, friend, influence_score = line.split(" ")
            if user in user_network_dict:
                user_network_dict[user].append((friend, influence_score))
            else:
                    user_network_dict[user] = [(friend, influence_score)]

    return user_network_dict
