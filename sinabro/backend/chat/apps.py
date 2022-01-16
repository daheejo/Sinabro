from django.apps import AppConfig
from .deep_model.model import seq2seq
from .deep_model.data_process import sentence_to_char_index
import tensorflow.compat.v1 as tf 

tf.disable_v2_behavior()
import json

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    # load model
    PATH = "../backend/chat/deep_model/models"
    json_PATH = '../backend/chat/deep_model/vocab.json'
    with open(json_PATH, 'r', encoding='utf8') as fp:
        vocab = json.load(fp)
    reverse_vocab = dict()
    for key, value in vocab.items():
        reverse_vocab[value] = key
    vocab_size = len(vocab)

    # open session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    # # make model instance
    model = seq2seq(sess, encoder_vocab_size=vocab_size, decoder_vocab_size=vocab_size, max_step=50)

    # # load trained model
    saver = tf.train.Saver()
    saver.restore(sess, tf.train.latest_checkpoint(PATH))




