# import gensim.downloader as api
# import pandas as pd
# import nltk
# nltk.download('wordnet')
import os
from gensim.models import KeyedVectors
import Utils
from WordEmbedding.word2vec import word2vec

"""-----------------------private_meyhod_area---------------------"""


def build_glove_w2v(glove_file):
    # convert glove.twitter.27B.200d.txt to glove.twitter.27B.200d.w2v
    from gensim.scripts.glove2word2vec import glove2word2vec
    glove_input_file = glove_file + ".txt"
    glove_wor2vec_output = glove_file + ".w2v"
    glove2word2vec(glove_input_file, glove_wor2vec_output)


def build_glove_model(glove_file_model):
    if not os.path.exists(glove_file_model):
        build_glove_w2v(glove_file_model)
    twitter_vectors = glove_file_model + ".w2v"
    model = KeyedVectors.load_word2vec_format(twitter_vectors, binary=False)
    model.save(glove_file_model)


def create_out_directory(out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


"""-----------------------main_area---------------------"""
source_dir = '../Data/Galaxy_ds/preproc_target_seeds'
out_dir = "../Data/Galaxy_ds/W2Vec/Seed_users_target_tweets"
glove_file_model = "../Data/Galaxy_ds/glove/glove.twitter.27B.200d"
alternative_words_glove_file = '../Data/Galaxy_ds/W2Vec/etc/alternative_words_glove.txt'
alternative_words = Utils.Utils().load_dictionary_with_list_value(alternative_words_glove_file)
create_out_directory(out_dir)
if not os.path.exists(glove_file_model):
    build_glove_model(glove_file_model)
model = KeyedVectors.load(glove_file_model, mmap='r')
processed_file_count = 0
user_list = Utils.Utils().csv_read('../Data/Galaxy_ds/valid_seed_users.txt')

for user in user_list:
    uid = user[0].rstrip()
    if os.path.isfile(out_dir + '/' + uid + '.json') is False:
        w2v_obj = word2vec(uid, source_dir, out_dir, model, alternative_words)
        w2v_obj.glove()
        processed_file_count += 1
        print(processed_file_count)
