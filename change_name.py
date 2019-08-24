"""
This Script is used to change all .md files names
"""

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


import os
import sys

dir_name = sys.argv[1]
directory = os.path.join(os.path.abspath('.'), dir_name)
files_to_change = [x for x in os.listdir(directory) if x.endswith('.md') and x.startswith('#')]
#  files_to_change = [os.path.splitext(x)[0] for x in os.listdir(directory) if x.endswith('.md') and x.startswith('#')]


for filename in files_to_change:
    to_change = os.path.splitext(filename)[0]
    replace = []
    for i in range(len(to_change)):
        if to_change[i] == '#' or to_change[i] == '.':
            continue
        elif to_change[i].isalnum():
            replace.append(to_change[i].lower())
        elif to_change[i] == ' ':
            replace.append('_')
    replace.append('.md')
    replace = ''.join(replace)

    # Change dir
    origin_dir = os.path.join(directory, filename)
    after_dir = os.path.join(directory, replace)
    os.rename(origin_dir, after_dir)
    print(f"Done! rename {origin_dir} to {after_dir}")
