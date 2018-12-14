import os
import sys

relactive_path=__file__  #相对路径
absolute_path=os.path.abspath(__file__)  #绝对路径
dir1=os.path.dirname(absolute_path)           #返回当前文件所在目录
PATH=os.path.dirname(dir1)          #返回当前文件所在目录去掉后一个
print(dir1)
print(PATH)

# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__) ))
sys.path.append(PATH)
from core import main
main.login()

list=map(lambda x:x%2,range(3))



print(list)
for i in list:
    print(i)