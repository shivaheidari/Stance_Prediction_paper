import codecs
import os
import pycld2 as cld2
import pandas as pd
import re
""" ---------------------private method area----------------------------------------"""


def language_detect(tweet_text):
    try:
        isReliable, textBytesFound, details = cld2.detect(tweet_text)
        if (details[0][2] > 50):
            lang = details[0][1]
        else:
            lang = "non"
    except:
        lang = "non"
    return lang


def tweet_size(tweet_text):
    return len(str(tweet_text).split(' '))


def set_output_directory():
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


def get_file_path(user_name):
    # user might be on of main users or on of main users friends
    if os.path.exists(users_source_dir + '/' + user_name + '.txt'):
        return users_source_dir + '/' + user_name + '.txt'


def process_general_tweets(des_fie, user_name):
    json_tweets = []
    source_file = get_file_path(user_name)
    if source_file == None:
        print(user_name+".txt not exist")
        return
    df_file = pd.read_json(codecs.open(source_file, 'r', 'utf-8'), orient='records', lines=True)
    url_regex = url_regex = r'https?://\S+|www\.\S+|(?!www)\b\w+\.\w+\b'
    url_http_set = url_regex = r'https?://\S+|www\.\S+|[\w-]+(\.[\w-]+)+(/[\w-]*)*'
    mention_regex = r'@\S+'
    # just number strings we don't want to eliminate 2 from CO2
    number_regex = r'\d\d+'
    non_alphanumeric_regex = r'[^((a-zA-Z0-9)+|\s)]'
    combined_regex = f"{mention_regex}|{url_regex}|{number_regex}|{url_http_set}"
    
    df_file['tweet'] = df_file['tweet'].str.replace(combined_regex, ' ',
                                                    case=False)

    #df_file['tweet'] = df_file['tweet'].str.replace(common_topic_regex, ' ', case=False)
    df_file['Language'] = df_file['tweet'].apply(lambda x: language_detect(x))
    df_file = df_file.drop(df_file.loc[df_file['Language'] != 'en'].index)

    # just words
    df_file['tweet'] = df_file['tweet'].str.replace(non_alphanumeric_regex, ' ', case=False)
    # replace unnecessary white space
    df_file['tweet'] = df_file['tweet'].str.replace(r'(\s)+', ' ', case=False)

    df_file["strLen"] = df_file['tweet'].apply(lambda x: tweet_size(x))
    df_file = df_file.drop(df_file.loc[df_file['strLen'] < 4].index)

    # if df_file.index.size >= 0:
    #     with open(des_fie, 'a+', encoding='utf-8') as file:
    #         df_file[['tweet']].to_csv(file, encoding='utf-8', header=False, index=False, newline='\n')
    if df_file.index.size >= 0:
       with open(des_fie, 'a+', encoding='utf-8') as file:
        df_file[['tweet']].to_csv(file, encoding='utf-8', header=False, index=False)

""" ------------------------------main area----------------------------------------"""
# Samsung related topics are common between all users so it has no value for detecting similar users
#common_topic_regex = r'(.+samsung).+'
out_dir = "Data/Galaxy_ds/Topic_Detection/cleaned_Tweets_seeds_general"
users_source_dir = "Data/Galaxy_ds/users_tweets_general"
set_output_directory()
#user_list = open("../out/selected_users.txt", 'r')
user_list = open("Data/Galaxy_ds/valid_seed_users.txt", 'r')
processed_count = 0
for u_name in user_list:
    processed_count += 1
    u_name = u_name.rstrip()
    des = out_dir + "/" + u_name + ".txt"
    if not os.path.exists(des):
               print(u_name)
               process_general_tweets(des, u_name)
    print(str(processed_count))


# import re

# def clean_text(text):
#     # Define a regular expression pattern to match URLs, email addresses, numbers, hashtags, mentions, and multi-segment URLs
#     pattern = r'\b(?:https?://\S+|www\.\S+|mailto:\S+|tel:\S+|@\S+|#\S+|\d+|(?:\w+\.)+\w+(?:/\S+)*)\b'
    
#     # Use re.sub to remove matched patterns and replace with a space
#     cleaned_text = re.sub(pattern, ' ', text, flags=re.IGNORECASE)
    
#     return ' '.join(cleaned_text.split())  # Remove extra spaces and strip

# # Test the clean_text function
# text = "This is a sample text with a URL https://www.example.com, an email address example@email.com, a phone number +1 (555) 123-4567, a hashtag #NLTK, a mention @user123, and a multi-segment URL https://example.com/path/to/resource."
# cleaned_text = clean_text(text)
# print(cleaned_text)

