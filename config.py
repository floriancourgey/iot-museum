import os
import shutil
import yaml

filename = 'config.yml'

if not os.path.isfile(filename):
    shutil.copy(filename+'.dist', filename)

config = yaml.load(open(filename))
