#!/usr/bin/env python     
# -*- coding: UTF-8 -*- 

# pandas用来做数据处理。
import pandas as pd  
# numpy用来做高维度矩阵运算.
import numpy as np  
# matplotlib用来做数据可视化。
#import matplotlib.pyplot as plt

import csv
import numpy as np




print type(a) == float

names = ['Bob','Jessica','Mary','John','Mel']

#创建一个names列表
births = [968,155,77,578,973]  #创建一个births 列表
DataSet = list(zip(names,births))  #用 zip 函数将这两个列表合并在一起

df = pd.DataFrame(data = DataSet ,columns=['Names','Births'])
#用生成的数据生成一个DataFrame对象


# 将创建的数据写入到/opt/births1880.csv文件中，如图4所示。
#将df写入到文件中
df.to_csv('D:/births1880.csv', index=False, header=False, sep=',')


ifile  = open('D:/births1880.csv', "rb",encoding='gbk')
reader = csv.reader(ifile)
ofile  = open('D:/ttest.csv', "wb")
writer = csv.writer(ofile, delimiter=chr(0x0f), quotechar='"', quoting=csv.QUOTE_ALL)
for row in reader:
    writer.writerow(row)
ifile.close()
ofile.close()