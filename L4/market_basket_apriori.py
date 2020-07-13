import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

# 数据加载
# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
# shape为(7501,20)
print(dataset.shape)

# 将数据存放到transactions中
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)
    
def eff_apriori():
    '''使用efficient_apriori挖掘频繁项集和频繁规则'''
    
    from efficient_apriori import apriori
    
    itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.4)
    print("频繁项集：", itemsets)
    print("关联规则：", rules)


#def mlx_apriori():
#    '''使用mlxtend挖掘频繁项集和频繁规则'''
# 
#    from mlxtend.frequent_patterns import apriori
#    from mlxtend.frequent_patterns import association_rules
#    
#    # 挖掘频繁项集，最小支持度为0.02
#    itemsets = apriori(transactions, use_colnames=True, min_support=0.02)
#    # 按照支持度从大到小进行排列
#    itemsets = itemsets.sort_values(by="support" , ascending=False) 
#    print('-'*20, '频繁项集', '-'*20)
#    print(itemsets)
#    # 根据频繁项集计算关联规则，设置最小提升度为2
#    rules = association_rules(itemsets, metric='lift', min_threshold=2)
#    # 按照提升度从大到小进行排序
#    rules = rules.sort_values(by="lift", ascending=False) 
#    #rules.to_csv('./rules.csv')
#    print('-'*20, '关联规则', '-'*20)
#    print(rules)

eff_apriori()
#mlx_apriori()
'''老师，使用mlx_apriori()一直报错“AttributeError: 'list' object has no attribute 'size'”。。。不知为何。。。'''
