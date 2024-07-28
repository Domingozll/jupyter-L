# coding:utf-8
# @SoftWare PyCharm
# @FileName demo01.py
# @Auther zhanglin
# @Date 2021/05/24/0024 10:12
# @Describe python中的io操作

# file = open(filename [,mode(打开模式，默认为只读),encoding(文件编码，windows打开默认为gbk，python默认保存utf-8)])

# r只读模式
# w只写模式，文件不存在则创建文件，文件存在则覆盖，文件指针在文件开头。
# a以追加模式打开文件，文件不存在则创建，存在则在文件末尾追加
# b以二进制打开文件，不能单独使用，须与其他模式一起使用，rb,或wb
# +以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
# file.write('hello python')
file = open('b.txt','r')
print(file.readlines())
file.close()


print('--------文件对象的常用方法----------')
print('read([size]) 从文件中读取size个字节或字符的内容返回，若省略size则读取全部内容。')
print('readLine() 从文件中读取一行内容')
print('readLines() 把文本中每一行都作为独立的字符串对象，并将这些对象放到列表返回')
print('write(str) 将字符串str写入文件')
print('writelines(s_list) 将字符串列表s_list写入文件，不添加换行符')
print('''seek(offset,[,whence]) 将文件指针移动到新的位置，offset表示相对于whence的位置：
       offset为正往结束方向移动，为负往开始方向移动
       whence不同的值代表不同的含义 0：从文件头开始计算，1：从当前位置开始计算 2：从文件尾开始计算''')
print('tell() 返回文件指针的当前位置')
print('flush() 把缓冲区的内容写入文件，但不关闭文件')
print('close() 把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源')
print('--------文件对象的常用方法--end-----')
print('\n')

print('--------with语句（上下文管理器）------')
# with语句（上下文管理器）
# with语句可以自动管理上下文资源，无论什么原因跳出with语句块，都能确保文件的正确关闭，以此来达到资源释放的目的
with open('b.txt','r') as file:
    print(file.readline())
'''
MyContent实现了特殊方法 __enter__(),__exit__()称该类对象遵守了上下文管理协议
该类的实例对象称为上下文管理器
'''
class MyContent(object):
    def __enter__(self):
        print('enter方法被调用')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用')
    def show(self):
        print('show方法被调用')
with MyContent() as mycontent:
    mycontent.show()
print('--------with语句（上下文管理器--end------')
print('\n')