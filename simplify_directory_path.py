# -*- coding: utf-8 -*-
"""
Simplify Directory Path
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
"""
def simplified_directory_path(path):
    # dirs = path.split('/')[1:-1]
    dirs = [x for x in path.split('/')[1:] if x]
    print dirs
    dir_stack = []
    for seq in dirs:
        if seq not in ['.', '..']:
            dir_stack.append(seq)
        else:
            if seq == '..':
                # To neglect any erroneous ../ when already in root dir
                if dir_stack:
                    dir_stack.pop()
    if dir_stack:
        return '/'+'/'.join(dir_stack)
    else:
        return '/'
if __name__ == '__main__':
    path = "/a/./b/../../c/"
    path = '/home/'
    path = '/'
    path = "/home//foo/"
    path = "/..."
    print simplified_directory_path(path)
