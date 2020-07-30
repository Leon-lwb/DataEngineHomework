# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:57:35 2020

@author: Leon
"""


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def get_transaction(path):
    '''获取列表'''
    data = pd.read_csv(path, encoding='gbk')
    #进行hotcode编码
    df = data.groupby(['客户ID','产品名称']).value_counts().unstack().fillna(0).reset_index().set_index('客户ID')
    df = df.applymap(lambda x:0 if x<=0 else 1 )
    return df


def mlx_apriori(transaction, min_surpport, min_threshold):
    '''用apriori计算频繁项集和关联规则'''
    frequent_itemsets = apriori(transaction, min_surpport=min_surpport, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
    frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
    print("-"*60)
    print('频繁项集：', frequent_itemsets)
    pd.options.display.max_columns = 50
    rules = rules.sort_values(by='lift', ascending=False)
    print("-"*60)
    print('关联规则：', rules)
    print("-"*60)

    return frequent_itemsets, rules


def main():
    min_surpport = 0.05
    min_threshold = 1
    path = r'./订单表.csv'
    frequent_itemsets, rules = mlx_apriori(get_transaction(path), min_surpport, min_threshold)


if __name__ == "__main__":
    main()

    
