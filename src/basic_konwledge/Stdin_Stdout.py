'''
python 标准输入输出函数
'''
import  sys

# #输入一行
# print("please input your name")
# #.strip()是因为这样获得的输入以/n为结尾，去掉/n
# name = sys.stdin.readline().strip('\n')
# print('hello',name)
#
# print(input("please input your language\n"))
#
#
#
# #输入内容用list存储
# print("please  input your phone num")
# line = sys.stdin.readline().strip()
# nums = list(map(int,line.split(",")))
# print(nums)
#
# print(list(map(int,input("please input your card num\n").split(','))))


# #输入多行
# for line in sys.stdin:
#     print(line.strip())


#标准输出  stdout
#等价于print(123)
sys.stdout.write(str(123)+'\n')

#标准输出重定向
#先保存原来的输出位置，完成特定输出后转化回来
temp = sys.stdout
sys.stdout = open('test.txt','w')
print('hello world')
sys.stdout = temp #恢复默认映射关系
print('nice')