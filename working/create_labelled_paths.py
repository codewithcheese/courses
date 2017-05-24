"""
    Creates required paths for vgg16 and moves files based on the label in their name.

    /train/dogs.0.jpg -> /train/dogs/dogs.0.jpg
    /train/cats.0.jpg -> /train/cats/cats.0.jpg
    random /train/cats.X.jpg -> /valid/cats/cats.X.jpg
    random /train/dogs.X.jpg -> /valig/cats/cats.X.jpg
"""
import os
import random
from shutil import copy

path = 'data/sandbox/'

# mv files to train directory
if not os.path.exists(path + 'train/'):
    raise Exception('train directory does not exist.')

for file in os.listdir(path + 'train/'):

    if file in ['.', '..'] or os.path.isdir(path + 'train/' + file):
        continue

    file_parts = file.split('.')

    if not os.path.exists(path + 'train/' + file_parts[0] + '/'):
        os.makedirs(path + 'train/' + file_parts[0] + '/')

    os.rename(path + 'train/' + file, path + 'train/' + file_parts[0] + '/' + file)

# create a valid path and copy a random selection
for root, dirs, files in os.walk(path + 'train/'):
    if len(files) == 0:
        continue
    random.shuffle(files)
    selection = files[:1000]
    for file in selection:
        file_parts = file.split('.')

        if not os.path.exists(path + 'valid/' + file_parts[0] + '/'):
            os.makedirs(path + 'valid/' + file_parts[0] + '/')

        copy(root + '/' + file, path + 'valid/' + file_parts[0] + '/' + file)


