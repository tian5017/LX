import pandas as pd
import time
import csv

# 开始计时
start = time.clock()

# 为汇总的输出，建立一个CSV文件，并包含表头字段明
with open('pd_sum.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    # 写入columns_name
    writer.writerow(['date', 'area', 'order_type', 'qty', 'revenue'])

# 分块处理
reader = pd.read_csv('sample_data.csv', encoding='gbk', iterator=True)
i = 0
while True:
    # 每次循环开始时间
    start2 = time.clock()
    try:
        df = reader.get_chunk(1000000)
        mini_sum = df.groupby(['date', 'area', 'order_type']).sum()
        mini_sum.to_csv('pd_sum.csv', mode='a', header=False)
        i = i + 1
        end2 = time.clock()
        # 每次循环结束时间
        print('{} 秒: completed {} rows'.format(end2 - start2, i * 1000000))
    except StopIteration:
        print("Iteration is stopped.")
        break
