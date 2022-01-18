import os

def re_fileName(path):
    filename_list = os.listdir(path)
    a = 0
    for i in filename_list:
        used_name = path + filename_list[a]
        print("u "+used_name)
        new_name = path + used_name.replace(" ", "_")
        print("n "+new_name)
        os.rename(used_name, new_name)
        print("文件%s重命名成功,新的文件名为%s" % (used_name, new_name))
        a += 1

if __name__ == '__main__':
    dir = "D:/新建文件夹/article/文献/"
    print("打印文件名+++")
    for root, dirs, files in os.walk(dir):
        #print(root)
        for file in files:
            #print(file)
            fileName, extension = os.path.splitext(file)
            if extension == '.pdf':
                print(root+'/'+fileName+extension)
                os.system("python pdf2txt.py -o \"{}.txt\" \"{}.pdf\"".format(root+'/'+fileName, root+'/'+fileName))
    print("+++")

