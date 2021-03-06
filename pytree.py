#!/usr/bin/env python3

import os
import sys
import subprocess
import string
import re


indent = '│   '
space = '    '

branch = '├── '
end_branch = '└── '


def print_tree(cpath, padding):
    children = [child for child in os.listdir(cpath) if not child.startswith('.')]
    children = sorted(children, key=lambda x: re.sub('[^a-zA-Z0-9]+', '', x).lower())
    dir_num = 0
    file_num = 0
    for index in range(len(children)):
        child = children[index]
        if index < len(children) - 1:
            next_padding = indent
            print(padding + branch + child)
        else:
            print(padding + end_branch + child)
            next_padding = space
        if os.path.isfile(os.path.join(cpath, child)):
            file_num += 1
        else:
            dir_num += 1
            t_dir_num, t_file_num = print_tree(os.path.join(cpath, child), padding + next_padding)
            dir_num += t_dir_num
            file_num += t_file_num
    return dir_num, file_num


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(".")
        current_path = os.getcwd() + '/'
    # elif len(sys.argv) == 2:
    else:
        temp = sys.argv[1]
        if temp[0] != '/':
            current_path = os.getcwd() + '/' + temp + '/'
        else:
            current_path = temp + '/'
        print(temp)
    dir_num, file_num = print_tree(current_path, "")
    print('\n' + str(dir_num) + " directories, " + str(file_num) + " files")
