 # -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : .ui 文件转为 .py 文件工具，一般不使用，直接手写 UI 更好管理

@Attention :
"""

import os
import os.path


# 文件所在的路径
file_dir = '.'


def ui_file_list():
    """ 找出路径下所有的.ui文件

    :return:
    """
    file_list = []
    files = os.listdir(file_dir)
    for filename in files:
        # print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            file_list.append(filename)
    return file_list


def trans_file(filename):
    """ 把扩展名为.ui的转换成.py的文件

    :param filename:
    :return:
    """
    return os.path.splitext(filename)[0] + '.py'


def main():
    """ 通过命令把.ui文件转换成.py文件

    :return:
    """
    file_list = ui_file_list()
    for file in file_list:
        py_file = trans_file(file)
        cmd = 'pyuic5 -o {0} {1}'.format(py_file, file)
        os.system(cmd)


if __name__ == "__main__":
    main()
