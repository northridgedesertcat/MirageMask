import sys
import os


def get_curry_path_name():
    path = sys.argv[0]
    path = path.split("\\")
    name=path[-1]
    path = "\\".join(path[0:-2]) + "\\"
    return path,name

def get_file_name(path):
    # 提取文件名和扩展名
    file_name = os.path.basename(path)
    name_without_extension, extension = os.path.splitext(file_name)
    # 去掉扩展名的文件名
    # result = name_without_extension
    return file_name

def copy_file(source, destination):
    with open(source, 'rb') as src_file:
        with open(destination, 'wb') as dest_file:
            dest_file.write(src_file.read())

if __name__=="__main__":
    a=get_file_name("file\\1.mp4")
    print(a)