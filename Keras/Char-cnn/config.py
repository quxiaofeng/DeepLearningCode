config = {} 
class TrainingConfig(object):
    
    base_rate = 1e-2
    momentum = 0.9
    decay_step = 150
    decay_rate = 0.95
    epochs = 5
    evaluate_every = 1
    checkpoint_every = 5
class ModelConfig(object):
    conv_layers = [[256, 7, 3],
                   [256, 7, 3],
                   [256, 3, None],
                   [256, 3, None],
                   [256, 3, None],
                   [256, 3, 3]]
    
    fully_connected_layers = [1024, 1024]
    th = 1e-6

    embedding_size = 128
    
    
class Config(object):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    alphabet_size = len(alphabet)
    l0 = 1014
    batch_size = 128
    num_of_classes = 4
    dropout_p = 0.5
    train_data_source = 'data/ag_news_csv/train.csv'
    dev_data_source = 'data/ag_news_csv/test.csv'
    
    training = TrainingConfig()
    
    model = ModelConfig()

config = Config()














