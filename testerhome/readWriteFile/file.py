#coding:utf-8


def open_example(in_file):
    file_instance = open(in_file,'r')
    content = file_instance.read()
    file_instance.close()
    print content

def write_utf8(in_file):
    file_instance = open(in_file,'w')

if __name__ == '__main__':
    file = './example.txt'
    open_example(file)