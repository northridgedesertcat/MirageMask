def read_confs(file):
    # 初始化一个空字典来存储元素及其对应的值
    result = {}
    try:
        # 打开 conf.txt 文件
        with open(file, 'r') as file:
            # 逐行读取文件内容
            for line in file:
                # 去除行尾的换行符
                line = line.strip()
                # 检查行中是否包含 '='
                if '=' in line:
                    # 按 '=' 分割每行内容
                    key, value = line.split('=', 1)
                    result[key] = value
    except FileNotFoundError:
        print("未找到 conf.txt 文件，请检查文件路径是否正确。")
    except Exception as e:
        print(f"发生其他错误: {e}")
    return result

if __name__=="__main__":
    a,b,c=read_confs()
    print(a,b,c)