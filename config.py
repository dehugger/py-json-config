from json import loads, dumps
from copy import deepcopy
from pprint import pformat

class Config:
    '''
    loaded_config = filepath to the configuration file. The default loaded is config.json.
    conf = the dictionary object for config values
    conf_init = the initial state of the conf dictionary when it was last loaded from a file.
    is_dirty() = compares Config.conf and conf_init to determine if the configuration has changed since load
    load_config() = loads json data from a file and writes to Config.conf, with config.json as the default. Updates Config.loaded_config if the filepath differs from teh default (or whatever was last loaded). Returns {} if no valid file could be found.
    store_config() = writes the current contents of Config.conf to the file at the Config.loaded_config path
    '''
    loaded_config = 'config.json'

    def load_config(fpath='config.json'):
        try:
            with open(fpath, 'r') as f:
                data = loads(f.read())
        except FileNotFoundError:
            data = {}
        try:
            Config.conf = data
            Config.conf_init = deepcopy(Config.conf)
            if data != {} and fpath != Config.loaded_config:
                Config.loaded_config = fpath
        except NameError:
            return data

    def store_config():
        fpath = Config.loaded_config
        with open(fpath, 'w') as f:
            f.write(dumps(Config.conf))

    def is_dirty() -> bool:
        if Config.conf != Config.conf_init:
            return True
        else:
            return False

    def pretty():
        return pformat(Config.conf)

    conf = load_config()
    conf_init = deepcopy(conf)