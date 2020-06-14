#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Action1：求2+4+6+8+...+100的求和，用Python该如何写
a=2
sum = 0
while a<101:
 sum=sum+a
 a=a+2
print(sum)


# In[46]:


import numpy as np
arange=np.arange(2,101,2)
sum=np.sum(arange)
print(arange)
print(sum)


# In[97]:


# 统计全班的成绩
# 班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
# coding=utf-8
import pandas as pd
data = {'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
#print(data)
df = pd.DataFrame(data,index=['张飞', '关羽', '刘备', '典韦','许诸'])
df.index.name='姓名'
df1=df.describe().loc[['mean','max','min','std']]
print(df1)
df['总分']=df.sum(axis=1)
df['名次']=df['总分'].rank()
df.sort_values('总分',ascending=0)


# In[63]:


# 对汽车投诉信息进行分析 

#Step1，数据加载
import pandas as pd
result = pd.read_csv('car_data_analyze/car_complain.csv')
#print(result)


#Step2，数据预处理   拆分problem类型 => 多个字段
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
#print(result)

#Step3，数据统计     对数据进行探索：品牌投诉总数，车型投诉总数 哪个品牌的平均车型投诉最多
df= result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=0)
print('品牌投诉总数：','\n',df)
df2= result.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=0)
print('车型投诉总数：','\n',df2)
df3= result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=0)
print('平均车型投诉最多的品牌：','\n',df3)



# In[ ]:





# In[ ]:




