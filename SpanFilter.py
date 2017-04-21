import shutil
import os

class SpanFilter(object):
    #初始化的时候把目录文件读入内存
    def __init__(self, index_file_path):
        self.index_dict = {}
        self.count_ham = 0
        self.count_span = 0
        with open(index_file_path,'r') as fp:
            for index in fp:
                type = index.split(' ')[0]
                path = index.split(' ')[1]
                self.index_dict[path.strip()] = type
                #print (path)
        current_path = os.getcwd()
        current_path += '/trec06c/full'
        os.chdir(current_path)

    def run(self):
        for path in self.index_dict:
            if self.index_dict[path] == 'ham':
                shutil.copyfile(path, '/home/yqh/span_filter/Ham/' + str(self.count_ham) + '.txt')
                self.count_ham += 1
            elif self.index_dict[path] == 'spam':
                shutil.copyfile(path, '/home/yqh/span_filter/Span/' + str(self.count_span) + '.txt')
                self.count_span += 1
            else:
                print ("error drop it!!")

            print ("now copying file......")




s = SpanFilter('./trec06c/full/index')
s.run()

