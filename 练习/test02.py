import pandas as pd
import numpy as np
import csv

date = ['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04', '2017-11-05', '2017-11-06', '2017-11-07']
area = ['华北', '华东', '华南', '西南', '华中', '东北', '西北']
order_type = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 随机抽样100万次，各个日期出现的概率是P
col1 = np.random.choice(date, 1000000, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.1])
col2 = np.random.choice(area, 1000000, p=[0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1])
col3 = np.random.choice(order_type, 1000000, p=[0.05, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05])
col4 = np.random.choice(100, 1000000)
col5 = np.random.choice(10000, 1000000)

df = pd.DataFrame({'date': col1, 'area': col2, 'order_type': col3, 'qty': col4, 'revenue': col5})
df = df.set_index('date')

with open('sample_data.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date', 'area', 'order_type', 'qty', 'revenue'])

# 为了减少内存占用，没有直接在上面生成1亿行数据，先生产100万，然后循环100次
for i in range(100):
    i = i+1
    df.to_csv('sample_data.csv', encoding='gbk', header=False, mode='a')
    print(i * 1000000)

