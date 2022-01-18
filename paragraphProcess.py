import nltk
import nltk.data
#from stanfordcorenlp import StanfordCoreNLP
import os
import sys
import codecs

# nlp = StanfordCoreNLP(r'G:\SUTU\jar\stanford-corenlp-4.3.2', lang='en')

def splitPara(para, path):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(para)
    temp = sentences
    for i in sentences:
        # print(i)
        if len(i) < 20:
            temp.remove(i)
    for j in temp:
        print(j)
    with codecs.open(file, 'w', 'utf-8') as writeFile:
        for l in temp:
            writeFile.write(l+'\n')
    writeFile.close()

    return sentences


def rewriteFile(path):
    print(path)
    with codecs.open(path, 'utf-8') as file:
        # 读取每一行
        lines = file.readlines()

    # 空字符（中间不加空格）
    a = ''
    for line in lines:
        # strip()是去掉每行末尾的换行符\n 1
        # print(line)
        if len(line) > 1 and line[-2] == '-':
            line = line[0:-2] + ' \n'
        if len(line)>1 and line[-1] == ' ':
            line = line[0:-1]

        a += line.strip()
    a = a.replace(';', '. ')
    # a = a.replace('.', '. ')
    # print("a")
    # 至此得到了我们需要的 拼接好的字符串
    # print(a)
    splitPara(a, path)


if __name__ == '__main__':
    dir = "E:/mydata/mytxt"
    print("正在处理:")
    for root, dirs, files in os.walk(dir):
        for file in files:
            fileName, extension = os.path.splitext(file)
            if extension == '.txt':
                rewriteFile(root + '/' + fileName + extension)
                # sys.exit()

