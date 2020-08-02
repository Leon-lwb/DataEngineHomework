# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:14:18 2020

@author: Leon
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


'''生成训练数据；minmax变换'''
data = pd.read_csv('./CarPrice_Assignment.csv', encoding='gbk')
train_x = data.drop(['car_ID','CarName'], axis=1)
     
le = LabelEncoder()
train_x['fueltype'] = le.fit_transform(train_x['fueltype'])
train_x['aspiration'] = le.fit_transform(train_x['aspiration'])
train_x['doornumber'] = le.fit_transform(train_x['doornumber'])
train_x['carbody'] = le.fit_transform(train_x['carbody'])
train_x['drivewheel'] = le.fit_transform(train_x['drivewheel'])
train_x['enginelocation'] = le.fit_transform(train_x['enginelocation'])
train_x['enginetype'] = le.fit_transform(train_x['enginetype'])
train_x['cylindernumber'] = le.fit_transform(train_x['cylindernumber'])
train_x['fuelsystem'] = le.fit_transform(train_x['fuelsystem'])
    
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)


'''
# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
# 使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=5)
y = model.fit_predict(train_x)
print(y)
linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()
'''

# 使用KMeans聚类
kmeans = KMeans(n_clusters=6)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果'}, axis=1, inplace=True)
print(result)
result.to_csv("result.csv", index=False, encoding='gbk')

# 获取和VW品牌聚类结果相同的品牌
result['CarBrand'] = [x.split(' ')[0] for x in result['CarName']]
brand_vw = pd.concat([result[result['CarBrand'] == 'volkswagen'],
                      result[result['CarBrand'] == 'vw'],
                      result[result['CarBrand']=='vokswagen']])
brand_competing_cars = []
for i in brand_vw['聚类结果'].unique():
    brand_competing_cars += list(result[result['聚类结果'] == i]['CarBrand'].unique())
brand_competing_cars = list(set(brand_competing_cars))
brand_competing_cars.remove('volkswagen')
brand_competing_cars.remove('vw')
brand_competing_cars.remove('vokswagen')

print('-' * 60)
print("VW品牌竞品是：")
print(brand_competing_cars)
print('-' * 60)