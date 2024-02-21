# -*- coding = utf-8 -*-
# @Time : 2022/7/29 16:28
# @File : 数据可视化.py
# @Software: PyCharm

from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd

df = pd.read_csv('315老坛酸菜.csv')
df_to_dit = df.to_dict()
x = list(df['作者'].values)
print(x)
y = list(df['播放量'].values)
y_1 = []
for i in y:
    y_1.append(int(i))
c = (
    Bar()
    .add_xaxis(x[:10])
    .add_yaxis('播放量', y_1[:10])
)
c.render('播放量图表.html')

