import os

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def fileDirs(path):
    ori_dirs = []
    for file in os.listdir(path):
        ori_dirs.append(os.path.join(path, file))
    return ori_dirs

