import os.path

import yaml

basic_path=os.path.dirname(__file__)


def read_yaml(filename):
    file=os.path.join(basic_path,"data",filename)
    return yaml.safe_load(open(file=file))
